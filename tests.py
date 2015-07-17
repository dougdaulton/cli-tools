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

target_isos = "/go/TR/02_TARGET/00_ISOS"                                # Watch Folder:  ISOs

target_tarballs = "/go/TR/02_TARGET/01_TARBALLS"                        # Watch Folder: Tarballs

target_reencodes = "/go/TR/02_TARGET/02_REENCODES"                      # Watch Folder: Reencodes

#target_isos = "/go/PROCESS/00_ISOS"                                # Watch Folder:  ISOs

#target_tarballs = "/go/PROCESS/01_TARBALLS"                        # Watch Folder: Tarballs

#target_reencodes = "/go/PROCESS/02_REENCODE"                        # Watch Folder: Reencodes

exts_isos = [".iso",".ISO"]                                    # File Extensions (ISOs)

exts_tarballs= [".tar",".TAR",".tgz",".TGZ",".zip",".ZIP"]     # File Extensions (Tarballs)

exts_reencodes = [".avi",".AVI",".flv",".FLV",".mpg",".MPG"]   # File Extensions (Reencodes)


# FIND & MOVE FILES
# --------------------------------------------------------

for dirpath, dirs, files in os.walk(sourcedir):                 # Parse The Directory
    for f in files:
        fname, fext = os.path.splitext(f)                       # Split files into basename & ext
        
        if any(fext in x for x in exts_isos):                  # FIND & MOVE ISOS
            targetpath = target_isos                               # Set target directory
           
            print ("mv "+dirpath+"/"+f+" "+targetpath+"/"+f)    # Move File (Display)
#           shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

            iso_dirs = iso_dirs.extend(dirpath) 

        elif any(fext in x for x in exts_tarballs):              # FIND & MOVE TARBALLS
            targetpath = target_tarballs                           # Set target directory
            
            print ("mv "+dirpath+"/"+f+" "+targetpath+"/"+f)    # Move File (Display)
#           shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

            tarball_dirs = tarball_dirs.extend(dirpath) 

        elif any(fext in x for x in exts_reencodes):             # FIND & MOVE Reencodes
            targetpath = target_reencodes                          # Set target directory

	     	
            dir2move = os.path.basename(dirpath)
            print ("mv "+dirpath+" --> "+targetpath+"/")    # Move File (Display)
#           shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

        else:
            print "# ------------------------------------"
            print "# NOTHING TO MOVE"
            print "# ------------------------------------"

        return iso_dirs
        return tarball_dirs

# REMOVE EMPTY DIRECTORIES
# --------------------------------------------------------
iso_dirs = set(iso_dirs)
print ("++++++++++\n"+iso_dirs+"++++++++++\n\n") 

tarball_dirs = set(tarball_dirs)
print ("++++++++++\n"+tarball_dirs+"++++++++++\n") 
# --------------------------------------------------------
# EOF
# --------------------------------------------------------	
print "##########################################"
