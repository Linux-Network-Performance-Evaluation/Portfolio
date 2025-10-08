import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.lines import Line2D
import numpy as np

# IPv4 datasets
ipv4_datasets = {
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
        'y_range': None
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
        'y_range': None
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
        'y_range': None
    }
}

# IPv6 datasets
ipv6_datasets = {
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
        'y_range': None
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
        'y_range': None
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
        'y_range': None
    }
}

def plot_comparison_data(ipv4_data_str, ipv6_data_str, metric, unit, y_range=None):
    """
    Processes the raw IPv4 and IPv6 data strings and generates a comparison line plot.

    Args:
        ipv4_data_str (str): The IPv4 raw data in a string format.
        ipv6_data_str (str): The IPv6 raw data in a string format.
        metric (str): The name of the metric (e.g., 'Delay', 'Jitter').
        unit (str): The unit for the y-axis (e.g., 's', 'ms', '%').
        y_range (tuple): Optional tuple of (y_min, y_max) for fixed y-axis scaling.
    """
    # Read IPv4 data
    df_ipv4 = pd.read_csv(io.StringIO(ipv4_data_str), sep='\t', skipinitialspace=True)
    df_ipv4_melted = df_ipv4.melt(id_vars='Packet Size', var_name='OS_Protocol', value_name=f'Average {metric}')
    df_ipv4_melted[['OS', 'Protocol_Info']] = df_ipv4_melted['OS_Protocol'].str.split(' IPv4 ', expand=True)
    df_ipv4_melted['Protocol'] = df_ipv4_melted['Protocol_Info'].str.split(' ', expand=True)[0]
    df_ipv4_melted['IP_Version'] = 'IPv4'
    df_ipv4_melted.drop(columns=['OS_Protocol', 'Protocol_Info'], inplace=True)
    
    # Read IPv6 data
    df_ipv6 = pd.read_csv(io.StringIO(ipv6_data_str), sep='\t', skipinitialspace=True)
    df_ipv6_melted = df_ipv6.melt(id_vars='Packet Size', var_name='OS_Protocol', value_name=f'Average {metric}')
    df_ipv6_melted[['OS', 'Protocol_Info']] = df_ipv6_melted['OS_Protocol'].str.split(' IPv6 ', expand=True)
    df_ipv6_melted['Protocol'] = df_ipv6_melted['Protocol_Info'].str.split(' ', expand=True)[0]
    df_ipv6_melted['IP_Version'] = 'IPv6'
    df_ipv6_melted.drop(columns=['OS_Protocol', 'Protocol_Info'], inplace=True)
    
    # Combine both datasets
    df_combined = pd.concat([df_ipv4_melted, df_ipv6_melted], ignore_index=True)
    
    # Create the plot
    plt.figure(figsize=(14, 10))
    
    # Color palette for OS with different shades for IPv4 and IPv6
    ipv4_colors = {'Ubuntu': '#FF5733', 'Fedora': '#029C1E', 'Kali': "#3369FF"}  # Darker shades
    ipv6_colors = {'Ubuntu': '#FF8A65', 'Fedora': '#4CAF50', 'Kali': "#64B5F6"}  # Lighter shades
    
    # Markers for IP versions - filled for IPv4, hollow for IPv6
    ipv4_markers = {'Ubuntu': 'o', 'Fedora': 's', 'Kali': '^'}  # Filled: Circle, Square, Triangle
    ipv6_markers = {'Ubuntu': 'o', 'Fedora': 's', 'Kali': '^'}  # Same shapes but will be hollow
    
    # Line styles for protocols
    protocol_styles = {'TCP': '-', 'UDP': '--'}  # Solid for TCP, Dashed for UDP
    
    # Plot each combination
    labeled_combinations = set()  # Track what we've labeled for the legend
    
    for ip_version in ['IPv4', 'IPv6']:
        for os_name in ['Ubuntu', 'Fedora', 'Kali']:
            for protocol in ['TCP', 'UDP']:
                # Filter data for this combination
                subset = df_combined[
                    (df_combined['IP_Version'] == ip_version) & 
                    (df_combined['OS'] == os_name) & 
                    (df_combined['Protocol'] == protocol)
                ]
                
                if not subset.empty:
                    # Create label for legend (only for first occurrence of each OS)
                    if ip_version == 'IPv4' and protocol == 'TCP' and os_name not in labeled_combinations:
                        label = os_name
                        labeled_combinations.add(os_name)
                    else:
                        label = ""
                    
                    # Set marker properties and colors
                    if ip_version == 'IPv4':
                        marker = ipv4_markers[os_name]
                        fillstyle = 'full'
                        alpha = 0.8
                        color = ipv4_colors[os_name]
                    else:  # IPv6
                        marker = ipv6_markers[os_name]
                        fillstyle = 'none'
                        alpha = 0.7
                        color = ipv6_colors[os_name]
                    
                    plt.plot(
                        subset['Packet Size'], 
                        subset[f'Average {metric}'],
                        marker=marker,
                        fillstyle=fillstyle,
                        linestyle=protocol_styles[protocol],
                        linewidth=2.5,
                        markersize=8,
                        markeredgewidth=2,
                        color=color,
                        alpha=alpha,
                        label=label
                    )
    
    # Set plot titles and labels
    plt.title(f'IPv4 vs IPv6 Comparison: Average {metric}', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Packet Size (bytes)', fontsize=14, fontweight='bold')
    plt.ylabel(f'Average {metric} ({unit})', fontsize=14, fontweight='bold')
    
    # Set x-axis ticks to show all packet sizes
    plt.xticks(df_ipv4['Packet Size'].unique(), rotation=45)
    
    # Set y-axis limits
    if y_range:
        plt.ylim(y_range[0], y_range[1])
    else:
        # Dynamically determine y-axis ticks and limits
        y_min = df_combined[f'Average {metric}'].min()
        y_max = df_combined[f'Average {metric}'].max()
        
        # Add a small buffer to the y-axis limits
        y_buffer = (y_max - y_min) * 0.1 if y_max != y_min else 0.1
        plt.ylim(y_min - y_buffer, y_max + y_buffer)
    
    # Improve the y-axis tick formatting
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
    
    # Improve grid appearance
    plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Create comprehensive legend
    # Legend 1: Operating Systems
    legend1 = plt.legend(title='Operating Systems', 
                        frameon=True, 
                        fancybox=True, 
                        shadow=True, 
                        loc='upper left',
                        fontsize=10,
                        title_fontsize=12)
    
    # Legend 2: Protocol Line Styles
    protocol_elements = [
        Line2D([0], [0], color='black', linestyle='-', linewidth=2, label='TCP (Solid Line)'),
        Line2D([0], [0], color='black', linestyle='--', linewidth=2, label='UDP (Dashed Line)')
    ]
    
    legend2 = plt.legend(handles=protocol_elements, 
                        title='Protocol Line Styles',
                        frameon=True, 
                        fancybox=True, 
                        shadow=True, 
                        bbox_to_anchor=(0.15, 0.883),
                        fontsize=10,
                        title_fontsize=12)
    
    # Legend 3: IP Version Markers
    ip_version_elements = [
        Line2D([0], [0], color='black', marker='o', fillstyle='full', 
               linestyle='None', markersize=8, markeredgewidth=2, label='IPv4 (Filled Markers)'),
        Line2D([0], [0], color='black', marker='o', fillstyle='none', 
               linestyle='None', markersize=8, markeredgewidth=2, label='IPv6 (Hollow Markers)')
    ]
    
    legend3 = plt.legend(handles=ip_version_elements, 
                        title='IP Version Markers',
                        frameon=True, 
                        fancybox=True, 
                        shadow=True, 
                        bbox_to_anchor=(0.167, 0.79),
                        fontsize=10,
                        title_fontsize=12)
    
    # Add the first two legends back (matplotlib removes them when creating subsequent ones)
    plt.gca().add_artist(legend1)
    plt.gca().add_artist(legend2)
    
    plt.tight_layout()
    
    # Save the plot with a descriptive filename and higher DPI for better quality
    filename = f"Comparison_IPv4_vs_IPv6_{metric}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Comparison plot saved as {filename}")
    
    # Close the plot to free memory
    plt.close()

# Generate comparison plots for all metrics
def generate_all_comparisons():
    """Generate comparison plots for all metrics (Delay, Jitter, Throughput, Packet Loss)"""
    print("Generating IPv4 vs IPv6 comparison plots...")
    
    for metric in ['Delay', 'Jitter', 'Throughput', 'Packet Loss']:
        print(f"\nGenerating {metric} comparison plot...")
        plot_comparison_data(
            ipv4_datasets[metric]['data'], 
            ipv6_datasets[metric]['data'], 
            metric, 
            ipv4_datasets[metric]['unit'],
            ipv4_datasets[metric]['y_range']
        )
    
    print("\nAll comparison plots have been generated successfully!")

# Run the comparison generation
if __name__ == "__main__":
    generate_all_comparisons()