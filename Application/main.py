import os
import re
from module.readLogFiles import readLogFile
from regexGen.regexGen import generateReg, modelInitializer

model, tokenizer = modelInitializer()

log_array, log_for_test = readLogFile("./testLog/SSH.log")
if (not log_array or not log_for_test):
    print("Not able to read Log File")
    exit(0)

train_csv_file = "./testLog/SSH.csv"
train_model(model, tokenizer, train_csv_file)
feature = generateReg(log_for_test, model, tokenizer)
# print(feature)
for log in log_array:
    print(log)
    print(re.findall(feature, log))
    print("--------------------------------------------------")
