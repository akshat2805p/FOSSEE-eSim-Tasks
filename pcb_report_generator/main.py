from analyzer import analyze_components
from report_writer import generate_report

with open("sample_data.txt", "r") as file:
    data = file.readlines()

results = analyze_components(data)

report = generate_report(results)

with open("report.txt", "w") as file:
    file.write(report)

print("Report generated successfully!")