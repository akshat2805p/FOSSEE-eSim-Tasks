import json
import os

def generate_report(stats):

    report_path = os.path.join(
        os.path.dirname(__file__),
        "pcb_health_report.json"
    )

    with open(report_path, "w") as report_file:
        json.dump(stats, report_file, indent=4)

    print(f"Report generated at: {report_path}")