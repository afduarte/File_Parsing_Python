#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Delete Lines Python Script

from sys import argv, stdout # Imports arguments and stdout from sys

oldFile = argv[1] # The path for the file we want to modify
find = argv[2:] # The array of different strings we want to look for (every argument after the first one)

f = open(oldFile,"r") # Open the old file in read mode
lines = f.readlines() # Create array with every line in the old file
f.close() # Close the old file

newFile = oldFile+".new" # New file name is oldfilename.extension.new

n = open(newFile,"w") # Open new file in write mode

for string in find:            # For every string passed in and
    for line in open(oldFile): # For every line in the old file
        if string not in line: # Check for string
            n.write(line)      # If it exists, don't write it to new file.

n.close() # Close the new file
print("Deleted every line that contained "+find+" output to file: "+newFile)
