#! /bin/bash

shopt -s nullglob
shopt -s extglob

# -----------------------------------------------------
# Pull FIles From ISO
# -----------------------------------------------------

# From the BASH shell

# bash pull-from-ISO.sh ISO-key SOURCEDIR WRITEDIR


# Establish Variables
# -----------------------------------------------------
	SOURCEDIR="$(dirname "$1")"
	
	SAVEIFS=$IFS										# Used for filenames with spaces
	IFS=$(echo -en "\n\b")								# Used for filenames with spaces



# Make Required directories
# -----------------------------------------------------
# sudo mkdir /media/tmpISO								# Temporary ISO Mount Point


#	sudo mkdir $WRITEDIR"/"00_REENCODE
#	sudo mkdir $WRITEDIR"/"01_TO_FILE

# Read the Directory
# -----------------------------------------------------

#	ISOPATHS=${SOURCEDIR}/**/*.iso
	
	ISOPATHS=$(find ${SOURCEDIR} -type f -name "*.iso")
	
	for isofile in $ISOPATHS
	do
		ISOFOLDER=${isofile##*/}						# Strip leading DIRS off of ISO NAME
		ISOFOLDER=${ISOFOLDER%.*}						# Strip .iso off ISO name to create folder name

		sudo mount -o loop $isofile /media/tmpISO		# Mount ISO to filesystem
		
		# Load Directory into Array
		
		ISOCONTENTS=$(find /media/tmpISO -type f)		# Read ISO Contents into array
		
#		echo -e "\n"$ISOCONTENTS
#		echo -e "\nBREAK\n"
		
		i=0;
		for f in $ISOCONTENTS; 
		do
			mediafiles[$i]="$f"
			((i++))
		done

		echo -e "\nMEDIA PATH:"$mediafiles""
	
		mediatype=${mediafiles##*.}			
#		mediatype="avi"
		
		echo -e "MEDIA TYPE:" $mediatype"\n"
						
		if [ $mediatype == "flv" ]
			then
				WRITESUBDIR="00_REENCODE"
									
		elif [ $mediatype == "avi" ]
			then
				WRITESUBDIR="00_REENCODE"
					
		else 
			WRITESUBDIR="01_TO_FILE"		
		fi	

		WRITEDIR=$2"/"$WRITESUBDIR"/"$ISOFOLDER
		
		#ls -lah /media/tmpISO/!(*.nfo)
	
		mkdir $WRITEDIR

		cp -rv /media/tmpISO/*!(*.nfo) $WRITEDIR

		sudo umount /media/tmpISO 						# Unmount ISO from filesystem
		
		echo rm -rf $WRITEDIR/*nfo
		
#		unset $WRITEDIR
		
		sleep 5
		
	done




# Remove Selected String
# -----------------------------------------------------

#ls directory | xargs cp -v dir2


# CLEANUP BEFORE SCRIPT ENDS
# -----------------------------------------------------
# sudo rm -rf /media/tmpISO								# Remove Temporary ISO Mount Point

IFS=$SAVEIFS											# Used for filenames with spaces


#

	
#	ISOPATHS=${find ${SOURCEDIR}/**/*.iso -type f}
#	ISONAMES=$(ls -R $SOURCEDIR | fgrep ".iso")