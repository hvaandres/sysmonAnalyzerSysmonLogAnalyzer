import json

def analyze_sysmon_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Function to find events based on a specific condition
    def find_events(condition):
        return [event for event in data['events'] if condition(event)]

    # 1. Identify the Creation Event of realvirus.exe
    creation_events = find_events(lambda event: event.get('event_type') == 'file_creation' and
                                               event.get('file_name') == 'realvirus.exe')

    if creation_events:
        creation_event = creation_events[0]
        creation_time = creation_event.get('timestamp')
        created_file_path = creation_event.get('file_path')
        creator_process_name = creation_event.get('creator_process_name')
        creator_process_id = creation_event.get('creator_process_id')

        print("1. Realvirus.exe Creation Event:")
        print(f"   - Date/Time: {creation_time}")
        print(f"   - File Path: {created_file_path}")
        print(f"   - Creator Process: {creator_process_name} (ID: {creator_process_id})")
        print()

    # 2. Identify the Process Creation Event of Executing realvirus.exe
    execution_events = find_events(lambda event: event.get('event_type') == 'process_creation' and
                                                event.get('process_name') == 'realvirus.exe')

    if execution_events:
        execution_event = execution_events[0]
        execution_process_name = execution_event.get('process_name')
        execution_process_id = execution_event.get('process_id')
        parent_process_name = execution_event.get('parent_process_name')
        parent_process_id = execution_event.get('parent_process_id')
        mitre_technique_id = execution_event.get('mitre_technique_id')
        mitre_technique_name = execution_event.get('mitre_technique_name')

        print("2. Realvirus.exe Execution Event:")
        print(f"   - Execution Process: {execution_process_name} (ID: {execution_process_id})")
        print(f"   - Parent Process: {parent_process_name} (ID: {parent_process_id})")
        print(f"   - MITRE Technique: {mitre_technique_id} - {mitre_technique_name}")
        print()

    # 3. Identify the Self-Duplication Event
    duplication_events = find_events(lambda event: event.get('event_type') == 'file_duplication' and
                                                   event.get('file_name') == 'realvirus.exe')

    if duplication_events:
        duplication_event = duplication_events[0]
        duplicated_file_path = duplication_event.get('duplicated_file_path')
        duplicator_user = duplication_event.get('duplicator_user')

        print("3. Realvirus.exe Self-Duplication Event:")
        print(f"   - Duplicated File Path: {duplicated_file_path}")
        print(f"   - Duplicator User: {duplicator_user}")
        print()

# Replace 'your_file_path' with the actual path to your sysmon.json file
analyze_sysmon_json('/Users/hvaandres/Documents/Git/hashencrypt/sysmon.json')
