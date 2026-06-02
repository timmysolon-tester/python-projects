import csv
import os


print ("=============IT Inventory Tracker==================")
print ("1. Add new device")
print ("2. View all devices")
print ("3. Search for a device")
print ("4. Update device information")
print ("5. Delete a device")
print ("6. Exit")
print ("==================================================")
while True:
    choice = input("Choice: ")
    if choice == '1':
        # Add new device logic here
        device_name = input("Enter device name: ")
        device_type = input("Enter device type: ")
        device_serial = input("Enter device serial number: ")
        device_status = input("Enter device status (e.g., 'In Use', 'Available', 'Under Repair'): ")
    file_exists = os.path.exists("devices.csv")
    if not file_exists:    
        with open("devices.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Type", "Serial Number", "Status"])
            writer.writerow([device_name, device_type, device_serial, device_status])
        pass
    elif choice == '2':
        # View all devices logic here
        if not os.path.exists("devices.csv"):
            print("No devices found. Please add a device first.")
        else:
            with open("devices.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"Name: {row['Name']}, Type: {row['Type']}, Serial Number: {row['Serial Number']}, Status: {row['Status']}")
        pass
    elif choice == '3':
        # Search for a device logic here
        search_term = input("Enter device name or serial number to search: ")
        with open("devices.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term in row:
                    print(row)
        pass
    elif choice == '4':
        # Update device information logic here
        search_term = input("Enter device name or serial number to update: ")
        updated_info = input("Enter new device information (Name, Type, Serial Number, Status): ")
        updated_info_list = updated_info.split(", ")
        with open("devices.csv", "r") as file:
            reader = csv.reader(file)
            devices = list(reader)
        with open("devices.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for row in devices:
                if search_term in row:
                    writer.writerow(updated_info_list)
                else:
                    writer.writerow(row)
        pass
    elif choice == '5':
        # Delete a device logic here
        search_term = input("Enter device name or serial number to delete: ")
        with open("devices.csv", "r") as file:
            reader = csv.reader(file)
            devices = list(reader)
        with open("devices.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for row in devices:
                if search_term not in row:
                    writer.writerow(row)
        pass
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
