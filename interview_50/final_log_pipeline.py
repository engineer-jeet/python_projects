# You are building a simple log analysis utility for distributed services.
#Log files contain entries in the following format:

#line = "2024-01-15T10:12:01.101Z[auth-service][INFO]User login request received"


import os
import re


def parse_log_line(line):
    line = line.strip()

    first_bracket = line.find("[")
    second_bracket = line.find("]", first_bracket)
    third_bracket = line.find("[", second_bracket)
    fourth_bracket = line.find("]", third_bracket)

    if -1 in (first_bracket, second_bracket, third_bracket, fourth_bracket):
        return None
    
    timestamp = line[:first_bracket]
    service = line[first_bracket+1 : second_bracket]
    level = line[third_bracket+1 : fourth_bracket]
    message = line[fourth_bracket+1 : ].strip()

    return {
        "timestamp" : timestamp,
        "service" : service,
        "level" : level,
        "message" : message
    }



def parse_log_line_new(line):
    pattern = r'^(.*?)\[(.*?)\]\[(.*?)\](.*)$'
    match = re.match(pattern, line.strip())
    
    if not match:
        return None
    
    timestamp, service, level, message = match.groups()
    
    return {
        "timestamp": timestamp,
        "service": service,
        "level": level,
        "message": message.strip()
    }
    
def load_logs_from_directory(folder_path):
    aggregated_logs = []

    files = os.listdir(folder_path)

    for file in files:
        if file.endswith(".log"):
            filepath = os.path.join(folder_path, file)

            with open(filepath) as f:
                for line in f:
                    parsed = parse_log_line(line)
                    if parsed:
                        aggregated_logs.append(parsed)
    return aggregated_logs


def filter_by_severity(logs, severity):
    severity = severity.lower()
    filetered = []

    for log in logs:
        if log['level'].lower() == severity:
            filetered.append(log)

    return filetered


def group_logs_by_service(logs, severity):
    severity = severity.lower()

    grouped = {}

    for log in logs:
        if log["level"].lower() == severity:
            service = log["service"]
            if service not in grouped:
                grouped[service] = []

            grouped[service].append(log)

    return grouped


def identify_patterns(logs, severity):
    severity = severity.lower()
    message_count = {}

    for log in logs:
        if log["level"].lower() == severity:
            msg = log["message"]

            if msg not in message_count:
                message_count[msg] =1
            else:
                message_count[msg] +=1
    return message_count




folderpath = "log_files"
logs = load_logs_from_directory(folderpath)
filtered = filter_by_severity(logs, "error")
print(group_logs_by_service(logs,"error"))







