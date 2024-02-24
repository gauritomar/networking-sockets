#!/bin/bash

# Read the projects from the text file
while IFS= read -r project; do
    # Create the directory
    mkdir -p "$project"
done < "projects.txt"
