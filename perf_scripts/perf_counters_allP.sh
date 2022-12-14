# Usage: bash perf_counters_allP.sh [output_file] [observation_period]

for i in {0..15}
do 
    filename="$1"_"$i".out
    bash ../perf_scripts/perf_counters_1P.sh $filename $2 $i & 
done    