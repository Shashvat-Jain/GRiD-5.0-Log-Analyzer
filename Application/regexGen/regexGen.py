# Will generate a regex from LLM Model using Logines
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from regexGen.features import MODEL_TO_EXTRACT
import langchain

MODEL_NAME = "google/flan-t5-small"
INPUT_PROMPT_LOG_REGEX = ""

# fine tune the model by using the csv file and langchain to re tune model
# def train_model(model, tokenizer, train_csv_file):


def generateReg(logLines, model, tokenizer):
    logText = ""
    for logLine in logLines:
        logText += logLine + "\n"
    input_ids = tokenizer("Extract regex as per the following log line: " + logText,
                          return_tensors="pt").input_ids
    with tokenizer.as_target_tokenizer():
        answer_ids = model.generate(input_ids)
        answer = tokenizer.decode(answer_ids[0], skip_special_tokens=True)
    regex = answer
    return regex


def reGenerateReg(logLine, model, tokenizer):
    input_ids = tokenizer("Improve the previous regex using this logline " + logLine,
                          return_tensors="pt").input_ids
    with tokenizer.as_target_tokenizer():
        answer_ids = model.generate(input_ids)
        answer = tokenizer.decode(answer_ids[0], skip_special_tokens=True)
    regex = answer
    return regex


def modelInitializer():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return model, tokenizer


if __name__ == "__main__":
    model, tokenizer = modelInitializer()
    MODEL_TO_EXTRACT = ["User", "Access", "Action"]
    regex = generateReg(model)
    print(regex)
