#!/usr/bin/env python

# --------------------------------------------------------
# Parse Directory and conforms all filenames as follows:
#
#	1. Filename 
#		Title Case
#		Only Letters, Numbers & Underscores
#  
#   2. File Extension
#		Lower Case
#	
#  	3. Remove cruft from filename
#	
#  	4. Standardize the following:
#		Release Year
#		Resolution (if available)
#  		Source Abreviations
# --------------------------------------------------------

# Using this script
# --------------------------------------------------------

# ./name-conform.py -d SOURCEDIR

# Configure environment
# --------------------------------------------------------

# Load Libraries
# -----------------------
import sys 
import glob 
import os 
import sh
from optparse import OptionParser

# Set sourcedir
# -----------------------
parser = OptionParser()
parser.add_option("-d", dest="dir")

(options, args) = parser.parse_args()

#try: options.dir

if options.dir == None:
    sourcedir = os.getcwd()
else:
    sourcedir = options.dir


# name_conform () 			# Master Function
# --------------------------------------------------------

# files_load () 			# Load Files from Dir 
# --------------------------------------------------------

# conform_nameext () 		# Conform File Name & Ext
# --------------------------------------------------------

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % title + ext))

# conform_killcruft () 		# Remove Cruft
# --------------------------------------------------------

# conform_stanrdize () 		# Final Standardization
# --------------------------------------------------------

# write_log () 				# Write List To DB
# --------------------------------------------------------