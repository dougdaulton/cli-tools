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

REMOTEPATH=("/VOLUMES/KODIAK4TB1/PLEX_MOVIES" "/VOLUMES/KODIAK4TB1/PLEX_TV" "/VOLUMES/KODIAK4TB1/PLEX_MUSIC" "/VOLUMES/KODIAK4TB1/PLEX_AUDIO")
LOCALPATH=("/VOLUMES/FROG4TB/PLEX/MOVIES" "/VOLUMES/FROG4TB/PLEX/TV_SHOWS" "/VOLUMES/FROG4TB/PLEX/MUSIC" "/VOLUMES/FROG4TB/PLEX/AUDIO")


# LOOP THROUGH DIRS TO EXECUTE RSYNC
# ------------------------------------------------------------------

for i in "${REMOTEPATH[@]}"
do
	$RSYNC -avn -e "$SSH -i $KEY" $RUSER@$RHOST:$i $LOCALPATH[@] 
done