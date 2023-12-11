import pandas as pd

def analyze_sysmon_csv(csv_filepath):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_filepath)

    # Requirement 1: Identify the Creation Event of realvirus.exe
    creation_event = df[df['Process Path'].str.endswith('realvirus.exe', na=False)]

    if not creation_event.empty:
        print("Creation Event of realvirus.exe:")
        print("Date/Time:", creation_event['Timestamp'].values[0])
        print("Location:", creation_event['Process Path'].values[0])
        print("Process Name/ID:", creation_event['Process Path'].values[0], creation_event['Process ID'].values[0])
        print()

    # Requirement 2: Identify the Process Creation Event of Executing realvirus.exe
    execution_event = df[df['Process Path'].str.contains('realvirus.exe', na=False)]

    if not execution_event.empty:
        print("Process Creation Event of Executing realvirus.exe:")
        print("Process Name/ID:", execution_event['Process Path'].values[0], execution_event['Process ID'].values[0])

        # Check if 'Parent Process Path' and 'Parent Process ID' columns exist
        if 'Parent Process Path' in execution_event.columns and 'Parent Process ID' in execution_event.columns:
            print("Parent Process Name/ID:", execution_event['Parent Process Path'].values[0], execution_event['Parent Process ID'].values[0])
        
        # You may need to adapt the code below based on the actual columns in your CSV file
        if 'MITRE Technique ID' in execution_event.columns and 'MITRE Technique Name' in execution_event.columns:
            print("MITRE Technique ID/Name:", execution_event['MITRE Technique ID'].values[0], execution_event['MITRE Technique Name'].values[0])
        
        print()

    # Requirement 3: Identify the Self-Duplication Event
    duplication_event = df[df['Process Path'].duplicated(keep=False)]

    if not duplication_event.empty:
        print("Self-Duplication Event:")
        print("Duplicate Location:", duplication_event['Process Path'].values[0])
        print("User:", duplication_event['User'].values[0])
        print()

if __name__ == "__main__":
    # Specify the path to your CSV file
    csv_filepath = "/Users/hvaandres/Documents/Git/hashencrypt/sysmon.csv"

    # Call the analysis function
    analyze_sysmon_csv(csv_filepath)
