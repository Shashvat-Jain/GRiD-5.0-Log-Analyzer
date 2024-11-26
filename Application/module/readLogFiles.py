# Read Log file in python
from module.typeChange import typeCheck
import os

LOG_SIZE = 20


def readLogFile(log_path):
    log_file_name = log_path.split("/")[-1]
    if not log_file_name.endswith(".log"):
        print("Log File is not a .log file")
        return False, False
    if not os.path.exists(log_path):
        return False, False
    with open(log_path, "r") as f:
        log_files = f.read().split("\n")
    log_files = [log_file for log_file in log_files]
    return log_files, log_files[:LOG_SIZE]


if __name__ == "__main__":
    print(readLogFile("../testLog/SSH.log"))
