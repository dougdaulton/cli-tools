#!/usr/bin/env python

# --------------------------------------------------------
# Load Libraries
# --------------------------------------------------------
import sys 
import os 
import shutil

from inspect import getmembers
from pprint import pprint
from optparse import OptionParser


print "##########################################"

# --------------------------------------------------------
# Set sourcedir
# --------------------------------------------------------
parser = OptionParser()
parser.add_option("-d", dest="dir")

(options, args) = parser.parse_args()


if options.dir == None:
    sourcedir = os.getcwd()
else:
    sourcedir = options.dir


# --------------------------------------------------------
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


# --------------------------------------------------------
# Set targetdirs & file extension lists
# --------------------------------------------------------


def find_move_iso ( sourcedir, exts_isos ):

    targetpath = target_isos                                            # Set target directory

    iso_dirs =[]

    for dirpath, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_isos:                   # FIND & MOVE ISOS

                print fname+fext

#                print ("mv "+dirpath+"/"+f+" --> "+targetpath+"/"+f)    # Move File (Display)
#                shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

                iso_dirs.append(dirpath)

#            else:
#                print f+" is not a an ISO."

    return iso_dirs


def find_move_tarball ( sourcedir, exts_tarballs ):

    targetpath = target_tarballs                        # Set target directory

    tarball_dirs =[]

    for dirpath, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_tarballs:               # FIND & MOVE TARBALLS
                
                print fname+fext

#                print ("mv "+dirpath+"/"+f+" --> "+targetpath+"/"+f)    # Move File (Display)
#              shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

                tarball_dirs.append(dirpath) 

#            else:
#                print f+" is not a tarball."

    return tarball_dirs


def find_move_reencode ( sourcedir, exts_reencodes ):

    targetpath = target_reencodes                       # Set target directory

    reencode_dirs =[]

    for dirpath, dirnames, filenames in os.walk(sourcedir,topdown=True):

        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_reencodes:              # FIND & MOVE Reencodes

#                print ("mv "+dirpath+" --> "+targetpath+"/")        # Move File (Display)
#                shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

                reencode_dirs.append(dirpath) 

#            else:
#                print "No reencodes found."

    return reencode_dirs


# --------------------------------------------------------
# FIND & MOVE ISOS
# --------------------------------------------------------

print "# ------------------------------------"
print "# ISOs Moved"
print "# ------------------------------------"

iso_dirs = find_move_iso (sourcedir, exts_isos)

iso_dirs = list(set(iso_dirs))


# --------------------------------------------------------
# FIND & MOVE TARBALLS
# --------------------------------------------------------

print "\n# ------------------------------------"
print "# Tarballs Moved"
print "# ------------------------------------"
tarball_dirs = find_move_tarball (sourcedir, exts_tarballs)

tarball_dirs = list(set(tarball_dirs))


# --------------------------------------------------------
# FIND & MOVE REENCODESs
# --------------------------------------------------------

print "\n# ------------------------------------"
print "# Reencodes Moved"
print "# ------------------------------------"

reencode_dirs = find_move_reencode (sourcedir, exts_reencodes)

reencode_dirs = list(set(reencode_dirs))

print ("\n".join(reencode_dirs))

# REMOVE EMPTY DIRECTORIES
# --------------------------------------------------------

print "\n# ------------------------------------"
print ("\n".join(iso_dirs)) 
print "# ------------------------------------"

print "\n# ------------------------------------"
print ("\n".join(tarball_dirs)) 
print "# ------------------------------------"

print "\n# ------------------------------------"
print ("\n".join(reencode_dirs)) 
print "# ------------------------------------"

print "################ EOS ####################"

# --------------------------------------------------------
# EOF
# --------------------------------------------------------