#!/usr/bin/env python

# --------------------------------------------------------
# Parse Directory, find and move files to directories 
# for processing.
#
#  	1. Remove cruft from folders
#
#	2. Move the following file types 
#       + ISOs (.iso)
#       + Tarballs (.tar, .tgz, .zip)
#       + Reencodes (.avi, .flv, .mpg)
#
# --------------------------------------------------------

# Using this script
# --------------------------------------------------------

# ./file-mover.py -t -d SOURCEDIR

#   -t = test mode. No files move.

# --------------------------------------------------------
# Load Libraries
# --------------------------------------------------------
import sys 
import os 
import shutil

from inspect import getmembers
from pprint import pprint
from optparse import OptionParser
from termcolor import colored


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
# Set cruft cull list
# --------------------------------------------------------

cruft_names = [
    "Torrent","H33T", "Demonoid"                                    # Name segments to cull
]

cruft_exts = [".url",".torrent"]                                    # File extensions to cull


# --------------------------------------------------------
# Set file extension lists
# --------------------------------------------------------

exts_isos = [".iso",".ISO"]                                         # File Extensions (ISOs)

exts_tarballs= [".tar",".TAR",".tgz",".TGZ",".zip",".ZIP"]          # File Extensions (Tarballs)

exts_reencodes = [".avi",".AVI",".flv",".FLV",".mpg",".MPG"]        # File Extensions (Reencodes)


# --------------------------------------------------------
# Required Functions
# --------------------------------------------------------


def cull_cruft ( sourcedir, cruft_names, cruft_exts ):

    cruft_removed = 0

    for pathroot, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                        # Split filenames into basename & ext
            
            remove_path = pathroot+"/"+f

            if any(cruft in fname for cruft in cruft_names):
#           if fname in cruft_exts:                                  # FIND & DELETE CRUFT BY NAME

                print colored("  + ","red"), fname+fext

                if options.test == False:
                    os.remove(pathroot+"/"+f)                        # Delete Cruft (Execute)
                else:
                    print colored("     rm","magenta",attrs=['bold']), colored(remove_path, "blue")

                cruft_removed = cruft_removed+1

            elif fext in cruft_exts:                                 # FIND & DELETE CRUFT BY EXT

                print colored("  + ","red"), fname+fext

                if options.test == False:
                    os.remove(pathroot+"/"+f)                        # Delete Cruft (Execute)
                else:
                    print colored("     rm","magenta",attrs=['bold']), colored(remove_path, "blue")

                cruft_removed = cruft_removed+1

    if cruft_removed == 0:
        print "No cruft found."

    return cruft_removed


def find_move_reencode ( sourcedir, exts_reencodes, target_reencodes ):

    """
        1. Walk sourcedir using os.walk
        
        2. Read each directory checking for the first file that matches a value in exts_reencodes (list)
        
        3. Move files as follows:
            
            a. If found file is in sourcedir root, move the file only
            
            b. If found file is in a subdir of sourcedir, 
                
                + move the entire subdir
                
                + break and skip to the next subdir
    """

    reencodes_moved = 0

    for pathroot, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for p in pathroot:

            for f in filenames:
 
                fname,fext = os.path.splitext(f)                        # Split filenames into basename & ext

                if fext in exts_reencodes:                              # FIND & MOVE Reencodes

                    if pathroot == sourcedir:

                        move_source = pathroot+f
                        move_target = target_reencodes+"/"+f

                        print colored("  + ","yellow"), fname+fext

                        if options.test == False:
                            shutil.move(move_source, move_target)    # Move File (Execute)
                        else:
                            print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                        reencodes_moved = reencodes_moved+1

                    else:

                        move_source = pathroot
                        move_target = target_reencodes+"/."

                        print colored("  * ","cyan"), fname+fext

                        if options.test == False:
                            shutil.move(move_source, move_target) 
                        else:
                            print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                        reencodes_moved = reencodes_moved+1
                    break

    if reencodes_moved == 0:
        print "No reencodes found."

    return (reencodes_moved)


def find_move_iso ( sourcedir, exts_isos, target_isos ):

    isos_moved = 0

    for pathroot, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                        # Split filenames into basename & ext

            if fext in exts_isos:                                   # FIND & MOVE ISOS

                if pathroot == sourcedir:

                    move_source = pathroot+f
                    move_target = target_isos+"/"+f

                    print colored("  + ","yellow"), fname+fext

                    if options.test == False:
                        shutil.move(move_source, move_target)    # Move File (Execute)
                    else:
                        print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                    isos_moved = isos_moved+1

                else:
                    
                    move_source = pathroot
                    move_target = target_isos+"/."

                    print colored("  * ","cyan"), fname+fext
                    
                    if options.test == False:
                        shutil.move(move_source, move_target) 
                    else:
                        print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                    isos_moved = isos_moved+1

    if isos_moved == 0:
        print "No ISOs found."

    return (isos_moved)


def find_move_tarball ( sourcedir, exts_tarballs, target_tarballs ):

    tarballs_moved = 0

    for pathroot, dirnames, filenames in os.walk(sourcedir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_tarballs:                               # FIND & MOVE TARBALLS

                if pathroot == sourcedir:

                    move_source = pathroot+f
                    move_target = target_tarballs+"/"+f

                    print colored("  + ","yellow"), fname+fext
                    if options.test == False:
                        shutil.move(move_source, move_target)    # Move File (Execute)
                    else:
                        print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                    tarballs_moved = tarballs_moved+1

                else:
                    
                    move_source = pathroot
                    move_target = target_tarballs+"/."

                    print colored("  * ","cyan"), fname+fext
                    
                    if options.test == False:
                        shutil.move(move_source, move_target) 
                    else:
                        print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                    tarballs_moved = tarballs_moved+1

    if tarballs_moved == 0:
        print "No tarballs found."

    return (tarballs_moved)


# --------------------------------------------------------
# FIND & REMOVE CRUFT
# --------------------------------------------------------

print "\n------------------------------------"
print colored("Remove Cruft","yellow")
print "------------------------------------"

cruft_removed = cull_cruft (sourcedir, cruft_names, cruft_exts)

print "------------------------------------"
print colored("Cruft Removed:","green"), colored(cruft_removed,"yellow"),"files\n"


# --------------------------------------------------------
# FIND & MOVE REENCODESs
# --------------------------------------------------------

print "------------------------------------"
print colored("Move Reencodes","yellow")
print "------------------------------------"

reencodes_moved = find_move_reencode (sourcedir, exts_reencodes, target_reencodes)

""""
reencode_dirs = list(set(reencode_dirs))

if reencodes_moved == 0:
    print "No reencodes found."
else:
    print ("\n".join(reencode_dirs))
"""

print "------------------------------------"
print colored("Reencodes Moved:","green"), colored(reencodes_moved,"yellow"),"files\n"


# --------------------------------------------------------
# FIND & MOVE ISOS
# --------------------------------------------------------

print "------------------------------------"
print colored("Move ISOs","yellow")
print "------------------------------------"

isos_moved = find_move_iso (sourcedir, exts_isos, target_isos)

print "------------------------------------"
print colored("ISOs Moved:","green"), colored(isos_moved,"yellow"),"files\n"


# --------------------------------------------------------
# FIND & MOVE TARBALLS
# --------------------------------------------------------

print "------------------------------------"
print colored("Move Tarballs","yellow")
print "------------------------------------"

tarballs_moved = find_move_tarball (sourcedir, exts_tarballs, target_tarballs)

print "------------------------------------"
print colored("Tarballs Moved:","green"), colored(tarballs_moved,"yellow"),"files\n"


# --------------------------------------------------------
# EOF
# --------------------------------------------------------