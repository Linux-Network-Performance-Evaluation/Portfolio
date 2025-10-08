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
        'data': """Packet Size	Ubuntu IPv6 TCP Average Delay	Ubuntu IPv6 UDP Average Delay	Fedora IPv6 TCP Average Delay	Fedora IPv6 UDP Average Delay	Kali IPv6 TCP Average Delay	Kali IPv6 UDP Average Delay
128	0.0004069	0.0000405	0.0005006	0.0001383	0.0005969	0.0001305
256	0.0004279	0.0001303	0.0005152	0.000163	0.0005508	0.0001651
384	0.0008508	0.0001676	0.0007442	0.0001101	0.0009236	0.0001929
512	0.0008026	0.0001982	0.0006828	0.0000657	0.000649	0.0001969
640	0.0008431	0.000248	0.000671	0.0000749	0.000839	0.0002199
768	0.0689433	0.0049348	0.0688691	0.0047572	0.0696282	0.0049292
896	0.078873	0.0057024	0.0744548	0.005532	0.0766718	0.0057063
1024	0.081427	0.0064242	0.0747777	0.0062883	0.0778551	0.0064381
1152	0.0799189	0.0072028	0.0737663	0.0071164	0.0754107	0.0072345
1280	0.0777853	0.0080841	0.0768856	0.0079735	0.0742953	0.0082635
1408	0.072229	0.0088678	0.0680818	0.0086958	0.0819091	0.0089074
1536	0.0578138	0.0071511	0.0680265	0.006978	0.0591323	0.0072446

""",
        'unit': 'ms',
        'y_range': (-0.01, 0.09)
    },
    'Jitter': {
        'data': """Packet Size	Ubuntu IPv6 TCP Jitter	Ubuntu IPv6 UDP  Jitter	Fedora IPv6 TCP Jitter	Fedora IPv6 UDP Jitter	Kali IPv6 TCP Jitter	Kali IPv6 UDP Jitter
128	0.0000985	0.000045	0.0000985	0.000046	0.000097	0.0000461
256	0.0000906	0.0000471	0.0000905	0.0000476	0.0000903	0.000047
384	0.0000887	0.0000443	0.0000873	0.0000434	0.0000883	0.0000443
512	0.0000864	0.000036	0.0000835	0.0000348	0.0000834	0.0000341
640	0.0000866	0.0000278	0.0000846	0.0000257	0.0000859	0.0000256
768	0.0001201	0.0002009	0.0001202	0.0002029	0.00012	0.0002013
896	0.0001409	0.0003895	0.0001409	0.0003914	0.0001409	0.0003911
1024	0.0001615	0.0005576	0.0001614	0.0005663	0.0001616	0.0005689
1152	0.0001819	0.0007263	0.0001823	0.0007158	0.0001822	0.0007296
1280	0.0002029	0.0008604	0.0002028	0.0008684	0.0002025	0.0008714
1408	0.0002228	0.0010005	0.0002235	0.0009959	0.0002236	0.0009917
1536	0.0002429	0.0008701	0.0002442	0.0009134	0.0002438	0.0009029

""",
        'unit': 'ms',
        'y_range': (-0.01, 0.09)
    },
    'Throughput': {
        'data': """Packet Size	Ubuntu IPv6 TCP Bitrate	Ubuntu IPv6 UDP Bitrate	Fedora IPv6 TCP Bitrate	Fedora IPv6 UDP Bitrate	Kali IPv6 TCP Bitrate	Kali IPv6 UDP Bitrate
128	17264.1327	17432.89961	17249.02424	17441.29725	17261.78322	17449.60437
256	34842.46211	34920.77153	34820.48713	34937.99939	34817.98518	34920.65891
384	52556.72056	52334.19474	52595.30784	52338.84739	52553.03333	52295.46418
512	70066.63153	69824.52761	70186.22856	69802.44935	70126.19083	69766.41877
640	87956.73591	87249.90529	88146.93726	87241.74742	88080.38277	87305.13495
768	93571.63416	91119.65752	93549.83061	91065.55229	93563.07573	91087.53875
896	93586.8715	92350.63363	93584.13296	92352.91526	93584.69672	92320.0093
1024	93639.61281	93257.08305	93662.78411	93287.46072	93629.48161	93239.20358
1152	93665.27714	93955.26164	93676.58196	93980.70515	93652.03828	94018.39185
1280	93636.82835	94563.85667	93688.44859	94633.3827	93688.7489	94569.70013
1408	93695.24101	95038.99887	93722.5765	95100.76984	93685.61888	95105.498
1536	93851.8148	91749.92721	93761.08089	91815.56597	93837.23922	91842.88404

""",
        'unit': 'bps',
        'y_range': (-0.01, 0.09)
    },
    'Packet Loss': {
        'data': """Packet Size	Ubuntu IPv6 TCP Packet Loss	Ubuntu IPv6 UDP Packet Loss	Fedora IPv6 TCP Packet Loss	Fedora IPv6 UDP Packet Loss	Kali IPv6 TCP Packet Loss	Kali IPv6 UDP Packet Loss
128	0	0.051	0	0.055	0	0.052
256	0	0.06	0	0.12	0	0.064
384	0	0.106	0	0.05	0	0.056
512	0	0.056	0	0.059	0	0.053
640	0	0.112	0	0.05	0	0.119
768	0	0.05	0	0.111	0	0.06
896	0	0.052	0	0.05	0	0.05
1024	0	0.084	0	0.045	0	0.093
1152	0	0.041	0	0.09	0	0.052
1280	0	0.04	0	0.042	0	0.038
1408	0	0.221	0	0.182	0	0.145
1536	0	0.042	0	0.057	0	0.033

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
    df_melted[['OS', 'Protocol_Info']] = df_melted['OS_Protocol'].str.split(' IPv6 ', expand=True)
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
    plt.title(f'Average {metric} (IPv6)', fontsize=16, fontweight='bold')
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
    filename = f"IPv6_Comparison_{metric}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved as {filename}")

# Loop through the datasets and generate a plot for each
for metric, details in datasets.items():
    plot_network_data(details['data'], metric, details['unit'])
