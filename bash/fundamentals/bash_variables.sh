#!/bin/bash

# the name of the bash script
echo $0

#the user currently running the script
echo $USER

#the current line number of the script
echo $LINENO

#the process id of the current script
echo $$

#print the first command argument, add one when running the script
#./bash_variables.sh billiam
echo $1

#an example of creating a custom variable
createdvariable=Exampleofcreatedcreatedvariable

echo $createdvariable