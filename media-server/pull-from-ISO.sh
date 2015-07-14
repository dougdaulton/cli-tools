#! /bin/bash

# -----------------------------------------------------
# Pull FIles From ISO
# -----------------------------------------------------

# From the BASH shell

# bash pull-from-ISO.sh ISO-key SOURCEDIR WRITEDIR


# Establish Variables
# -----------------------------------------------------
SOURCEDIR=$1
WRITEDIR=$2

# Read the Directory
# -----------------------------------------------------

arr=(~/$SOURCEDIR/*)

# iterate through array using a counter
for ((i=0; i<${#arr[@]}; i++)); do
    #do something to each element of array
    echo "${arr[$i]}"
done

# Remove Selected String
# -----------------------------------------------------

# Convert Case to CamelCase
# -----------------------------------------------------

# Cleanup Loose Ends
# -----------------------------------------------------