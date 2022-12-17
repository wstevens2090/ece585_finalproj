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

ipc_k_a = []
ipc_u_a = []
l1i_mpki_k_a = []
l1i_mpki_u_a = []
l1d_mpki_k_a = []
l1d_mpki_u_a = []
l2_mpki_k_a = []
l2_mpki_u_a = []
llc_mpki_k_a = []
llc_mpki_u_a = []
itlb_mpki_k_a = []
itlb_mpki_u_a = []
dtlb_mpki_k_a = []
dtlb_mpki_u_a = []

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
    insn_f = insn_u + insn_k
    ipc = 1.0 * (insn_u + insn_k) / (cycles_u + cycles_k)
    ipc_a.append(ipc)
    ipc_k_a.append( 1.0 * (insn_k) / (cycles_k) )
    ipc_u_a.append( 1.0 * (insn_u) / (cycles_u) )
    l1i_mpki = 1000.0 * (l1i_miss_u + l1i_miss_k) / (insn_u + insn_k) 
    l1i_mpki_a.append(l1i_mpki)
    # l1i_mpki_k_a.append( 1000.0 * (l1i_miss_k) / (insn_k) )
    # l1i_mpki_u_a.append( 1000.0 * (l1i_miss_u) / (insn_u) )
    l1i_mpki_k_a.append( 1000.0 * (l1i_miss_k) / (insn_f) )
    l1i_mpki_u_a.append( 1000.0 * (l1i_miss_u) / (insn_f) )
    l1d_mpki = 1000.0 * (l1d_miss_u + l1d_miss_k) / (insn_u + insn_k)
    l1d_mpki_a.append(l1d_mpki)
    # l1d_mpki_k_a.append( 1000.0 * (l1d_miss_k) / (insn_k) )
    # l1d_mpki_u_a.append( 1000.0 * (l1d_miss_u) / (insn_u) )
    l1d_mpki_k_a.append( 1000.0 * (l1d_miss_k) / (insn_f) )
    l1d_mpki_u_a.append( 1000.0 * (l1d_miss_u) / (insn_f) )
    l2_mpki = 1000.0 * (l2_miss_u + l2_miss_k) / (insn_u + insn_k)
    l2_mpki_a.append(l2_mpki)
    # l2_mpki_k_a.append( 1000.0 * (l2_miss_k) / (insn_k) )
    # l2_mpki_u_a.append( 1000.0 * (l2_miss_u) / (insn_u) )
    l2_mpki_k_a.append( 1000.0 * (l2_miss_k) / (insn_f) )
    l2_mpki_u_a.append( 1000.0 * (l2_miss_u) / (insn_f) )
    llc_mpki = 1000.0 * (llc_miss_u + llc_miss_k) / (insn_u + insn_k)
    llc_mpki_a.append(llc_mpki)
    # llc_mpki_k_a.append( 1000.0 * (llc_miss_k) / (insn_k) )
    # llc_mpki_u_a.append( 1000.0 * (llc_miss_u) / (insn_u) )
    llc_mpki_k_a.append( 1000.0 * (llc_miss_k) / (insn_f) )
    llc_mpki_u_a.append( 1000.0 * (llc_miss_u) / (insn_f) )
    itlb_mpki = 1000.0 * (itlb_miss_u + itlb_miss_k) / (insn_u + insn_k)
    itlb_mpki_a.append(itlb_mpki)
    # itlb_mpki_k_a.append( 1000.0 * (itlb_miss_k) / (insn_k) )
    # itlb_mpki_u_a.append( 1000.0 * (itlb_miss_u) / (insn_u) )
    itlb_mpki_k_a.append( 1000.0 * (itlb_miss_k) / (insn_f) )
    itlb_mpki_u_a.append( 1000.0 * (itlb_miss_u) / (insn_f) )
    dtlb_mpki = 1000.0 * (dtlb_miss_u + dtlb_miss_k) / (insn_u + insn_k)
    dtlb_mpki_a.append(dtlb_mpki)
    # dtlb_mpki_k_a.append( 1000.0 * (dtlb_miss_k) / (insn_k) )
    # dtlb_mpki_u_a.append( 1000.0 * (dtlb_miss_u) / (insn_u) )
    dtlb_mpki_k_a.append( 1000.0 * (dtlb_miss_k) / (insn_f) )
    dtlb_mpki_u_a.append( 1000.0 * (dtlb_miss_u) / (insn_f) )


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

# plt_data = []
# plt_data.append(parse_perf("../data_analytics/results/data_analytics_P.out"))
# plt_data.append(parse_perf("../data_analytics/results/data_analytics_E.out"))
# plt_data.append(parse_perf("../memory_analytics/results/memory_analytics_P.out"))
# plt_data.append(parse_perf("../memory_analytics/results/memory_analytics_E.out"))
# plt_data.append(parse_perf("./results/media_streaming_0-15.out"))
# plt_data.append(parse_perf("./results/media_streaming_16-23.out"))
parse_perf("./results/media_streaming_0-15.out")
parse_perf("./results_pinned_kernel/media_streaming_0-15.out")
parse_perf("./results_pinned_kernel_E/media_streaming_0-15.out")
# parse_perf("./results/media_streaming_pinned_0-15.out")
parse_perf("./results/media_streaming_16-23.out")
parse_perf("./results_pinned_kernel/media_streaming_16-23.out")
parse_perf("./results_pinned_kernel_E/media_streaming_16-23.out")
# parse_perf("./results/media_streaming_pinned_16-23.out")
print(ipc_a, ipc_k_a, ipc_u_a)
print(l1i_mpki_a, l1i_mpki_k_a, l1i_mpki_u_a)
print(l1d_mpki_a, l1d_mpki_k_a, l1d_mpki_u_a)
print(l2_mpki_a, l2_mpki_k_a, l2_mpki_u_a)
print(llc_mpki_a, llc_mpki_k_a, llc_mpki_u_a)
print(itlb_mpki_a, itlb_mpki_k_a, itlb_mpki_u_a)
print(dtlb_mpki_a, dtlb_mpki_k_a, dtlb_mpki_u_a)
# print(cycles_k_p)
# print(insns_k_p)
# print(l1i_mpki_k_p)
# print(l1d_mpki_k_p)
# print(l2_mpki_k_p)
# print(llc_mpki_k_p)
# print(itlb_mpki_k_p)
# print(dtlb_mpki_k_p)

font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 13}

Labels=['IPC', 'L1I MPKI', 'L1D MPKI', 'ITLB MPKI', 'DTLB MPKI']
# y_labels=['Cycles', 'Instructions', 'L1I Misses', 'L1D Misses', 'L2 Misses', 'LLC Misses', 'ITLB Misses', 'DTLB Misses']
# y_pos=np.array([3.5, 3 , 2.5, 2.0, 1.5, 1.0, 0.5, 0.0])
x_labels=['Full system', 'Kernel', 'User']
x_pos=np.array([0, 1.0, 2.0])

titles = ['Media Streaming Runs on P-cores', 'Media Streaming runs on E-cores']

plt.rc('font', **font)
fig, axs = plt.subplots(5, 2, figsize=(12, 11))
# plt_data = [ipc_a, l1i_mpki_a, l1d_mpki_a, l2_mpki_a, llc_mpki_a]
ylims = [[0,1.4], [0,30], [0,22], [0,1.1], [0,5]]

#             [l2_mpki_a[0], l2_mpki_k_a[0], l2_mpki_u_a[0]],\
#             [llc_mpki_a[0], llc_mpki_k_a[0], llc_mpki_u_a[0]],\
plt_data_0 = [[ipc_a[0], ipc_k_a[0], ipc_u_a[0]],\
            [l1i_mpki_a[0], l1i_mpki_k_a[0], l1i_mpki_u_a[0]],\
            [l1d_mpki_a[0], l1d_mpki_k_a[0], l1d_mpki_u_a[0]],\
            [itlb_mpki_a[0], itlb_mpki_k_a[0], itlb_mpki_u_a[0]],\
            [dtlb_mpki_a[0], dtlb_mpki_k_a[0], dtlb_mpki_u_a[0]]]
#             [l2_mpki_a[1], l2_mpki_k_a[1], l2_mpki_u_a[1]],\
#             [llc_mpki_a[1], llc_mpki_k_a[1], llc_mpki_u_a[1]],\
plt_data_1 = [[ipc_a[1], ipc_k_a[1], ipc_u_a[1]],\
            [l1i_mpki_a[1], l1i_mpki_k_a[1], l1i_mpki_u_a[1]],\
            [l1d_mpki_a[1], l1d_mpki_k_a[1], l1d_mpki_u_a[1]],\
            [itlb_mpki_a[1], itlb_mpki_k_a[1], itlb_mpki_u_a[1]],\
            [dtlb_mpki_a[1], dtlb_mpki_k_a[1], dtlb_mpki_u_a[1]]]
plt_data_2 = [[ipc_a[2], ipc_k_a[2], ipc_u_a[2]],\
            [l1i_mpki_a[2], l1i_mpki_k_a[2], l1i_mpki_u_a[2]],\
            [l1d_mpki_a[2], l1d_mpki_k_a[2], l1d_mpki_u_a[2]],\
            [itlb_mpki_a[2], itlb_mpki_k_a[2], itlb_mpki_u_a[2]],\
            [dtlb_mpki_a[2], dtlb_mpki_k_a[2], dtlb_mpki_u_a[2]]]
plt_data_3 = [[ipc_a[3], ipc_k_a[3], ipc_u_a[3]],\
            [l1i_mpki_a[3], l1i_mpki_k_a[3], l1i_mpki_u_a[3]],\
            [l1d_mpki_a[3], l1d_mpki_k_a[3], l1d_mpki_u_a[3]],\
            [itlb_mpki_a[3], itlb_mpki_k_a[3], itlb_mpki_u_a[3]],\
            [dtlb_mpki_a[3], dtlb_mpki_k_a[3], dtlb_mpki_u_a[3]]]
plt_data_4 = [[ipc_a[4], ipc_k_a[4], ipc_u_a[4]],\
            [l1i_mpki_a[4], l1i_mpki_k_a[4], l1i_mpki_u_a[4]],\
            [l1d_mpki_a[4], l1d_mpki_k_a[4], l1d_mpki_u_a[4]],\
            [itlb_mpki_a[4], itlb_mpki_k_a[4], itlb_mpki_u_a[4]],\
            [dtlb_mpki_a[4], dtlb_mpki_k_a[4], dtlb_mpki_u_a[4]]]
plt_data_5 = [[ipc_a[5], ipc_k_a[5], ipc_u_a[5]],\
            [l1i_mpki_a[5], l1i_mpki_k_a[5], l1i_mpki_u_a[5]],\
            [l1d_mpki_a[5], l1d_mpki_k_a[5], l1d_mpki_u_a[5]],\
            [itlb_mpki_a[5], itlb_mpki_k_a[5], itlb_mpki_u_a[5]],\
            [dtlb_mpki_a[5], dtlb_mpki_k_a[5], dtlb_mpki_u_a[5]]]
for i in range(5):
    for j in range(2):
        if j == 0:
            axs[i,j].bar(x_pos+0.1, plt_data_0[i], width=0.2, color = 'slateblue' , label='No Kernel Pinned')
            axs[i,j].bar(x_pos+0.3, plt_data_1[i], width=0.2, color = 'orangered' , label='Kernel Pinned to Single P-core')
            axs[i,j].bar(x_pos+0.5, plt_data_2[i], width=0.2, color = 'darkorange' , label='Kernel Pinned to Single E-core')
        else:
            axs[i,j].bar(x_pos+0.1, plt_data_3[i], width=0.2, color = 'slateblue' , label='No Kernel Pinned')
            axs[i,j].bar(x_pos+0.3, plt_data_4[i], width=0.2, color = 'orangered' , label='Kernel Pinned to Single P-core')
            axs[i,j].bar(x_pos+0.5, plt_data_5[i], width=0.2, color = 'darkorange' , label='Kernel Pinned to Single E-core')
        if i == 0:
            axs[i,j].set_title(titles[j], fontsize=15, fontweight="bold")
        axs[i,j].set_xticks(x_pos+0.3, x_labels)
        if j == 0:
            axs[i,j].set_ylabel(Labels[i], fontweight="bold")
        # axs[i].plot(x_pos+0.15, plt_data[i], marker='x', markersize=11, color = 'royalblue' , label=Labels[i])
        # if j == 0:
        #     axs[i].set_yticks(y_pos+0.15, y_labels)
        # else:
        #     axs[i].set_yticks([])
        # axs[i].set_xlabel('Kernel vs User Ratio', fontweight="bold")
        # axs[i].set_xlim([0,100])
        #axs[i,j].invert_yaxis()
        # axs[i].set_ylabel('IPC', fontweight="bold")
        # axs[i].set_ylabel(Labels[i] + ' MPKI', fontweight="bold")
        axs[i,j].set_ylim(ylims[i])
        # if i == 0 or i == 1 or i == 2:
        #     axs[i,j].set_ylim(ylims[i])
        # if i == 1 and j == 0:
        #     axs[i,j].set_ylim([0, 30])
        # axs[i].grid()
        handles1, labels1 = axs[i,j].get_legend_handles_labels()
fig.legend(handles1, labels1, loc='upper right')
# fig.text(0.58, 0.93, '(a) MapReduce', horizontalalignment='center', verticalalignment='center')
# fig.text(0.58, 0.61, '(b) In-Memory Analytics', horizontalalignment='center', verticalalignment='center')
# fig.text(0.58, 0.29, '(c) Media Streaming', horizontalalignment='center', verticalalignment='center')

plt.subplots_adjust(top=0.880, bottom=0.043, left=0.071, right=0.984, hspace=0.342, wspace=0.119)
fig.savefig('Pinned_Kernel.eps', format='eps')
plt.show()

