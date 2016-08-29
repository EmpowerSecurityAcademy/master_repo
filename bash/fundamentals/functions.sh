#!/bin/bash

simple_function() {
	echo $1
}

simple_function Edward
simple_function Anthony


favorite_number() {
	return $1
}

favorite_number 7
echo You can access the value returned by typing $?