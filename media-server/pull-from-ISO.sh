#! /bin/bash

shopt -s nullglob

# -----------------------------------------------------
# Pull FIles From ISO
# -----------------------------------------------------

# From the BASH shell

# bash pull-from-ISO.sh ISO-key SOURCEDIR WRITEDIR


# Establish Variables
# -----------------------------------------------------
	SOURCEDIR="$(dirname "$1")"
	WRITEDIR=$2
	
	SAVEIFS=$IFS										# Used for filenames with spaces
	IFS=$(echo -en "\n\b")								# Used for filenames with spaces



# Make Required directories
# -----------------------------------------------------
# sudo mkdir /media/tmpISO								# Temporary ISO Mount Point


echo sudo mkdir $WRITEDIR"/"00_REENCODE
echo sudo mkdir $WRITEDIR"/"01_TO_FILE

# Read the Directory
# -----------------------------------------------------

#	ISOPATHS=${SOURCEDIR}/**/*.iso
	
	ISOPATHS=$(find ${SOURCEDIR} -type f -name "*.iso")
	
	for isofile in $ISOPATHS
	do
		ISOFOLDER=${isofile##*/}						# Strip leading DIRS off of ISO NAME
		ISOFOLDER=${ISOFOLDER%.*}						# Strip .iso off ISO name to create folder name
		echo mkdir $WRITEDIR"/"$ISOFOLDER

		sudo mount -o loop $isofile /media/tmpISO		# Mount ISO to filesystem
#		ls -l /media/tmpISO								# Read ISO Contents into array
		
		ISOCONTENTS=$(find /media/tmpISO -type f)
		
		for mediafile in $ISOCONTENTS
		do
			mediaext=${mediafile##*.}
			echo $mediaext
		done

		sudo umount /media/tmpISO 						# Unmount ISO from filesystem
	done




# Remove Selected String
# -----------------------------------------------------

#ls directory | xargs cp -v dir2


# CLEANUP BEFORE SCRIPT ENDS
# -----------------------------------------------------
# sudo rm -rf /media/tmpISO								# Remove Temporary ISO Mount Point

IFS=$SAVEIFS											# Used for filenames with spaces

#SOURCEDIR-NULL
#WRITEDIR=NULL
#ISOPATHS=NULL
#ISOOLDER=NULL
#ISOCONTENTS=NULL


#

	
#	ISOPATHS=${find ${SOURCEDIR}/**/*.iso -type f}
#	ISONAMES=$(ls -R $SOURCEDIR | fgrep ".iso")