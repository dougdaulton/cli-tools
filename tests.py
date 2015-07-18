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
parser.add_option("-t", action="store_true", dest="test")

(options, args) = parser.parse_args()


if options.dir == None:
    sourcedir = os.getcwd()
else:
    sourcedir = options.dir


# --------------------------------------------------------
# Set targetdirs
# --------------------------------------------------------

if options.test == True:
    target_root = "/go/TR/02_TARGET/"

else:
    target_root = "/go/PROCESS/"

target_isos = target_root+"00_ISOS"                                # Watch Folder:  ISOs

target_tarballs = target_root+"01_TARBALLS"                        # Watch Folder: Tarballs

target_reencodes = target_root+"02_REENCODES"                      # Watch Folder: Reencodes


# --------------------------------------------------------
# Set file extension lists
# --------------------------------------------------------

exts_isos = [".iso",".ISO"]                                    # File Extensions (ISOs)

exts_tarballs= [".tar",".TAR",".tgz",".TGZ",".zip",".ZIP"]     # File Extensions (Tarballs)

exts_reencodes = [".avi",".AVI",".flv",".FLV",".mpg",".MPG"]   # File Extensions (Reencodes)


# --------------------------------------------------------
# Set targetdirs & file extension lists
# --------------------------------------------------------


def find_move_iso ( sourcedir, exts_isos ):

    targetpath = target_isos                                            # Set target directory

    iso_dirs =[]
    
    isos_moved = 0

    for dirpath, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_isos:                   # FIND & MOVE ISOS

                print "  + "+fname+fext

                if options.test == False:
                    shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

                iso_dirs.append(dirpath)
                
                isos_moved = isos_moved+1

    if isos_moved == 0:
        print "No ISOs found."


    return iso_dirs


def find_move_tarball ( sourcedir, exts_tarballs ):

    targetpath = target_tarballs                        # Set target directory

    tarball_dirs =[]
    
    tarballs_moved = 0

    for dirpath, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_tarballs:               # FIND & MOVE TARBALLS
                
                print "  + "+fname+fext

                if options.test == False:
                    shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

                tarball_dirs.append(dirpath) 
                
                tarballs_moved = tarballs_moved+1

    if tarballs_moved == 0:
        print "No tarballs found."

    return tarball_dirs


def find_move_reencode ( sourcedir, exts_reencodes ):

    targetpath = target_reencodes                       # Set target directory

    reencode_dirs =[]
    
    reencodes_moved = 0

    for dirpath, dirnames, filenames in os.walk(sourcedir,topdown=True):

        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_reencodes:              # FIND & MOVE Reencodes

                if options.test == False:
                    shutil.move(dirpath+"/"+f, targetpath+"/"+f)       # Move File (Execute)

                reencode_dirs.append(dirpath) 
                
                reencodes_moved = reencodes_moved+1

    return (reencodes_moved, reencode_dirs)

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

reencodes_moved, reencode_dirs = find_move_reencode (sourcedir, exts_reencodes)

reencode_dirs = list(set(reencode_dirs))

if reencodes_moved == 0:
    print "No Reencodes found."
else:
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