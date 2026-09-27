import json

counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_lines = []

with open("logs/app.log", "r") as f:
    for line in f:
        if "INFO:" in line:
            counts["INFO"] += 1
        elif "WARNING:" in line:
            counts["WARNING"] += 1
        elif "ERROR:" in line:
            counts["ERROR"] += 1
            error_lines.append(line.strip())

report = {
    "summary": counts,
    "error_details": error_lines
}

with open("reports/log-report.json", "w") as file:
    json.dump(report, file, indent=4)

print("DONE")
