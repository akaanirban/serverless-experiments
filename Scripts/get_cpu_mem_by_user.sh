#!/bin/bash

while [ : ]
do
	#clear
	output=`top -b -n 1 -u "ggc_user" | awk 'NR>7 { cpu += $9; mem += $10; } END { if (cpu >= 0.0) print ",CPU:" cpu, ",MEMORY:" mem; }'`
	echo `date -u +"%Y-%m-%dT%H:%M:%SZ"` ", USER: ggc_user" $output
	sleep $1
done

