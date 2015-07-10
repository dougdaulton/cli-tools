#!/bin/bash

# rsync-plex.sh
# ------------------------------------------------------------------
# 
# This script is used to sync/backup media directories from a central 
# PLEX server. Run via crontab once a day, in the early AM hours.
#
# Run the script from the PLEX sattelite (LOCAL), which pulls from 
# the central PLEX server (REMOTE).  Pass variables accordingly.


# RUNNING THE SCRIPT
# ------------------------------------------------------------------

# From the BASH shell

# bash rsync-plex.sh sync-key REMOTEUSER REMOTEHOST LOCALHOST

# From Cron

# 0 0 * * * rsync-plex.sh rsync-key REMOTEUSER REMOTEHOST LOCALHOST


# SET BASE VARIABLES
# ------------------------------------------------------------------
RUSER=$rsync-key[1]
RHOST=$rsync-key[2]
LDRIVE=echo ${rsync-key[3]^^}4TB

RSYNC=/usr/bin/rsync 
SSH=/usr/bin/ssh 
KEY=/home/${RUSER}/cron/${REMOTE}-rsync-key
LPATH=/VOLUMES/${LDRIVE}/PLEX

REMOTEPATH=(
	[0]=/VOLUMES/KODIAK4TB1/PLEX_MOVIES
	[1]=/VOLUMES/KODIAK4TB1/PLEX_TV
	[2]=/VOLUMES/KODIAK2TB/PLEX_MUSIC
	[3]=/VOLUMES/KODIAK2TB/PLEX_AUDIO
)

LOCALPATH=(
	[0]=$LPATH/MOVIES
	[1]=$LPATH/TV_SHOWS
	[2]=$LPATH/MUSIC
	[3]=$LPATH/AUDIO
)

# LOOP THROUGH DIRS TO EXECUTE RSYNC
# ------------------------------------------------------------------

for index in ${!REMOTEPATH[*]}
do
	$RSYNC -avn -e "$SSH -i $KEY" $RUSER@$RHOST:${REMOTEPATH[$index]} ${LOCALPATH[$index]} 
done