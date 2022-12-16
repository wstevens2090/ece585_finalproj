# Get username by PID
for pid in /proc/[0-9]*
do
    # echo ${pid:6}
    USERNAME="$( ps -o uname= -p "${pid:6}" )"
    if [[ "root" == "$USERNAME" ]]
    then
        # echo ${pid:6} 
	# pin to core 16
	sudo taskset -p 0x10000 ${pid:6}
    fi
done

