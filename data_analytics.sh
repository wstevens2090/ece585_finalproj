# Step 1: Set up test for data analytics.

# Step 2: Pin tasks to P cores. Run 1 master, 1 slave. 
taskset --cpu-list 0-15 docker run --rm -d --net hadoop-net --name master --hostname master cloudsuite3/data-analytics master
taskset --cpu-list 0-15 docker run --rm -d --net hadoop-net --name slave01 --hostname slave01 cloudsuite3/hadoop slave

# Step 3: Run Execute; sleep for 60s. 
docker exec master benchmark & 
sleep 60

# Step 4: Record counters for 60s. Run with & to prevent blocking. 
bash perf_counters_P.sh data_analytics.out