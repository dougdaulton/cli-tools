#!/usr/bin/env python

# --------------------------------------------------------
# Parse Directory and conforms all filenames as follows:
#
#	1. Filename 
#		Title Case
#		Only Letters, Numbers & Underscores
#  
# 	2. File Extension
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

import sys 
import os 
import shutil
from optparse import OptionParser

# Set sourcedir
# --------------------------------------------------------
parser = OptionParser()
parser.add_option("-d", dest="dir")

(options, args) = parser.parse_args()

#try: options.dir

if options.dir == None:
    sourcedir = os.getcwd()
else:
    sourcedir = options.dir


# Cruft Removal Definitions & Functions  
# --------------------------------------------------------
remove_words = [["YIFY", ""],["ETRG", ""],["[ www.Torrenting.com ] - ", ""], ["{AceMerlin}", ""]]

remove_chars = [["#",""],["%", ""],[":", ""],["'", ""],[",", ""],["(", ""],[")", ""], ["{", ""], ["}", ""], ["[", ""], ["]", ""], ["!", ""]]

def remove_char(fname):
    for item in remove_chars:
        fname = fname.replace(item[0], item[1])
    return fname   

def remove_word(fname):
    for item in remove_words:
        fname = fname.replace(item[0], item[1])
    return fname   
    

# Standardization Definitions & Functions  
# --------------------------------------------------------

replace_spaces = [[" ", "_"], [".", "_"], ["-", "_"],["__", "_"],["___", "_"]]

replace_words = [["1080P", "1080"], ["1080p", "1080"], ["720P", "720"],["720p", "720"],["&", "And"], ["'S", "s"], ["`S", "s"]]

replace_sources = [["Digital Tutors", "DT"],["Digital_Tutors", "DT"],["Dt", "DT"],["Kelbyone", "KT"],["Kelby_Training", "KT"],["Kt", "KT"],["Lynda", "LDC"],["Ldc", "LDC"],["New_Masters_Academy", "NMA"],["Nma", "NMA"],["Skillfeed", "SF"],["Sf", "SF"],["Amherst_Media", "AM"],["Dslr", "DSLR"],["Digital_Photographer", "DP"],["Dp", "DP"],["Hdr", "HDR"],["__", "_"],["Cc", "CC"],["EPubs", "ePubs"],["Nra", "NRA"],["Gnomon", "GNOMON"],["Seo", "SEO"], ["Indesign", "InDesign"], ["Skillshare", "SS"], ["Ss", "SS"], ["Phlearn","PHLEARN"]]

def replace_space(fname):
    for item in replace_spaces:
        fname = fname.replace(item[0], item[1])
    return fname 
    
def replace_word(fname):
    for item in replace_words:
        fname = fname.replace(item[0], item[1])
    return fname    
    
def replace_source(fname):
    for item in replace_sources:
        fname = fname.replace(item[0], item[1])
    return fname         


# --------------------------------------------------------
# Execute Standards Rename: FILENAMES
# --------------------------------------------------------

for dirpath, dirs, files in os.walk(sourcedir):				# Parse The Directory
    for f in files:												
		fname, fext = os.path.splitext(f)			# Split files into basename & ext
		fname = remove_word(fname)				# Remove unwanted words
		fname = remove_char(fname)				# Remove unwanted characters
		fname = replace_space(fname)				# Standardize spaces & space markers 
		fname = replace_word(fname)				# Standardize filename elements
		fname = fname.rstrip('_')				# Remove trailing underscore(s)

		fname = fname.title()+fext.lower()			# Assemble filename and apply case conversions
		
		fname = replace_source(fname)				# Standardize Source Prefixes
		
		shutil.move(dirpath+"/"+f, dirpath+"/"+fname)		# Rename files
		print ("mv "+dirpath+"/"+f+" "+dirpath+"/"+fname)	# Display changed filenames


# --------------------------------------------------------
# Execute Standards Rename: DIRECTORIES
# --------------------------------------------------------

for dirpath, dirs, files in os.walk(sourcedir):				# Parse The Directory
    for d in dirs:	
   		dname = remove_word(d)					# Remove unwanted words												
		dname = remove_char(dname)				# Remove unwanted characters
		dname = replace_space(dname)				# Standardize spaces & space markers 
		dname = replace_word(dname)				# Standardize filename elements
		dname = dname.rstrip('_')				# Remove trailing underscore(s)
		
   		dname = dname.title()					# Reset Directory Name to Title Case
		
		dname = replace_source(dname)				# Standardize Source Prefixes

		
		shutil.move(dirpath+"/"+d, dirpath+"/"+dname)		# Rename directories
		print ("mv "+dirpath+"/"+d+" "+dirpath+"/"+dname)	# Display changed directories
		
# --------------------------------------------------------
# EOF
# --------------------------------------------------------	
