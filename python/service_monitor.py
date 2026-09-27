import requests, json, datetime

urls = ["https://example.com", "https://google.com", "https://okyere-nock.homes"]
results = []

for url in urls:
    data = {"url": url, "time": str(datetime.datetime.now()), "status": "unhealthy"}

    try:
        res = requests.get(url, timeout=5)
        data["status_code"] = res.status_code
        data["ms"] = round(res.elapsed.total_seconds() * 1000, 2)
        if res.status_code == 200:
            data["status"] = "healthy"
    except Exception:
        date["error"] = "Failed"
    results.append(data)

with open("reports/service-report.json", "w") as f:
    json.dump(results, f, indent=2)

print("saved/service-report.json")



