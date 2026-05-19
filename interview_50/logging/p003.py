# Return the longest streak of consecutive deployment failures.

events = [
"SUCCESS",
"SUCCESS",
"FAILED",
"FAILED",
"FAILED",
"SUCCESS",
"FAILED"
]

def consicutive_failures(events):
    current_count = 0
    max_count = 0

    for event in events:

        if event == "FAILED":
            current_count += 1

            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count
            

print(consicutive_failures(events))