#!/usr/bin/env python

# Load Libraries
# -----------------------
import sys 
import os 
import shutil
from optparse import OptionParser

# some test code
# -----------------------

print "##########################################"
    
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


# Set targetdirs & file extension lists
# --------------------------------------------------------

dir_isos = "/go/TR/02_TARGET/00_ISOS"                                # Watch Folder:  ISOs

dir_tarballs = "/go/TR/02_TARGET/01_TARBALLS"                        # Watch Folder: Tarballs

dir_reencodes = "/go/TR/02_TARGET/02_REENCODES"                      # Watch Folder: Reencodes

#dir_isos = "/go/PROCESS/00_ISOS"                                # Watch Folder:  ISOs

#dir_tarballs = "/go/PROCESS/01_TARBALLS"                        # Watch Folder: Tarballs

#dir_reencodes = "/go/PROCESS/02_REENCODE"                        # Watch Folder: Reencodes

files_isos = [".iso",".ISO"]                                    # File Extensions (ISOs)

files_tarballs= [".tar",".TAR",".tgz",".TGZ",".zip",".ZIP"]     # File Extensions (Tarballs)

files_reencodes = [".avi",".AVI",".flv",".FLV",".mpg",".MPG"]   # File Extensions (Reencodes)


# FIND & MOVE FILES
# --------------------------------------------------------

for dirpath, dirs, files in os.walk(sourcedir):                 # Parse The Directory
    for f in files:
        fname, fext = os.path.splitext(f)                       # Split files into basename & ext
        
        if any(fext in x for x in files_isos):                  # FIND & MOVE ISOS
            targetpath = dir_isos                               # Set target directory
           
            print ("mv "+dirpath+"/"+f+" "+targetpath+"/"+f)    # Move File (Display)
#           shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

        if any(fext in x for x in files_tarballs):              # FIND & MOVE TARBALLS
            targetpath = dir_tarballs                           # Set target directory
            
            print ("mv "+dirpath+"/"+f+" "+targetpath+"/"+f)    # Move File (Display)
#           shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

        if any(fext in x for x in files_reencodes):             # FIND & MOVE Reencodes
            targetpath = dir_reencodes                          # Set target directory

            print ("mv "+dirpath+"/"+f+" "+targetpath+"/"+f)    # Move File (Display)
#           shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

# --------------------------------------------------------
# EOF
# --------------------------------------------------------	
print "##########################################"
