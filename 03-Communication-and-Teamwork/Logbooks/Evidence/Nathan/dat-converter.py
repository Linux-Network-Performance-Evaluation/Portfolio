import os
import pandas as pd
import re
import numpy as np

def extract_data_v19(dat_file_path):
    """
    Reads a .dat file, skips the first line, and extracts the third column data.

    Args:
        dat_file_path (str): The full path to the .dat file.

    Returns:
        list: A list of the third column values as floats, or an empty list if no data.
    """
    data = []
    try:
        with open(dat_file_path, 'r') as file:
            next(file)  # Skip the first line
            for line in file:
                values = line.strip().split()
                if len(values) >= 3:
                    try:
                        data.append(float(values[2]))
                    except ValueError:
                        print(f"Warning: Non-numeric value in the third column of '{os.path.basename(dat_file_path)}': {values[2]}")
                elif values:
                    print(f"Warning: Line in '{os.path.basename(dat_file_path)}' has less than 3 columns: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found at {dat_file_path}")
    except StopIteration:
        print(f"Warning: '{os.path.basename(dat_file_path)}' is empty or has only one line and was skipped.")
    except Exception as e:
        print(f"An error occurred while processing '{os.path.basename(dat_file_path)}': {e}")
    return data

def process_folder_v19(folder_path, output_filename="combined_data_with_time.xlsx", export_folder="excel_output"):
    """
    Processes all .dat files in a folder, extracts the third column, and saves
    all data into a single Excel file with sheets grouped by protocol type and
    packet size, with run numbers as column headers ordered from 1 to 10,
    and a leading 'Time' column.

    Args:
        folder_path (str): The path to the folder containing the .dat files.
        output_filename (str, optional): The name of the output Excel file.
                                         Defaults to 'combined_data_with_time.xlsx'.
        export_folder (str, optional): The path to the folder where the Excel file will be saved.
                                       Defaults to 'excel_output' in the same directory.
    """
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    grouped_data = {}  # Dictionary to store data grouped by (protocol, packet_size)

    for filename in os.listdir(folder_path):
        if filename.endswith(".dat"):
            dat_file_path = os.path.join(folder_path, filename)
            data = extract_data_v19(dat_file_path)

            match = re.search(r'([a-z0-9]+)_([a-z]+)_(\d+)_(\d+)(?:\.log)?_([^_]+)\.dat$', filename, re.IGNORECASE)
            if match:
                protocol_type = match.group(1).lower()
                transport_protocol = match.group(2).lower()
                packet_size = int(match.group(3))
                run_number = int(match.group(4))

                group_key = (protocol_type.upper(), transport_protocol.upper(), packet_size)
                if group_key not in grouped_data:
                    grouped_data[group_key] = {}  # Initialize a dictionary for runs

                grouped_data[group_key][run_number] = data  # Store with integer key
            else:
                print(f"Warning: Could not extract information from filename: {filename}")

    # Write grouped data to a single Excel file with different sheets and ordered run numbers as headers, including the time column
    if grouped_data:
        output_path = os.path.join(export_folder, output_filename)
        try:
            with pd.ExcelWriter(output_path) as writer:
                for (proto_type, trans_proto, pkt_size), run_data in grouped_data.items():
                    sheet_name = f"{proto_type}_{trans_proto}_Size{pkt_size}"
                    # Sort the run numbers
                    sorted_runs = sorted(run_data.keys())
                    ordered_run_data = {f"Run {run}": run_data[run] for run in sorted_runs}

                    # Determine the maximum number of data points across all runs for this group
                    max_len = 0
                    for run_list in ordered_run_data.values():
                        max_len = max(max_len, len(run_list))

                    # Create the time column
                    time_column = np.arange(0, max_len * 0.1, 0.1)
                    if len(time_column) > max_len:
                        time_column = time_column[:max_len]
                    elif len(time_column) < max_len:
                        padding = np.full(max_len - len(time_column), np.nan) # Pad with NaN if runs have different lengths
                        time_column = np.concatenate([time_column, padding])

                    # Create the DataFrame
                    df = pd.DataFrame.from_dict(ordered_run_data, orient='index').transpose()
                    df.insert(0, 'Time', time_column) # Insert the time column at the beginning

                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"\nThird column data grouped by Protocol and Packet Size, with runs ordered as columns and a 'Time' column, exported to '{output_path}'.")
        except Exception as e:
            print(f"An error occurred while writing to the Excel file: {e}")
    else:
        print("\nNo valid data was found to export.")

# Example usage:
folder_path = 'C:\\Users\\GGPC\\OneDrive - AUT University\\2025\\R&D Project\\Shared\\Part 1\\04-Development-and-Quality-Assurance\\Ubuntu\\logs\\ipv4\\throughput\\tcp'  # Replace with the actual path to your folder

# --------------------------------------------------------------------------------------------------------------------- #
# NEED TO CHANGE THE FOLDER PATH TO YOUR OWN - PATH ABOVE TO WHERE THE .DAT FILES ARE LOCATED
# --------------------------------------------------------------------------------------------------------------------- #

export_path = 'C:\\Users\\GGPC\\OneDrive - AUT University\\2025\\R&D Project\\Shared\\Part 1\\04-Development-and-Quality-Assurance\\Ubuntu\\logs\\ipv4\\exports'  # Specify your desired export path
output_file = 'ThroughPut TCP.xlsx' # Specify the output filename
process_folder_v19(folder_path, output_file, export_path)