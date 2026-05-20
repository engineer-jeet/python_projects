# You are given production logs from multiple services.
# Return the service producing the highest number of failures.

logs = [
"service=checkout status=500",
"service=payments status=200",
"service=checkout status=503",
"service=payments status=500",
"service=checkout status=500"
]

def highest_failed_services (logs):
    failure_count = {}

    for log in logs:
        parts = log.split()

        service = parts[0].split("=")[1]
        status = int(parts[1].split("=")[1])
        
        if status >=500 :

            if service in failure_count:
                failure_count[service] += 1
            else:
                failure_count[service] = 1

    max_service = max(failure_count, key=failure_count.get)
    return max_service

print(highest_failed_services(logs))