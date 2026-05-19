# Logs contain inconsistent service naming.
# Normalize them into lowercase trimmed names.

services = [
"PAYMENTS",
"payments",
"Payments ",
" checkout",
"CHECKOUT"
]

def normalize_service_names(logs):

    services = []
    freq = {}

    for log in logs:
        log = log.lower().strip()
        services.append(log)

        if log in freq:
            freq[log] += 1
        else:
            freq[log] = 1

    return services, freq

print(normalize_service_names(services))


