# Step 1: Set up test for data analytics.


# Step 2: Pin tasks to P cores. Run 1 master, 1 slave. 
docker run --rm --cpuset-cpus 0 -d --net hadoop-net --name master --hostname master cloudsuite3/data-analytics master

for i in {1..15}
do 
    name=slave"$i"
    docker run --rm --cpuset-cpus $i -d --net hadoop-net --name $name --hostname $name cloudsuite3/hadoop slave
done    

# Step 3: Run Execute; sleep for 60s. 
docker exec master benchmark & 
sleep 60

# Step 4: Record counters for 60s. Run with & to prevent blocking. 
bash ../perf_scripts/perf_counters_P.sh ./results/data_analytics_P.out 60 & 
bash ../perf_scripts/perf_counters_allP.sh ./results/data_analytics_P 60 &