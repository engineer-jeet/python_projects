# Return the most frequent ERROR message.

logs = [
"ERROR Database timeout",
"INFO User login",
"ERROR Database timeout",
"ERROR Redis unavailable",
"ERROR Database timeout"
]

def frequent_error(logs):

    error_frequency = {}

    for log in logs:
        if log.startswith("ERROR"):
            parts = log.split()[1:]
            part = " ".join(parts)

            if part not in error_frequency:
                error_frequency[part] = 1
            else:
                error_frequency[part] += 1
        
    return max(error_frequency, key=error_frequency.get)

        

print(frequent_error(logs))