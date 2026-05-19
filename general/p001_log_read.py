"""
Python script that:
 - Aggregates logs from multiple files
 - Lets user choose severity
 - Groups logs by service
 - Detects recurring messages
 - Writes the final report into report.txt
"""

import os

# -------------------------------------------------------------
# Parse a single log line WITHOUT regex
# Format: 2024-01-15T14:32:28Z[service][LEVEL]message
# -------------------------------------------------------------

def parse_log_line(line):
    line = line.strip()

    # Find positions of brackets
    first_bracket = line.find("[")
    second_bracket = line.find("]", first_bracket)
    third_bracket = line.find("[", second_bracket)
    fourth_bracket = line.find("]",third_bracket)

    if first_bracket == -1 or second_bracket == -1 or third_bracket == -1 or fourth_bracket == -1:
        return None
    
    timestamp = line[:first_bracket]
    service = line[first_bracket+1 : second_bracket]
    level = line[third_bracket+1 : fourth_bracket]
    message = line[fourth_bracket+1 : ].strip()

    return {
        "timestamp": timestamp,
        "service": service,
        "level" : level,
        "message": message
    }

# -------------------------------------------------------------
# Load all .log files from ./logs using os.listdir
# -------------------------------------------------------------

def load_logs_from_directory(folder_path):
    aggregated_logs = []

    files = os.listdir(folder_path)
    
    for file in files:
        if file.endswith(".log"):
            filepath = folder_path + "/" + file

            with open(filepath) as f:
                for line in f:
                    parsed = parse_log_line(line)
                    if parsed:
                        aggregated_logs.append(parsed)
    
    return aggregated_logs


# -------------------------------------------------------------
# Filter logs by severity
# -------------------------------------------------------------

def filter_by_severity(logs, severity):
    severity = severity.lower()
    filtered = []

    for log in logs:
        if log['level'].lower() == severity:
            filtered.append(log)

    return filtered

# -------------------------------------------------------------
# Group logs by service 
# -------------------------------------------------------------

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

# -------------------------------------------------------------
# Identify recurring patterns 
# -------------------------------------------------------------

def identify_patterns(logs, severity):
    severity = severity.lower()
    message_count = {}

    for log in logs:
        if log["level"].lower() == severity:
            msg = log["message"]

            if msg not in message_count:
                message_count[msg] = 1
            else:
                message_count[msg] += 1

    return message_count


# -------------------------------------------------------------
# Write summary to report.txt
# -------------------------------------------------------------

def write_report(all_logs, severity, grouped, patterns):

    with open("log_files/report.txt", 'w') as rpt:

        rpt.write("\n================ LOG SUMMARY REPORT ================\n\n")

        rpt.write("Total Logs Parsed: " + str(len(all_logs)) + "\n")
        rpt.write("Severity Filter Applied: " + severity.upper() + "\n")

        # Count logs with the chosen severity
        count = 0
        for log in all_logs:
            if log["level"].lower() == severity.lower():
                count+=1

        rpt.write("Matching Logs: " + str(count) + "\n\n")

        rpt.write("---- COUNT BY SERVICE ----\n")
        for service in grouped:
            rpt.write(service + " : " + str(len(grouped[service])) + " logs\n")

        rpt.write("\n---- RECURRING PATTERNS ----\n")
        for msg, cnt in patterns.items():
            if cnt > 1:
                rpt.write("[" + str(cnt) + " occurrences] " + msg + "\n")

        rpt.write("\n====================================================\n")

    print("Report written to report.txt")


# -------------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------------

if __name__ == "__main__":

    logs = load_logs_from_directory("log_files")

    if len(logs) == 0:
        print("No logs found in ./logs folder")
        exit()
    
    print("Choose severity level (error / warning / info): ")
    choice = input("Enter: ").lower()

    if choice not in ["error", "warning", "info"]:
        print("Invalid severity")
        exit()
    
    grouped_logs = group_logs_by_service(logs, choice)
    patterns = identify_patterns(logs, choice)
    write_report(logs, choice, grouped_logs, patterns)

    


    



        













