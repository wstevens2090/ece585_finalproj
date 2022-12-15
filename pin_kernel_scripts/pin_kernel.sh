# top > top_all.out
# Get username by PID
for pid in /proc/[0-9]*
do
    # echo ${pid:6}
    USERNAME="$( ps -o uname= -p "${pid:6}" )"
    if [[ "root" == "$USERNAME" ]]
    then
        # echo ${pid:6} 
	# pin to core 0
	sudo taskset -p 0x1 ${pid:6}
    fi
done

