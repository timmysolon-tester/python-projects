import matplotlib.pyplot as plt
import csv
import os
import pandas as pd

file_exists = os.path.exists("network_log.csv")
if not file_exists:
    print("Log file not found. Please ensure 'network_log.csv' exists in the current directory.")
    exit()

with open("network_log.csv", "r") as csv_file:
    network_log = list(csv.DictReader(csv_file))
def compute_uptime_percentages(csv_path="network_log.csv"):
    """Return a dict mapping device -> uptime percentage (0-100).

    csv_path: path to the CSV file. Keeps function testable and import-friendly.
    """
    df = pd.read_csv(csv_path)
    up_devices = df[df['Status'] == 'UP']
    down_devices = df[df['Status'] == 'DOWN']
    devices = sorted(set(df['Device']))
    result = {}
    for device in devices:
        up_count = len(up_devices[up_devices['Device'] == device])
        down_count = len(down_devices[down_devices['Device'] == device])
        total_count = up_count + down_count
        uptime_percentage = (up_count / total_count) * 100 if total_count > 0 else 0.0
        result[device] = uptime_percentage
    return result


def network_report(csv_path="network_log.csv"):
    print("===== Network Uptime Report =====")
    uptime = compute_uptime_percentages(csv_path)
    print(f"Total records: {len(network_log)}")
    print(f"Devices monitored: {len(uptime)}")
    print("Device \t\tUptime %")
    for device, uptime_percentage in uptime.items():
        print(f"{device} \t{uptime_percentage:.2f}%")


if __name__ == "__main__":
    network_report()

