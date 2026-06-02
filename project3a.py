import subprocess
import sys
import re
import matplotlib.pyplot as plt
import pandas as pd


def get_uptime_from_project3():
	proc = subprocess.run([sys.executable, "project3.py"], capture_output=True, text=True)
	out = proc.stdout
	devices = []
	uptimes = []
	for line in out.splitlines():
		if '%' not in line:
			continue
		# Prefer tab-separated parsing (matches project3.py output)
		if '\t' in line:
			parts = [p.strip() for p in line.split('\t') if p.strip()]
			if len(parts) >= 2:
				device = parts[0]
				uptime_part = parts[-1]
				m = re.search(r"([\d.]+)%", uptime_part)
				if m:
					devices.append(device)
					uptimes.append(float(m.group(1)))
					continue
		# Fallback regex parse
		m = re.search(r'^(?P<device>.+?)\s+\d+\s+\d+\s+(?P<uptime>[\d.]+)%$', line.strip())
		if m:
			devices.append(m.group('device'))
			uptimes.append(float(m.group('uptime')))
	return devices, uptimes


devices, uptime_percentages = get_uptime_from_project3()

if not devices:
	# fallback: compute directly from CSV if parsing failed
	df = pd.read_csv("network_log.csv")
	devices = sorted(set(df['Device']))
	uptime_percentages = []
	for device in devices:
		up = len(df[(df['Device'] == device) & (df['Status'] == 'UP')])
		down = len(df[(df['Device'] == device) & (df['Status'] == 'DOWN')])
		total = up + down
		uptime_percentages.append((up / total) * 100 if total > 0 else 0.0)

plt.figure(figsize=(10, 6))
colors = plt.cm.tab10.colors[: len(devices)]
plt.bar(devices, uptime_percentages, color=colors)
plt.title('Network Device Uptime Percentages')
plt.xlabel('Devices')
plt.ylabel('Uptime Percentage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('uptime_report.png')
plt.show()
print("Chart saved as uptime_report.png")