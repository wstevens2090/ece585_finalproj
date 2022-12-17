import matplotlib.pyplot as plt
import numpy as np

ipc_a = []
l1i_mpki_a = []
l1d_mpki_a = []
l2_mpki_a = []
llc_mpki_a = []
itlb_mpki_a = []
dtlb_mpki_a = []

cycles_k_p = []
insns_k_p = []
l1i_mpki_k_p = []
l1d_mpki_k_p = []
l2_mpki_k_p = []
llc_mpki_k_p = []
itlb_mpki_k_p = []
dtlb_mpki_k_p = []

def parse_perf(file_name):
    cycles_u = 0
    cycles_k = 0
    insn_u = 0
    insn_k = 0
    l1i_miss_u = 0
    l1i_miss_k = 0
    l1d_miss_u = 0
    l1d_miss_k = 0
    l2_miss_u = 0
    l2_miss_k = 0
    llc_miss_u = 0
    llc_miss_k = 0
    itlb_miss_u = 0
    itlb_miss_k = 0
    dtlb_miss_u = 0
    dtlb_miss_k = 0
    
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tokens = line.split()
            if "cpu" in line:
                num = int(tokens[0].replace(',', ''))
            else:
                continue
            if "cpu-cycles:u" in line:
                cycles_u = num
            elif "cpu-cycles:k" in line:
                cycles_k = num
            elif "instructions:u" in line:
                insn_u = num
            elif "instructions:k" in line:
                insn_k = num
            elif "r0280:u" in line:
                l1i_miss_u = num
            elif "r0280:k" in line:
                l1i_miss_k = num
            elif "r0151:u" in line:
                l1d_miss_u = num
            elif "r0151:k" in line:
                l1d_miss_k = num
            elif "r2724:u" in line:
                l2_miss_u = num
            elif "r2724:k" in line:
                l2_miss_k = num
            elif "cache-misses:u" in line:
                llc_miss_u = num
            elif "cache-misses:k" in line:
                llc_miss_k = num
            # for P cores
            elif "r0e11:u" in line:
                itlb_miss_u = num
            elif "r0e11:k" in line:
                itlb_miss_k = num
            elif "r0e12:u" in line:
                dtlb_miss_u = num
            elif "r0e12:k" in line:
                dtlb_miss_k = num
            # for E cores
            elif "r0e85:u" in line:
                itlb_miss_u = num
            elif "r0e85:k" in line:
                itlb_miss_k = num
            elif "r0e08:u" in line:
                dtlb_miss_u = num
            elif "r0e08:k" in line:
                dtlb_miss_k = num
    ipc = 1.0 * (insn_u + insn_k) / (cycles_u + cycles_k)
    ipc_a.append(ipc)
    l1i_mpki = 1000.0 * (l1i_miss_u + l1i_miss_k) / (insn_u + insn_k) 
    l1i_mpki_a.append(l1i_mpki)
    l1d_mpki = 1000.0 * (l1d_miss_u + l1d_miss_k) / (insn_u + insn_k)
    l1d_mpki_a.append(l1d_mpki)
    l2_mpki = 1000.0 * (l2_miss_u + l2_miss_k) / (insn_u + insn_k)
    l2_mpki_a.append(l2_mpki)
    llc_mpki = 1000.0 * (llc_miss_u + llc_miss_k) / (insn_u + insn_k)
    llc_mpki_a.append(llc_mpki)
    itlb_mpki = 1000.0 * (itlb_miss_u + itlb_miss_k) / (insn_u + insn_k)
    itlb_mpki_a.append(itlb_mpki)
    dtlb_mpki = 1000.0 * (dtlb_miss_u + dtlb_miss_k) / (insn_u + insn_k)
    dtlb_mpki_a.append(dtlb_mpki)

    cycles_k_p.append( 100.0 * (cycles_k) / (cycles_u + cycles_k) )
    insns_k_p.append( 100.0 * (insn_k) / (insn_u + insn_k) )
    l1i_mpki_k_p.append( 100.0 * (l1i_miss_k) / (l1i_miss_u + l1i_miss_k) )
    l1d_mpki_k_p.append( 100.0 * (l1d_miss_k) / (l1d_miss_u + l1d_miss_k) )
    l2_mpki_k_p.append( 100.0 * (l2_miss_k) / (l2_miss_u + l2_miss_k) )
    llc_mpki_k_p.append( 100.0 * (llc_miss_k) / (llc_miss_u + llc_miss_k) )
    itlb_mpki_k_p.append( 100.0 * (itlb_miss_k) / (itlb_miss_u + itlb_miss_k) )
    dtlb_mpki_k_p.append( 100.0 * (dtlb_miss_k) / (dtlb_miss_u + dtlb_miss_k) )
    return [cycles_k_p[-1], insns_k_p[-1], l1i_mpki_k_p[-1], l1d_mpki_k_p[-1], l2_mpki_k_p[-1], llc_mpki_k_p[-1], itlb_mpki_k_p[-1], dtlb_mpki_k_p[-1]]
    # return ipc, l1i_mpki, l1d_mpki, l2_mpki, llc_mpki, itlb_mpki, dtlb_mpki

plt_data = []
plt_data.append(parse_perf("../data_analytics/results/data_analytics_P.out"))
plt_data.append(parse_perf("../data_analytics/results/data_analytics_E.out"))
plt_data.append(parse_perf("../memory_analytics/results/memory_analytics_P.out"))
plt_data.append(parse_perf("../memory_analytics/results/memory_analytics_E.out"))
plt_data.append(parse_perf("./results/media_streaming_0-15.out"))
plt_data.append(parse_perf("./results/media_streaming_16-23.out"))
# print(ipc_a)
# print(l1i_mpki_a)
# print(l1d_mpki_a)
# print(l2_mpki_a)
# print(llc_mpki_a)
# print(itlb_mpki_a)
# print(dtlb_mpki_a)
print(cycles_k_p)
print(insns_k_p)
print(l1i_mpki_k_p)
print(l1d_mpki_k_p)
print(l2_mpki_k_p)
print(llc_mpki_k_p)
print(itlb_mpki_k_p)
print(dtlb_mpki_k_p)

font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 13}

Labels=['IPC', 'L1I', 'L1D', 'L2', 'LLC']
y_labels=['Cycles', 'Instructions', 'L1I Misses', 'L1D Misses', 'L2 Misses', 'LLC Misses', 'ITLB Misses', 'DTLB Misses']
y_pos=np.array([3.5, 3 , 2.5, 2.0, 1.5, 1.0, 0.5, 0.0])

# titles=['MapReduce on P-cores', 'MapReduce on E-cores', 'In-Memory Analytics on P-cores', 'In-Memory Analytics on E-cores', 'Media Streaming on P-cores', 'Media Streaming on E-cores']
titles=['P-cores', 'E-cores', 'P-cores', 'E-cores', 'P-cores', 'E-cores']

plt.rc('font', **font)
fig, axs = plt.subplots(3, 2, figsize=(7, 12))
# plt_data = [ipc_a, l1i_mpki_a, l1d_mpki_a, l2_mpki_a, llc_mpki_a]
# ylims = [[0.8,1.4], [5,8], [18,29], [4.5,8.5],[1,3]]

for i in range(3):
    for j in range(2):
        axs[i,j].barh(y_pos+0.15, np.array([100,100,100,100,100,100,100,100]), height=0.3, color = 'darkorange' , label='User')
        axs[i,j].barh(y_pos+0.15, plt_data[i*2+j], height=0.3, color = 'royalblue' , label='Kernel')
        # axs[i].plot(x_pos+0.15, plt_data[i], marker='x', markersize=11, color = 'royalblue' , label=Labels[i])
        if j == 0:
            axs[i,j].set_yticks(y_pos+0.15, y_labels)
        else:
            axs[i,j].set_yticks([])
        axs[i,j].set_xlabel('Kernel vs User Ratio', fontweight="bold")
        axs[i,j].set_xlim([0,100])
        axs[i,j].set_title(titles[i*2+j], fontsize=12)
        #axs[i,j].invert_yaxis()
        # axs[i].set_ylabel('IPC', fontweight="bold")
        # axs[i].set_ylabel(Labels[i] + ' MPKI', fontweight="bold")
        # axs[i].set_ylim(ylims[i])
        # axs[i].grid()
        handles1, labels1 = axs[i,j].get_legend_handles_labels()
# Add subtitle
fig.legend([handles1[1], handles1[0]], [labels1[1], labels1[0]], loc='upper right')
fig.text(0.58, 0.93, '(a) MapReduce', horizontalalignment='center', verticalalignment='center')
fig.text(0.58, 0.61, '(b) In-Memory Analytics', horizontalalignment='center', verticalalignment='center')
fig.text(0.58, 0.29, '(c) Media Streaming', horizontalalignment='center', verticalalignment='center')

# plt.subplots_adjust(top=0.971, bottom=0.079, left=0.121, right=0.972, hspace=0.4, wspace=0.2)
plt.subplots_adjust(top=0.9, bottom=0.059, left=0.224, right=0.945, hspace=0.55, wspace=0.2)
fig.savefig('Kernel_User.eps', format='eps')
plt.show()

