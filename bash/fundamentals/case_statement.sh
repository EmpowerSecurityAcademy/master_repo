#!/bin/bash

case $1 in
	[0-3]*)
		echo Pretty small number
		;;
	[4-7]*)
		echo Getting a little bit larger
		;;
	[8-9]*)
		echo Huge fan of these numbers
		;;
	*)
		echo Now your just doing too much
		;;
esac