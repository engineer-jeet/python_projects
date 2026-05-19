# You are given API request logs.
# Write a function that returns all requests whose latency exceeds a given threshold.

logs = [
"GET /orders latency=120ms",
"POST /payments latency=2100ms",
"GET /users latency=80ms",
"POST /checkout latency=4500ms"
]



def slow_requests(logs):
    threshold = 1000

    requests = []

    for log in logs:
        parts = log.split()
        
        for part in parts:
            if part.startswith("latency="):

                latency = part.split("=")[1]
                if int(latency[:-2]) > threshold:
                    requests.append(log)
    return requests
                    


print(slow_requests(logs))