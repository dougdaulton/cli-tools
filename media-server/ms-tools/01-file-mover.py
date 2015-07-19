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
    "Torrent","H33T", "Demonoid", "torrent"                         # Name segments to cull
]

cruft_exts = [".url",".torrent",".nfo"]                              # File extensions to cull


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


def find_move_files ( files_type, source_dir, ext_list, target_dir ):

    """
        1. Walk source_dir
        
        2. Read each directory checking for the first file extension to match value in exts_reencodes (list)
        
        3. Move files as follows:
            
            a. If found file is in source_dir root, move the file only
            
            b. If found file is in a sub_dir of source_dir, 
                
                + move the entire sub_dir
                
                + break and skip to the next sub_dir
    """

    files_moved = 0
    folders_moved = 0
    
    for current_dir, sub_dirs, filenames in os.walk(source_dir,topdown=True):
        for f in filenames:
            if os.path.splitext(f)[1] in ext_list:
                if current_dir is source_dir:
                    move_source = os.path.join(current_dir, f)
                    print colored("  + ","yellow"), f
                    files_moved += 1
                else:
                    move_source = current_dir
                    folders_moved += 1
                    print colored("  * ","cyan"), current_dir
                
                move_target = os.path.join(target_dir)
                
                if not options.test:
                    shutil.move(move_source, move_target)
                else:
                    print colored("     mv", "magenta", attrs=['bold']), colored(move_source,"blue"), colored(move_target,"green")
                
                if (current_dir is not source_dir and files_type == "reencodes"):
                    break

    total_moved = files_moved + folders_moved

    if total_moved == 0:
        print "No "+files_type+" found."

    return (files_moved, folders_moved)


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

reencode_files_moved, reencode_folders_moved = find_move_files ("reencodes", source_dir, exts_reencodes, target_reencodes)

print "------------------------------------"
print colored("Reencodes Moved:","green"), "folders:", colored(reencode_folders_moved,"yellow"), "files:", colored(reencode_files_moved,"yellow"),"\n"


# --------------------------------------------------------
# FIND & MOVE ISOS
# --------------------------------------------------------

print "------------------------------------"
print colored("Move ISOs","yellow")
print "------------------------------------"

iso_files_moved, iso_folders_moved = find_move_files ("ISOs", source_dir, exts_isos, target_isos)

print "------------------------------------"
print colored("ISOs Moved:","green"), "folders:", colored(iso_folders_moved,"yellow"), "files:", colored(iso_files_moved,"yellow"),"\n"


# --------------------------------------------------------
# FIND & MOVE TARBALLS
# --------------------------------------------------------

print "------------------------------------"
print colored("Move Tarballs","yellow")
print "------------------------------------"

tarball_files_moved, tarball_folders_moved = find_move_files ("tarballs", source_dir, exts_tarballs, target_tarballs)

print "------------------------------------"
print colored("Tarballs Moved:","green"), "folders:", colored(tarball_folders_moved,"yellow"), "files:", colored(tarball_files_moved,"yellow"),"\n"


# --------------------------------------------------------
# EOF
# --------------------------------------------------------