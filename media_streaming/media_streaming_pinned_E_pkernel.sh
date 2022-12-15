# Usage: bash media_streaming_multicore_E.sh [max_cpu]
# runs 1 server and 15 clients on cpus [16, max_cpu]

# config variables
waittime=60
runtime=60
num_clients=15

# cpulist = 0-max_cpu
cpulist="16-${1}"

# create hadoop network
docker network create streaming_network

# pins master, 3 slaves to cpus on $cpulist
docker run -d --cpuset-cpus 16 --rm --name streaming_server --volumes-from streaming_dataset --net streaming_network cloudsuite3/media-streaming:server
for i in $( seq 1 $num_clients )
do 
    name=streaming_client_"$i"
    logfile="./results/client_${i}_results"
    docker run -t --cpuset-cpus $((${i}/2+16)) --rm --name=$name -v $logfile --volumes-from streaming_dataset --net streaming_network cloudsuite3/media-streaming:client streaming_server &
done    

# runs benchmark
# docker exec master benchmark & 

# waits for $waittime for benchmark to set-up
sleep $waittime
sudo bash ../pin_kernel_scripts/pin_kernel.sh

# records activity on cpus [16, max_cpu] for $runtime seconds
filename="./results_pinned_kernel/media_streaming_pinned_16-${1}.out"
bash ../perf_scripts/perf_counters_1E.sh $filename $runtime ${cpulist} &
for i in $( seq 16 $1 )
do
    filename="./results_pinned_kernel/media_streaming_pinned_E_${cpulist}_${i}.out"
    bash ../perf_scripts/perf_counters_1E.sh $filename $runtime $i &
done
# Add another script for recording core 0
filename="./results_pinned_kernel/media_streaming_E_${cpulist}_0.out"
bash ../perf_scripts/perf_counters_1E.sh $filename $runtime 0 &

# waits $runtime seconds for performance counting
sleep $runtime

# stops/kills containers 
for i in $( seq 1 $num_clients )
do 
    name=streaming_client_"$i"
    docker stop $name
done
docker stop streaming_server

# destroys network 
docker network rm streaming_network
