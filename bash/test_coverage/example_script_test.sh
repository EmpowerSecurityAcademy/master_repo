#!/bin/bash

script_path=${0%/*}

source "$script_path/example_script.sh"

testFavoriteNumberFAIL() 
{
  favorite_number
  assertTrue "This is the message if it fails" "[ $? -eq 5 ]"
}

testFavoriteNumberPASS() 
{
  favorite_number
  assertTrue "This is the message if it fails" "[ $? -eq 7 ]"
}

. shunit2