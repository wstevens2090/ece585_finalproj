# Usage: bash data_analytics_P_pinned.sh [max_cpu]
# runs 1 master and 3 slaves on cpus [0, max_cpu]

# config variables
waittime=60
runtime=60
num_slaves=3

# cpulist = 0-max_cpu
# cpulist="0-${1}"

# create hadoop network
docker network create hadoop-net

# pins master, 3 slaves to cpus on $cpulist
docker run --rm --cpuset-cpus 0 -d --net hadoop-net --name master --hostname master cloudsuite3/data-analytics master
for i in $( seq 1 $num_slaves )
do 
    name=slave"$i"
    docker run --rm --cpuset-cpus $i -d --net hadoop-net --name $name --hostname $name cloudsuite3/hadoop slave
done    

# runs benchmark
docker exec master benchmark & 

# waits for $waittime for benchmark to set-up
sleep $waittime

# records activity on cpus [0, max_cpu] for $runtime seconds
filename="./results/data_analytics_P_pinned_per_core.out"
bash ../perf_scripts/perf_counters_1P.sh $filename $runtime 0-3 &
for i in $( seq 0 3 )
do
    filename="./results/data_analytics_P_pinned_per_core_${i}.out"
    bash ../perf_scripts/perf_counters_1P.sh $filename $runtime $i &
done

# waits $runtime seconds for performance counting
sleep $runtime

# stops/kills containers 
docker stop master
for i in $( seq 1 $num_slaves )
do 
    name=slave"$i"
    docker stop $name
done

# destroys network 
docker network rm hadoop-net