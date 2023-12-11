import json

def is_valid_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        return True
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return False

def analyze_sysmon_json(file_path):
    if not is_valid_json(file_path):
        print("Please fix JSON issues before proceeding with analysis.")
        return

    with open(file_path, 'r') as file:
        data = json.load(file)

    # Check if 'events' key is present
    if 'events' not in data:
        print("JSON does not contain 'events' key. Please check the JSON structure.")
        return

    # Function to find events based on a specific condition
    def find_events(condition):
        return [event for event in data['events'] if condition(event)]

    # Rest of the analysis code remains unchanged

# Replace 'your_file_path' with the actual path to your sysmon.json file
file_path = '/Users/hvaandres/Documents/Git/hashencrypt/sysmon.json'
analyze_sysmon_json(file_path)
