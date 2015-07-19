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

# ./file-mover.py -t -d source_dir

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
# Set source_dir
# --------------------------------------------------------
parser = OptionParser()
parser.add_option("-d", dest="dir")
parser.add_option("-t", action="store_true", dest="test")

(options, args) = parser.parse_args()


if options.dir:
    source_dir = options.dir
else:
    source_dir = os.getcwd()

# --------------------------------------------------------
# Set targetdirs
# --------------------------------------------------------

if options.test:
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


def cull_cruft ( source_dir, cruft_names, cruft_exts ):

    cruft_removed = 0

    for current_dir, sub_dirs, filenames in os.walk(source_dir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                        # Split filenames into basename & ext
            
            remove_path = current_dir+"/"+f

            if any(cruft in fname for cruft in cruft_names):
#           if fname in cruft_exts:                                  # FIND & DELETE CRUFT BY NAME

                print colored("  + ","red"), fname+fext

                if options.test == False:
                    os.remove(current_dir+"/"+f)                        # Delete Cruft (Execute)
                else:
                    print colored("     rm","magenta",attrs=['bold']), colored(remove_path, "blue")

                cruft_removed = cruft_removed+1

            elif fext in cruft_exts:                                 # FIND & DELETE CRUFT BY EXT

                print colored("  + ","red"), fname+fext

                if options.test == False:
                    os.remove(current_dir+"/"+f)                        # Delete Cruft (Execute)
                else:
                    print colored("     rm","magenta",attrs=['bold']), colored(remove_path, "blue")

                cruft_removed = cruft_removed+1

    if cruft_removed == 0:
        print "No cruft found."

    return cruft_removed


def find_move_reencode ( source_dir, exts_reencodes, target_reencodes ):

    """
        1. Walk source_dir
        
        2. Read each directory checking for the first file extension to match value in exts_reencodes (list)
        
        3. Move files as follows:
            
            a. If found file is in source_dir root, move the file only
            
            b. If found file is in a sub_dir of source_dir, 
                
                + move the entire sub_dir
                
                + break and skip to the next sub_dir
    """

    reencode_folders_moved = 0
    reencode_files_moved = 0

    for current_dir, sub_dirs, filenames in os.walk(source_dir,topdown=True):
        for f in filenames:
            if os.path.splitext(f)[1] in exts_reencodes:

#                if options.test:
#                    print "target_reencodes: "+target_reencodes, "\ncurrent_dir: "+current_dir

                if current_dir is source_dir:
                    move_source = os.path.join(current_dir, f)
                    print colored("  + ","yellow"), f
                    reencode_files_moved += 1
                else:
                    move_source = current_dir
                    reencode_folders_moved += 1
                    print colored("  * ","cyan"), current_dir
                
                move_target = os.path.join(target_reencodes)
                if not options.test:
                    shutil.move(move_source, move_target)
                else:
                    print colored("     mv", "magenta", attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")
                break

    reencodes_moved = reencode_files_moved + reencode_folders_moved

    if reencodes_moved == 0:
        print "No reencodes found."

    return (reencode_folders_moved,reencode_files_moved)


def find_move_iso ( source_dir, exts_isos, target_isos ):

    isos_moved = 0

    for current_dir, sub_dirs, filenames in os.walk(source_dir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                        # Split filenames into basename & ext

            if fext in exts_isos:                                   # FIND & MOVE ISOS

                if current_dir == source_dir:

                    move_source = current_dir+f
                    move_target = target_isos+"/"+f

                    print colored("  + ","yellow"), fname+fext

                    if options.test == False:
                        shutil.move(move_source, move_target)    # Move File (Execute)
                    else:
                        print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                    isos_moved = isos_moved+1

                else:
                    
                    move_source = current_dir
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


def find_move_tarball ( source_dir, exts_tarballs, target_tarballs ):

    tarballs_moved = 0

    for current_dir, sub_dirs, filenames in os.walk(source_dir,topdown=True):
    
        for f in filenames:

            fname,fext = os.path.splitext(f)                       # Split filenames into basename & ext

            if fext in exts_tarballs:                               # FIND & MOVE TARBALLS

                if current_dir == source_dir:

                    move_source = current_dir+f
                    move_target = target_tarballs+"/"+f

                    print colored("  + ","yellow"), fname+fext
                    if options.test == False:
                        shutil.move(move_source, move_target)    # Move File (Execute)
                    else:
                        print colored("     mv","magenta",attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")

                    tarballs_moved = tarballs_moved+1

                else:
                    
                    move_source = current_dir
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

cruft_removed = cull_cruft (source_dir, cruft_names, cruft_exts)

print "------------------------------------"
print colored("Cruft Removed:","green"), colored(cruft_removed,"yellow"),"files\n"


# --------------------------------------------------------
# FIND & MOVE REENCODESs
# --------------------------------------------------------

print "------------------------------------"
print colored("Move Reencodes","yellow")
print "------------------------------------"

reencode_folders_moved, reencode_files_moved = find_move_reencode (source_dir, exts_reencodes, target_reencodes)

print "------------------------------------"
print colored("Reencodes Moved:","green"), "folders:", colored(reencode_folders_moved,"yellow"), "files:", colored(reencode_files_moved,"yellow"),"\n"


# --------------------------------------------------------
# FIND & MOVE ISOS
# --------------------------------------------------------

print "------------------------------------"
print colored("Move ISOs","yellow")
print "------------------------------------"

isos_moved = find_move_iso (source_dir, exts_isos, target_isos)

print "------------------------------------"
print colored("ISOs Moved:","green"), colored(isos_moved,"yellow"),"files\n"


# --------------------------------------------------------
# FIND & MOVE TARBALLS
# --------------------------------------------------------

print "------------------------------------"
print colored("Move Tarballs","yellow")
print "------------------------------------"

tarballs_moved = find_move_tarball (source_dir, exts_tarballs, target_tarballs)

print "------------------------------------"
print colored("Tarballs Moved:","green"), colored(tarballs_moved,"yellow"),"files\n"


# --------------------------------------------------------
# EOF
# --------------------------------------------------------