# Usage: bash perf_counters_P.sh [output_file] [observation_period]

#    cpu-cycles:u,cpu-cycles:k,\         # cycles for user/kernel
#    instructions:u,instructions:k,\     # instructions for user/kernel
#    r0280:u,r0280:k,\                   # L1I$ Misses for user/kernel
#    r0151:u,r0151:k,\                   # L1D$ Replacements for user/kernel
#    r2724:u,r2724:k,\                   # L2_RQSTS.ALL_DEMAND_MISS
#    cache-misses:u,cache-misses:k,\     # LLC misses
#    r412e:u,r412e:k,\                   # LONGEST_LAT_CACHE.MISS
#    r012a:u,r012a:k,\                   # offcore: OCR.DEMAND_DATA_RD.L3_MISS
#    r0e85:u,r0e85:k,\                   # ITLB_MISSES.WALK_COMPLETED
#    r0e08:u,r0e08:k,\                   # DTLB_LOAD_MISSES.WALK_COMPLETED

sudo perf stat \
    --cpu=16-23 \
    -e cpu-cycles:u,cpu-cycles:k,instructions:u,instructions:k,r0280:u,r0280:k,r0151:u,r0151:k,r2724:u,r2724:k,cache-misses:u,cache-misses:k,r0e85:u,r0e85:k,r0e08:u,r0e08:k \
    -o $1 sleep $2
#    -o $2 bash run_real_spec.sh $3 #runcpu -a run --config=kaifengx-qemu $3
