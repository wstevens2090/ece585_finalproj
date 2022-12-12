perf stat 

sudo perf stat \
    --cpu= 0-15 \
    -e \
    cpu-cycles:u,cpu-cycles:k,\         # cycles for user/kernel
    instructions:u,instructions:k,\     # instructions for user/kernel
    r0280:u, r0280:k,\                  # L1I$ Misses for user/kernel
    r0151:u, r0151:k,\                  # L1D$ Replacements for user/kernel
    -o $2 bash run_real_spec.sh $3 #runcpu -a run --config=kaifengx-qemu $3