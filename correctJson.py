import json

def fix_json(file_path, output_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # If decoding succeeds, attempt to write the corrected JSON
        with open(output_path, 'w') as output_file:
            json.dump(data, output_file, indent=2)

        print(f"JSON successfully loaded and written to: {output_path}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

        # Attempt to fix the JSON by removing characters causing the issue
        with open(file_path, 'r') as file:
            json_content = file.read()

        # Remove problematic characters (e.g., "{http://schem")
        cleaned_content = json_content.replace('{http://schem', '')

        # Write the cleaned content to a new file
        with open(output_path, 'w') as output_file:
            output_file.write(cleaned_content)

        print(f"JSON decoding issue fixed. Cleaned JSON saved to: {output_path}")

# Replace 'input_file_path' with the actual path to your problematic sysmon.json file
# Replace 'output_file_path' with the desired output path for the cleaned JSON
input_file_path = '/Users/hvaandres/Documents/Git/hashencrypt/sysmon.json'
output_file_path = '/Users/hvaandres/Documents/Git/hashencrypt/sysmon_cleaned.json'

fix_json(input_file_path, output_file_path)
