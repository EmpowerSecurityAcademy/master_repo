#!/bin/bash

#simple while loop
count=1
while [[ $counter -le 10 ]]
do
	echo $counter
	((counter++))
done

#simple for loop
fruits='apple orange grapefruit'
for fruit in $fruits
do
	echo $fruit
done

