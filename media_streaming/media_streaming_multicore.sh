# Usage: bash data_analytics_P_pinned.sh [max_cpu]
# runs 1 master and 3 slaves on cpus [0, max_cpu]

# config variables
waittime=60
runtime=60
num_clients=15

# cpulist = 0-max_cpu
cpulist="0-${1}"

# create hadoop network
docker network create streaming_network

# pins master, 3 slaves to cpus on $cpulist
docker run -d --cpuset-cpus 0-${1} --rm --name streaming_server --volumes-from streaming_dataset --net streaming_network cloudsuite3/media-streaming:server
for i in $( seq 1 $num_clients )
do 
    name=streaming_client_"$i"
    logfile="./results/client_${i}_results"
    docker run -t --cpuset-cpus 0-${1} --rm --name=$name -v $logfile --volumes-from streaming_dataset --net streaming_network cloudsuite3/media-streaming:client streaming_server &
done    

# runs benchmark
# docker exec master benchmark & 

# waits for $waittime for benchmark to set-up
sleep $waittime

# records activity on cpus [0, max_cpu] for $runtime seconds
filename="./results/media_streaming_0-${1}.out"
bash ../perf_scripts/perf_counters_1P.sh $filename $runtime ${cpulist} &
for i in $( seq 0 $1 )
do
    filename="./results/media_streaming_P_${cpulist}_${i}.out"
    bash ../perf_scripts/perf_counters_1P.sh $filename $runtime $i &
done

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
