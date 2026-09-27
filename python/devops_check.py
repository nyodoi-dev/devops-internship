import subprocess, requests, json, datetime

def run_command(cmd):
    
    try:
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        return result.stdout.strip() or result.stderr.strip()
    except Exception as e:
        return f" Failed: {e}"

def check_url(url):
    
    try:
        res = requests.get(url, timeout=3)
        return {"status": "UP", "code": res.status_code}
    except Exception:
        return {"status": "DOWN", "error": "Connection Failed"}

def main():
    
    report = {
        "timestamp": str(datetime.datetime.now()),
        "system_info": {
            "hostname": run_command("hostname"),
            "uptime": run_command("uptime -p"),
            "disk_usage": run_command("df -h /"),
            "memory": run_command("free -m")
        },
        "services": {
            "cron": run_command("systemctl is-active cron"),
            "fake_service": run_command("systemctl is-active this-does-not-exist") # Failure test
        },
        "urls": {
            "https://github.com": check_url("https://github.com"),
            "https://fake-website-for-testing.com": check_url("https://fake-website-for-testing.com") # Failure test
        }
    }

    with open("reports/system-report.json", "w") as file:
        json.dump(report, file, indent=4)
        
    print("Check complete! Saved to reports/system-report.json")


if __name__ == "__main__":
    main()
