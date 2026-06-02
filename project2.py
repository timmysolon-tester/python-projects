import os

file_exists = os.path.exists("system.log")
if not file_exists:
    print("Log file not found. Please ensure 'system.log' exists in the current directory.")
    exit()

with open("system.log", "r") as log_file:
    log_entries = log_file.readlines()

def get_level(entry):
    parts = entry.split()
    return parts[2] if len(parts) >= 3 else "<unknown>"

info_entries = [entry for entry in log_entries if "INFO" in entry]
warning_entries = [entry for entry in log_entries if "WARNING" in entry]
error_entries = [entry for entry in log_entries if "ERROR" in entry]

def show_report():
    print("===== Log Analysis Report =====")
    print("system.log")
    print(f"Total log entries: {len(log_entries)}")
    bar_scale = 3
    print(f"INFO   : {len(info_entries):>3} " + "█" * len(info_entries) * bar_scale)
    print(f"WARNING: {len(warning_entries):>3} " + "█" * len(warning_entries) * bar_scale)
    print(f"ERROR  : {len(error_entries):>3} " + "█" * len(error_entries) * bar_scale)
    print("---- Error Details ----")
    for entry in error_entries:
        parts = entry.split()
        timestamp = " ".join(parts[0:2]) if len(parts) >= 2 else "<unknown>"
        level = get_level(entry)
        print(f"[{timestamp}] {level}: {entry.strip()}")
    print("==============================")

show_report()