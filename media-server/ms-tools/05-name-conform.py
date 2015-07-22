#!/usr/bin/env python
#-*- coding: utf-8 -*-

# --------------------------------------------------------
# Parse Directory and conforms all filenames as follows:
#
#	1. Filename 
#       + Title Case
#       + Only Letters, Numbers & Underscores
#
# 	2. File Extension
#       + Lower Case
#	
#  	3. Remove cruft from filename
#
#  	4. Standardize the following:
#       + Release Year
#       + Resolution (if available)
#       + Source Abreviations
# --------------------------------------------------------

# Using this script
# --------------------------------------------------------

# ./name-conform.py -d SOURCEDIR

# Configure environment
# --------------------------------------------------------

import sys 
import os 
import shutil
import unicodedata

from optparse import OptionParser
from termcolor import colored


# Set sourcedir
# --------------------------------------------------------
parser = OptionParser()
parser.add_option("-d", dest="dir")
parser.add_option("-t", action="store_true", dest="test")

(options, args) = parser.parse_args()

if options.dir == None:
    sourcedir = os.getcwd()
else:
    sourcedir = options.dir


# Remove & Replace Lists (rnr_list)
# --------------------------------------------------------

remove_chars = [
    ["#",""],["%",""],[":",""],["'",""],[",",""],["(",""],[")",""], 
    ["{",""],["}",""],["[",""],["]",""],["!",""]
]

remove_words = [
    ["_X264",""],["Symposium",""],["Archery",""],["_ROUTED",""]
]


replace_spaces = [
    [" ","_"],[".","_"],["-","_"],["+","_"],["_-_","_"],["_–_","_"],["-","_"], 
    ["~~~","_"],["___","_"],["__","_"],[" - ","_"],["_«_","_"],[" ","_"]
]

replace_words = [
    ["1080P","1080"],["1080p","1080"],["720P","720"],["720p","720"],["Dslr","DSLR"],
    ["&","And"],["'S","s"],["`S","s"]
]

replace_fixes = [
    ["Dt","DT"],["Tutsplus","TP"],["Tp","TP"],["Kt","KT"],["Ldc","LDC"],["Nma","NMA"],["Sf","SF"],
    ["Dp","DP"],["Seo","SEO"],["Skillshare","SS"],["Ss","SS"],["Hdr","HDR"],["Ppc","PPC"],["Cd","CD"],
    ["Video_Copilot","VPC"]
]


# Remove and Replace Functions
# --------------------------------------------------------

def remove_and_replace ( old_name, rnr_list ):
    for item in rnr_list:
        old_name = old_name.replace(item[0], item[1])
    return old_name 


# --------------------------------------------------------
# Execute Standards Rename: FILENAMES
# --------------------------------------------------------

for dirpath, dirs, files in os.walk(sourcedir):                     # Parse The Directory
    for f in files:
        print f
        fname, fext = os.path.splitext(f)                           # Split files into basename & ext
        fname = remove_and_replace(fname,remove_words)              # Remove unwanted words
        fname = remove_and_replace(fname,remove_chars)              # Remove unwanted characters
        fname = remove_and_replace(fname,replace_spaces)            # Standardize spaces & space markers 
        fname = remove_and_replace(fname,replace_words)             # Standardize filename elements
        fname = fname.rstrip('_')                                   # Remove trailing underscore(s)

        fname = fname.title()+fext.lower()                          # Assemble filename and apply case conversions

        fname = remove_and_replace(fname,replace_fixes)             # Fix required capitialization

        move_source = os.path.join(dirpath,f)
        move_target = os.path.join(dirpath,fname)
        
        if not options.test:
            shutil.move(move_source, move_target)                   # Rename files

        print colored("OFN:","blue"),colored(move_source,"green")   # Display changed filenames
        print colored("NFN:","cyan"), move_target,"\n"


# --------------------------------------------------------
# Execute Standards Rename: DIRECTORIES
# --------------------------------------------------------
""""
for dirpath, dirs, files in os.walk(sourcedir):                     # Parse The Directory
    for d in dirs:	
        print d 
        dname = remove_and_replace(d,remove_words)                  # Remove unwanted words
        dname = remove_and_replace(dname,remove_chars)              # Remove unwanted characters
        dname = remove_and_replace(dname,replace_spaces)            # Standardize spaces & space markers 
        dname = remove_and_replace(dname,replace_words)             # Standardize filename elements
        dname = dname.rstrip('_')                                   # Remove trailing underscore(s)

        dname = dname.title()                                       # Reset Directory Name to Title Case

        dname = remove_and_replace(dname,replace_fixes)             # Fix required capitialization

        move_source = os.path.join(dirpath,d)
        move_target = os.path.join(dirpath,dname)

        if not options.test:
            shutil.move(move_source, move_target)                   # Rename files

        print colored("ODN:","blue"),colored(move_source,"yellow")  # Display changed filenames
        print colored("NDN:","cyan"), move_target,"\n"
"""
# --------------------------------------------------------
# EOF
# --------------------------------------------------------	
