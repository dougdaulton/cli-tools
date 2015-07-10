#!/bin/bash

# rsync-plex.sh
# ------------------------------------------------------------------
# 
# This script is used to sync/backup media directories from a central 
# PLEX server. Run via crontab once a day, in the early AM hours.


# RUNNING THE SCRIPT
# ------------------------------------------------------------------

# From the BASH shell

# bash rsync-plex.sh sync-key RUSER RHOST RVOLUME

# From Cron

# 0 0 * * * rsync-plex.sh rsync-key RUSER RHOST RVOLUME


# SET BASE VARIABLES
# ------------------------------------------------------------------
RSYNC=/usr/bin/rsync 
SSH=/usr/bin/ssh 
KEY=/home/bayaz/cron/frog-rsync-key
RUSER=rsync-key[1]
RHOST=rsync-key[2]
RPATH=/VOLUMES/rsync-key[3]/PLEX

REMOTEPATH=(
	[0]=/VOLUMES/KODIAK4TB1/PLEX_MOVIES
	[1]=/VOLUMES/KODIAK4TB1/PLEX_TV
	[2]=/VOLUMES/KODIAK2TB/PLEX_MUSIC
	[3]=/VOLUMES/KODIAK2TB/PLEX_AUDIO
)

LOCALPATH=(
	[0]=$RPATH/MOVIES
	[1]=$RPATH/TV_SHOWS
	[2]=$RPATH/MUSIC
	[3]=$RPATH/AUDIO
)

# LOOP THROUGH DIRS TO EXECUTE RSYNC
# ------------------------------------------------------------------

for index in ${!REMOTEPATH[*]}
do
	$RSYNC -avn -e "$SSH -i $KEY" $RUSER@$RHOST:${REMOTEPATH[$index]} ${LOCALPATH[$index]} 
done