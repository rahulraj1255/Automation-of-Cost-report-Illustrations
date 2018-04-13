#!/bin/bash
src=$1
suffix=m
destination=$2
format='.jpg'
count=3
count2=0
array=$(cat ${src}names.csv)
array2=($array)
current=none
while [[ !(-z $(eval "echo $"${count})) ]]
	do
	current=$(eval "echo $"$count)
	if [[ $(($(($count-3))%4)) -eq 0 ]]
		then
		mkdir $destination
		mkdir $destination/${array2[count2]}
		mv $src/$current $destination/${array2[count2]}/top${suffix}$format
		count=$(($count+1))
	
	elif [[ $(($(($count-3))%4)) -eq 1 ]]
		then
		mv $src/$current $destination/${array2[count2]}/front${suffix}$format
		count=$(($count+1))
	elif [[ $(($(($count-3))%4)) -eq 2 ]]
		then
		mv $src/$current $destination/${array2[count2]}/side${suffix}$format
		count=$(($count+1))
	elif [[ $(($(($count-3))%4)) -eq 3 ]]
		then
		mv $src/$current $destination/${array2[count2]}/iso${suffix}$format
		count=$(($count+1))
		count2=$(($count2+1))
	fi
done
