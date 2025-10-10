import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.lines import Line2D
import numpy as np

# A dictionary containing all the datasets. This makes the code scalable.
# Add new datasets here to generate more plots.
datasets = {
    'Delay': {
        'data': """Packet Size	Ubuntu IPv4 TCP Average Delay	Ubuntu IPv4 UDP Average Delay	Fedora IPv4 TCP Average Delay	Fedora IPv4 UDP Average Delay	Kali IPv4 TCP Average Delay	Kali IPv4 UDP Average Delay
128	0.0004279	0.00012	0.0004843	0.0001502	0.000519	0.0003945
256	0.0003962	0.0001304	0.0004364	0.0001836	0.0005151	0.000434
384	0.000847	0.0001403	0.0006376	0.0002775	0.0008891	0.0004394
512	0.0008598	0.000162	0.0005569	0.0002818	0.0009368	0.0004178
640	0.0009574	0.0001958	0.0005897	0.0003092	0.0010509	0.0004103
768	0.0720054	0.0049898	0.0740079	0.0050122	0.0717309	0.0050906
896	0.0766048	0.0057942	0.0739809	0.005805	0.0764994	0.0058662
1024	0.0746885	0.0063401	0.075339	0.0065336	0.0754016	0.0065946
1152	0.0806537	0.0070989	0.0761423	0.0071592	0.0784022	0.007348
1280	0.0704087	0.0081159	0.0773127	0.0080892	0.0744448	0.0083416
1408	0.0587484	0.0097223	0.0646749	0.0088167	0.0753321	0.0090388
1536	0.063501	0.0070705	0.0606886	0.0071181	0.068224	0.007302

""",
        'unit': 'ms',
        'y_range': (-0.01, 0.09)
    },
    'Jitter': {
        'data': """Packet Size	Ubuntu IPv4 TCP Jitter	Ubuntu IPv4 UDP Jitter	Fedora IPv4 TCP Jitter	Fedora IPv4 UDP Jitter	Kali IPv4 TCP Jitter	Kali IPv4 UDP Jitter
128	0.0000989	0.000047	0.0000988	0.0000469	0.0000985	0.0000463
256	0.0000905	0.0000471	0.0000904	0.000048	0.0000904	0.0000471
384	0.0000888	0.0000445	0.000087	0.0000433	0.0000878	0.0000446
512	0.0000864	0.0000365	0.0000838	0.0000345	0.0000854	0.0000347
640	0.0000869	0.0000277	0.0000848	0.0000257	0.0000863	0.0000251
768	0.00012	0.0002012	0.0001202	0.0002023	0.00012	0.000197
896	0.000141	0.0003937	0.000141	0.0003925	0.000141	0.0003916
1024	0.0001614	0.0005695	0.0001614	0.000574	0.0001615	0.0005695
1152	0.0001821	0.0007269	0.0001823	0.0007304	0.0001819	0.0007188
1280	0.0002025	0.000874	0.0002029	0.0008782	0.0002026	0.0008546
1408	0.0002234	0.0008382	0.0002236	0.0009996	0.0002237	0.0009943
1536	0.0002436	0.0009084	0.000244	0.0008972	0.0002444	0.0009116

""",
        'unit': 'ms',
        'y_range': (-0.01, 0.09)
    },
    'Throughput': {
        'data': """Packet Size	Ubuntu IPv4 TCP Bitrate	Ubuntu IPv4 UDP Bitrate	Fedora IPv4 TCP Bitrate	Fedora IPv4 UDP Bitrate	Kali IPv4 TCP Bitrate	Kali IPv4 UDP Bitrate
128	17261.85375	17471.90733	17247.45147	17417.31811	17245.82019	17456.93369
256	34747.96166	34940.13057	34816.86325	34917.24538	34804.32201	34942.6202
384	52560.3103	52335.95658	52670.85744	52378.96891	52601.00545	52154.57784
512	70081.83456	69851.08409	70046.29008	69810.5335	70083.51445	69797.02097
640	87960.00087	87352.85481	88086.86284	87271.32898	87896.87748	86995.93184
768	93570.53623	91024.66865	93563.80764	91072.75214	93581.59069	91091.66166
896	93587.57355	92351.43959	93583.91135	92343.76106	93572.37368	92280.24861
1024	93636.58398	93285.36198	93629.40534	93237.29453	93631.19046	93294.21305
1152	93657.3293	93933.80182	93630.95965	93982.17507	93644.15076	93997.2325
1280	93708.65022	94637.98039	93711.47111	94554.32552	93654.46107	94659.67336
1408	93734.54915	95113.14574	93698.79948	95104.2897	93704.91176	95043.68891
1536	93719.98697	91822.65242	93772.85034	91758.07362	93745.51959	91834.75422

""",
        'unit': 'bps',
        'y_range': (-0.01, 0.09)
    },
    'Packet Loss': {
        'data': """Packet Size	Ubuntu IPv4 TCP Packet Loss	Ubuntu IPv4 UDP Packet Loss	Fedora IPv4 TCP Packet Loss	Fedora IPv4 UDP Packet Loss	Kali IPv4 TCP Packet Loss	Kali IPv4 UDP Packet Loss
128	0	0.099	0	0.095	0	0.09
256	0	0.055	0	0.06	0	0.06
384	0	0.055	0	0.06	0	0.06
512	0	0.12	0	0.108	0	0.108
640	0	0.06	0	0.06	0	0.052
768	0	0.121	0	0.106	0	0.05
896	0	0.051	0	0.066	0	0.1
1024	0	0.046	0	0.089	0	0.047
1152	0	0.081	0	0.092	0	0.083
1280	0	0.04	0	0.054	0	0.019
1408	0	0.555	0	0.18	0	0.217
1536	0	0.032	0	0.035	0	0.029

""",
        'unit': '%',
        'y_range': (-0.01, 0.09)
    }
}

def plot_network_data(data_str, metric, unit):
    """
    Processes the raw data string and generates a line plot for the specified metric.

    Args:
        data_str (str): The raw data in a string format.
        metric (str): The name of the metric (e.g., 'Delay', 'Jitter').
        unit (str): The unit for the y-axis (e.g., 's', 'ms', '%').
    """
    # Read the data into a DataFrame
    df = pd.read_csv(io.StringIO(data_str), sep='\t', skipinitialspace=True)
    
    # Melt the DataFrame to a long format for easier plotting with seaborn
    df_melted = df.melt(id_vars='Packet Size', var_name='OS_Protocol', value_name=f'Average {metric}')

    # Split the 'OS_Protocol' column to create 'OS' and 'Protocol' columns
    df_melted[['OS', 'Protocol_Info']] = df_melted['OS_Protocol'].str.split(' IPv4 ', expand=True)
    df_melted['Protocol'] = df_melted['Protocol_Info'].str.split(' ', expand=True)[0]
    df_melted.drop(columns=['OS_Protocol', 'Protocol_Info'], inplace=True)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Use a more distinct color palette
    colors = {'Ubuntu': '#FF5733', 'Fedora': '#029C1E', 'Kali': "#3369FF"}  # Orange, Green, Blue
    
    # Define unique markers for each OS
    os_markers = {'Ubuntu': 'o', 'Fedora': 's', 'Kali': '^'}  # Circle, Square, Triangle
    
    # Define line styles for protocols
    protocol_styles = {'TCP': '-', 'UDP': '--'}  # Solid for TCP, Dashed for UDP
    
    # Plot each OS and protocol combination
    labeled_os = set()  # Track which OS we've already labeled
    
    for os_name in ['Ubuntu', 'Fedora', 'Kali']:
        for protocol in ['TCP', 'UDP']:
            # Filter data for this OS and protocol
            subset = df_melted[(df_melted['OS'] == os_name) & (df_melted['Protocol'] == protocol)]
            
            if not subset.empty:
                # Only label the first occurrence of each OS
                label = os_name if os_name not in labeled_os else ""
                if os_name not in labeled_os:
                    labeled_os.add(os_name)
                
                plt.plot(
                    subset['Packet Size'], 
                    subset[f'Average {metric}'],
                    marker=os_markers[os_name],
                    linestyle=protocol_styles[protocol],
                    linewidth=2.5,
                    markersize=8,
                    color=colors[os_name],
                    label=label
                )
    
    # Set plot titles and labels
    plt.title(f'Average {metric} (IPv4)', fontsize=16, fontweight='bold')
    plt.xlabel('Packet Size (bytes)', fontsize=12)
    plt.ylabel(f'Average {metric} ({unit})', fontsize=12)
    
    # Set x-axis ticks to show all packet sizes
    plt.xticks(df['Packet Size'].unique())

    # Dynamically determine y-axis ticks and limits
    y_min = df_melted[f'Average {metric}'].min()
    y_max = df_melted[f'Average {metric}'].max()
    
    # Add a small buffer to the y-axis limits
    y_buffer = (y_max - y_min) * 0.1
    plt.ylim(y_min - y_buffer, y_max + y_buffer)
    
    # Improve the y-axis tick formatting
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.4f'))

    # Improve grid appearance
    plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Create custom legend with line style explanations
    # Get the automatic legend
    legend1 = plt.legend(title='Operating Systems', 
                        frameon=True, 
                        fancybox=True, 
                        shadow=True, 
                        loc='upper left')
    
    # Add legend for line styles
    line_style_elements = [
        Line2D([0], [0], color='black', linestyle='-', linewidth=2, label='TCP (Solid Line)'),
        Line2D([0], [0], color='black', linestyle='--', linewidth=2, label='UDP (Dashed Line)')
    ]
    
    legend2 = plt.legend(handles=line_style_elements, 
                        title='Protocol Line Styles',
                        frameon=True, 
                        fancybox=True, 
                        shadow=True, 
                        bbox_to_anchor=(0.18, 0.85))
    
    # Add the first legend back (matplotlib removes it when creating the second)
    plt.gca().add_artist(legend1)
    
    plt.tight_layout()
    
    # Save the plot with a descriptive filename and higher DPI for better quality
    filename = f"IPv4_Comparison_{metric}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved as {filename}")

# Loop through the datasets and generate a plot for each
for metric, details in datasets.items():
    plot_network_data(details['data'], metric, details['unit'])
