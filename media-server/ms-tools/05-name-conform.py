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
                  
                  
                  
import shutil

def remove_char(name):
    for item in remove_chars:
        name = name.replace(item[0], item[1])
    return name   

def remove_word(name):
    for item in remove_words:
        name = name.replace(item[0], item[1])
    return name   
    
def replace_space(name):
    for item in replace_spaces:
        name = name.replace(item[0], item[1])
    return name 
    
def replace_word(name):
    for item in replace_words:
        name = name.replace(item[0], item[1])
    return name     

# Remove Trailing Underscore (tus)   
def remove_tus(name):
    if name.endswith("_"):
        name = "ball"
#       name = name[:-1]
#    else:
#        name = name
	return name 

for dirpath, dirs, files in os.walk(sourcedir):
    for f in files:
		fname, fext = os.path.splitext(f)
		name = remove_char(fname)
		name = remove_word(name)
		name = replace_space(name)
		name = replace_word(name)
		name = remove_tus(name)

#		name = name.title()+fext.lower()
		
		print ("FN: "+name+" EXT: "+fext)

# conform_killcruft () 		# Remove Cruft
# --------------------------------------------------------

# conform_stanrdize () 		# Final Standardization
# --------------------------------------------------------

# write_log () 				# Write List To DB
# --------------------------------------------------------