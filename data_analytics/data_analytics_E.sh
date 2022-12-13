# Step 1: Set up test for data analytics.


# Step 2: Pin tasks to P cores. Run 1 master, 1 slave. 
# docker run --rm -d --net hadoop-net --name master --hostname master cloudsuite3/data-analytics master
# docker run --rm -d --net hadoop-net --name slave01 --hostname slave01 cloudsuite3/hadoop slave

# Step 3: Run Execute; sleep for 60s. 
taskset --cpu-list 16-23 docker exec master benchmark & 
sleep 60

# Step 4: Record counters for 60s. Run with & to prevent blocking. 
bash ../perf_scripts/perf_counters_E.sh ./results/data_analytics_E.out 60