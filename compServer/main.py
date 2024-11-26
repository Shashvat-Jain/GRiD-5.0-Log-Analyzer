import json
from transformers import T5ForConditionalGeneration, T5Tokenizer
from parseComp import PDFParser

def generate_problem_solution(log_data, model, tokenizer):
    pdf_parser = PDFParser('.IT-Policy.pdf')
    pdf_text = pdf_parser.parse_pdf_to_text()
    prompt = f"Log Line {log_data['logline']} indicates a problem with user {log_data['userId']} attempting to {log_data['action']} with access {log_data['access']}. Please provide insights on how this log line issue relates to the compliance document.\n\nCompliance Document Content:\n{pdf_text}\n\nAnswer:"    
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    generated_ids = model.generate(
        input_ids,
        max_length=150,  
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )
    
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    model_name = "google/flanT5-base"  
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    with open("Logs.json", "r") as log_file:
        log_lines = json.load(log_file)
    
    problem_solution_pairs = []

    for log_data in log_lines:
        problem = f"Log Line {log_data['logline']} indicates a problem with user {log_data['userid']} attempting to {log_data['action']} with access {log_data['access']}."
        solution = generate_problem_solution(log_data, model, tokenizer)
        
        problem_solution_pairs.append({
            "problem": problem,
            "solution": solution
        })

    output_file = "problem_solution_pairs.json"
    with open(output_file, "w") as f:
        json.dump(problem_solution_pairs, f, indent=4)
    
    print(f"Generated problem-solution pairs saved to {output_file}")
