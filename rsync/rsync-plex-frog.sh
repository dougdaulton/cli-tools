#!/bin/sh

# rsync PLEX: KODIAK to FROG (TEST STRINGS)
# ------------------------------------------------------------------
# rsync -avzn -e "ssh -i /home/bayaz/cron/frog-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK4TB1/PLEX_MOVIES/ /VOLUMES/FROG4TB/PLEX/MOVIES/
# rsync -avzn -e "ssh -i /home/bayaz/cron/frog-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK4TB1/PLEX_TV/ /VOLUMES/FROG4TB/PLEX/TV_SHOWS/
# rsync -avzn -e "ssh -i /home/bayaz/cron/frog-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK2TB/PLEX_MUSIC/ /VOLUMES/FROG4TB/PLEX/MUSIC/
# rsync -avzn -e "ssh -i /home/bayaz/cron/frog-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK2TB/PLEX_AUDIOBOOKS/ /VOLUMES/FROG4TB/PLEX/AUDIOBOOKS/



# SET BASE VARIABLES
# ------------------------------------------------------------------
RSYNC=/usr/bin/rsync 
SSH=/usr/bin/ssh 
KEY=/home/bayaz/cron/frog-rsync-key
RUSER=bayaz 
RHOST=kodiak

REMOTEPATH[0]=/VOLUMES/KODIAK4TB1/PLEX_MOVIES
REMOTEPATH[1]=/VOLUMES/KODIAK4TB1/PLEX_TV
REMOTEPATH[2]=/VOLUMES/KODIAK4TB1/PLEX_MUSIC
REMOTEPATH[3]=/VOLUMES/KODIAK4TB1/PLEX_AUDIO

LOCALPATH[0]=/VOLUMES/FROG4TB/PLEX/MOVIES
LOCALPATH[1]/VOLUMES/FROG4TB/PLEX/TV_SHOWS
LOCALPATH[2]/VOLUMES/FROG4TB/PLEX/MUSIC
LOCALPATH[3]/VOLUMES/FROG4TB/PLEX/AUDIO

# LOOP THROUGH DIRS TO EXECUTE RSYNC
# ------------------------------------------------------------------

for index in ${!REMOTEPATH[*]}
do
	echo $RSYNC -avn -e "$SSH -i $KEY" $RUSER@$RHOST:$REMOTEPATH[$index] $LOCALPATH[$index] 
done