import matplotlib.pyplot as plt
import numpy as np

ipc_a = []
l1i_mpki_a = []
l1d_mpki_a = []
l2_mpki_a = []
llc_mpki_a = []
itlb_mpki_a = []
dtlb_mpki_a = []

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
    return ipc, l1i_mpki, l1d_mpki, l2_mpki, llc_mpki, itlb_mpki, dtlb_mpki

parse_perf("./results/media_streaming_0-0.out")
parse_perf("./results/media_streaming_0-1.out")
parse_perf("./results/media_streaming_0-3.out")
parse_perf("./results/media_streaming_0-7.out")
parse_perf("./results/media_streaming_0-15.out")
# parse_perf("./results/media_streaming_16-16.out")
# parse_perf("./results/media_streaming_16-17.out")
# parse_perf("./results/media_streaming_16-19.out")
# parse_perf("./results/media_streaming_16-23.out")
print(ipc_a)
print(l1i_mpki_a)
print(l1d_mpki_a)
print(l2_mpki_a)
print(llc_mpki_a)
print(itlb_mpki_a)
print(dtlb_mpki_a)

font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 13}

Labels=['IPC', 'L1I', 'L1D', 'L2', 'LLC']
x_labels=['1', '2', '4', '8', '16']
x_pos=np.array([0, 0.5 , 1, 1.5, 2.0])


plt.rc('font', **font)
fig, axs = plt.subplots(5, 1, figsize=(7, 9))
plt_data = [ipc_a, l1i_mpki_a, l1d_mpki_a, l2_mpki_a, llc_mpki_a]
ylims = [[0.8,1.4], [5,8], [18,29], [4.5,8.5],[1,3]]
for i in range(5):
    if i == 0:
        axs[i].plot(x_pos+0.15, plt_data[i], linewidth=3, color = 'darkorange' , label=Labels[i])
        axs[i].plot(x_pos+0.15, plt_data[i], marker='x', markersize=11, color = 'orangered' , label=Labels[i])
    else:
        axs[i].plot(x_pos+0.15, plt_data[i], linewidth=2, color = 'navy' , label=Labels[i])
        axs[i].plot(x_pos+0.15, plt_data[i], marker='x', markersize=11, color = 'royalblue' , label=Labels[i])
    axs[i].set_xticks(x_pos+0.15, x_labels)
    if i == 4:
        axs[i].set_xlabel('Core Number', fontweight="bold")
    if i == 0:
        axs[i].set_ylabel('IPC', fontweight="bold")
    else:
        axs[i].set_ylabel(Labels[i] + ' MPKI', fontweight="bold")
    axs[i].set_ylim(ylims[i])
    axs[i].grid()

plt.subplots_adjust(top=0.971, bottom=0.079, left=0.121, right=0.972, hspace=0.4, wspace=0.2)
fig.savefig('Core_Scaling.eps', format='eps')
plt.show()

