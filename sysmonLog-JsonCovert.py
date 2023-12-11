import Evtx.Evtx as evtx
import xmljson
from xml.etree.ElementTree import fromstring
import json

def convert_evtx_to_json(evtx_filepath, json_filepath):
    """
    Converts an .evtx file to a JSON file.

    Args:
      evtx_filepath: Path to the .evtx file.
      json_filepath: Path to the output JSON file.
    """
    # Open the .evtx file
    with evtx.Evtx(evtx_filepath) as log:
        # Create a JSON file
        with open(json_filepath, "w") as json_file:
            # Iterate over each record and write to JSON
            for record in log.records():
                xml_string = record.xml()
                json_data = xmljson.parker.data(fromstring(xml_string))
                json.dump(json_data, json_file, indent=4)
                json_file.write("\n")

# Example usage
evtx_filepath = "/Users/hvaandres/Documents/Git/hashencrypt/final-sysmon.evtx"
json_filepath = "/Users/hvaandres/Documents/Git/hashencrypt/sysmon.json"
convert_evtx_to_json(evtx_filepath, json_filepath)
print(f"Successfully converted {evtx_filepath} to {json_filepath}")
