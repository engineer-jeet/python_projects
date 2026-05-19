# Monitoring systems often generate noisy alerts. 
# Suppose duplicate alerts occurring within 5 minutes should be suppressed.
# Return only alerts that should actually be emitted.

alerts = [
("CPU_HIGH","10:00"),
("CPU_HIGH","10:02"),
("DISK_FULL","10:03"),
("CPU_HIGH","10:08")
]

alerts = [
    ("CPU_HIGH","10:00"),
    ("CPU_HIGH","10:02"),
    ("DISK_FULL","10:03"),
    ("CPU_HIGH","10:08")
]

def duplicate_alerts(alerts):

    emitted = []
    last_seen = {}

    for alert_name, time in alerts:
        #print(alert_name, time)

        hour, minute = time.split(":")
        total_minutes = int(hour)*60 + int(minute)

        if alert_name not in last_seen:
            emitted.append((alert_name, time))
            last_seen[alert_name] = total_minutes
            

        elif total_minutes - last_seen[alert_name] >= 5:
            emitted.append((alert_name, time))
            last_seen[alert_name] = total_minutes

    return emitted


print(duplicate_alerts(alerts))
 