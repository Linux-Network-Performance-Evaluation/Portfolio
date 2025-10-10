import pandas as pd

file_path = "Ubuntu_Fedora_Sample_Graphing.xlsx"
df_raw = pd.read_excel(file_path, sheet_name="Data", header=None)

def restructure_data(df, os_name):
    records = []
    run = None
    i = 0
    while i < len(df):
        row = df.iloc[i].tolist()

        # Detect Run label
        if isinstance(row[0], str) and "Run" in row[0]:
            run = row[0].split()[-1]
            i += 1
            continue

        # Skip header rows
        if isinstance(row[0], str) and "Packet Size" in row[0]:
            i += 1
            continue

        # Only process rows with numeric packet size
        if pd.notna(row[0]) and str(row[0]).isdigit():
            packet_size = int(row[0])

            # IPv4: columns 1-8
            tcp_ipv4 = row[1:9:2]
            udp_ipv4 = row[2:9:2]
            records.append([os_name, run, "TCP", "IPv4", packet_size, *tcp_ipv4])
            records.append([os_name, run, "UDP", "IPv4", packet_size, *udp_ipv4])

            # IPv6: columns 11-18 (shifted after blank column 9-10)
            tcp_ipv6 = row[11:19:2]
            udp_ipv6 = row[12:19:2]
            records.append([os_name, run, "TCP", "IPv6", packet_size, *tcp_ipv6])
            records.append([os_name, run, "UDP", "IPv6", packet_size, *udp_ipv6])

        i += 1

    return pd.DataFrame(records, columns=[
        "OS", "Run", "Protocol", "Version", "Packet Size",
        "Delay", "Jitter", "Throughput", "Packet Loss"
    ])

# Process data
ubuntu_df = restructure_data(df_raw, "Ubuntu")
fedora_df = restructure_data(df_raw, "Fedora")

# Combine and save
clean_df = pd.concat([ubuntu_df, fedora_df], ignore_index=True)
with pd.ExcelWriter(file_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
    clean_df.to_excel(writer, sheet_name="Cleaned_Data", index=False)

print("✅ Cleaned data written to 'Cleaned_Data' sheet.")
