#!/usr/bin/env python

# Load Libraries
# -----------------------
import sys 
import glob 
import os 
import sh
from optparse import OptionParser

# some test code
# -----------------------

print "##########################################"
    
parser = OptionParser()
parser.add_option("-d", dest="dir")

(options, args) = parser.parse_args()

#try: options.dir

if options.dir == None:
    sourcedir = os.getcwd()
else:
    sourcedir = options.dir

# print sourcedir
""""
print "##########################################"

for dirpath, dirs, files in os.walk(sourcedir):
    print('DIR = %s' % dirpath)
    for f in files:
        print('\t%s' % f)
        
print "##########################################"     
"""    

# Define Substitutions    
remove_chars = [["#", ""],["%", ""],[":", ""],["(", ""],[")", ""], ["{", ""], ["}", ""], ["[", ""], ["]", ""]]
remove_words = [["YIFY", ""],["ETRG", ""],["Dsl", ""]]

replace_spaces = [[" ", "_"], [".", "_"], ["-", "_"],["__", "_"],["___", "_"]]
replace_words = [["1080P", "1080"], ["1080p", "1080"], ["720P", "720"],["720p", "720"]]


# Execute Substitutions

def remove_char(fname):
    for item in remove_chars:
        fname = fname.replace(item[0], item[1])
    return fname   

def remove_word(fname):
    for item in remove_words:
        fname = fname.replace(item[0], item[1])
    return fname   
    
def replace_space(fname):
    for item in replace_spaces:
        fname = fname.replace(item[0], item[1])
    return fname 
    
def replace_word(fname):
    for item in replace_words:
        fname = fname.replace(item[0], item[1])
    return fname     

for dirpath, dirs, files in os.walk(sourcedir):
    for f in files:
		fname, fext = os.path.splitext(f)
		fname = remove_char(fname)
		fname = remove_word(fname)
		fname = replace_space(fname)
		fname = replace_word(fname)
		fname = fname.rstrip('_')

		name = fname.title()+fext.lower()
		
#		print ("FN: "+fname+" EXT: "+fext)
		print ("mv "+f+" --> "+name)
		

#       shutil.move(dirpath+"/"+f, dirpath+"/"+name)
#		print ("mv "+dirpath+"/"+f+" "+dirpath+"/"+name)
	

print "##########################################"

""""
def unix_find(pathin):
    # Return results similar to the Unix find command run without options
    # i.e. traverse a directory tree and return all the file paths
    return [os.path.join(path, file)
            for (path, dirs, files) in os.walk(pathin)
            for file in files]

pathlist = unix_find(sourcedir)[:]

from pprint import pprint
pprint(pathlist)
    
    
print "##########################################"

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, file = os.path.split(full_path)
print(path + ' --> ' + file + "\n")

print("This file directory only")
print(os.path.dirname(full_path))
"""    