import Evtx.Evtx as evtx
import xmljson
from xml.etree.ElementTree import fromstring
import csv

def extract_data_from_json(json_data):
    """
    Extracts relevant information from JSON data.

    Args:
      json_data: JSON data extracted from EVTX record.

    Returns:
      Tuple of (Event ID, Timestamp, Process ID, Process Path, Parent Process Path, User).
    """
    system_data = json_data.get("{http://schemas.microsoft.com/win/2004/08/events/event}System", {})
    event_id = system_data.get("{http://schemas.microsoft.com/win/2004/08/events/event}EventID", None)
    
    # Check if TimeCreated exists before attempting to access it
    time_created_data = system_data.get("{http://schemas.microsoft.com/win/2004/08/events/event}TimeCreated", {})
    timestamp = time_created_data.get("@SystemTime", "") if time_created_data else ""

    event_data = json_data.get("{http://schemas.microsoft.com/win/2004/08/events/event}EventData", {})
    data = event_data.get("{http://schemas.microsoft.com/win/2004/08/events/event}Data", [])

    # Check if the 'Data' array has enough elements
    if len(data) >= 8:
        process_id = data[3]
        process_path = data[4]
        parent_process_path = data[5]
        user = data[7]
        return event_id, timestamp, process_id, process_path, parent_process_path, user

    # If the 'Data' array doesn't have enough elements, return None values
    return None, None, None, None, None, None

def convert_evtx_to_csv(evtx_filepath, csv_filepath):
    """
    Converts an .evtx file to a CSV file.

    Args:
      evtx_filepath: Path to the .evtx file.
      csv_filepath: Path to the output CSV file.
    """
    # Open the .evtx file
    with evtx.Evtx(evtx_filepath) as log:
        # Create a CSV file
        with open(csv_filepath, "w", newline='', encoding='utf-8') as csv_file:
            # Create a CSV writer
            csv_writer = csv.writer(csv_file)

            # Write header to CSV file
            csv_writer.writerow(["Event ID", "Timestamp", "Process ID", "Process Path", "Parent Process Path", "User"])

            # Iterate over each record and write to CSV
            for record in log.records():
                xml_string = record.xml()
                json_data = xmljson.parker.data(fromstring(xml_string))

                # Extract relevant information from the JSON data
                event_id, timestamp, process_id, process_path, parent_process_path, user = extract_data_from_json(json_data)

                # Write to CSV
                csv_writer.writerow([event_id, timestamp, process_id, process_path, parent_process_path, user])

# Example usage
evtx_filepath = "/Users/hvaandres/Documents/Git/hashencrypt/final-sysmon.evtx"
csv_filepath = "/Users/hvaandres/Documents/Git/hashencrypt/sysmon.csv"
convert_evtx_to_csv(evtx_filepath, csv_filepath)
print(f"Successfully converted {evtx_filepath} to {csv_filepath}")
