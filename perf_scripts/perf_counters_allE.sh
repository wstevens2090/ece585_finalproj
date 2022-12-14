# Usage: bash perf_counters_allP.sh [output_file] [observation_period]

for i in {16..23}
do 
    filename="$1"_"$i".out
    bash ../perf_scripts/perf_counters_1E.sh $filename $2 $i & 
done    