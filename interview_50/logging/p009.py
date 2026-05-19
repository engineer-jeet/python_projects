# You receive Kubernetes logs:
# Return count of each pod state.

# Requirements:

# Ignore malformed entries.
# Status field position may vary.

# note : here key shopuld be pod_name and status

logs = [
"pod=api-7f9d status=Running",
"pod=worker-22a status=CrashLoopBackOff",
"pod=db-91c status=Running",
"pod=worker-22a status=CrashLoopBackOff"
]



def count_pod_state(logs):

    pod_state_freq = {}

    for log in logs:

        pod = None
        status = None

        parts = log.split()
        for part in parts:
            if part.startswith("pod="):
                pod = part.split("=")[1]

            if part.startswith("status="):
                status = part.split("=")[1]

        if pod and status:
            key = (pod, status)

            if key not in pod_state_freq:
                pod_state_freq[key] = 1
            else:
                pod_state_freq[key] += 1

    return pod_state_freq


print(count_pod_state(logs))