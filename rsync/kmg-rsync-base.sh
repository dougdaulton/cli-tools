#!/bin/sh

# MASTER RSYNC SCRIPT FOR THE KMG ENVIRONMENT
# ------------------------------------------------------------------
# Uncomment the rsync commands required by the given box



# rsync PLEX: DROBO5N to KODIAK
# ------------------------------------------------------------------
# rsync -avzn /VOLUMES/KMGN801/PLEX/Movies/ /VOLUMES/KODIAK4TB1/PLEX_MOVIES/

# rsync -avzn /VOLUMES/KODIAK4TB1/PLEX_MOVIES/ /VOLUMES/KMGN801/PLEX/Movies/



# rsync PLEX: KODIAK to TIGER
# ------------------------------------------------------------------

# rsync -avzn -e "ssh -i /home/bayaz/cron/tiger-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK4TB1/PLEX_MOVIES/ /VOLUMES/TIGER4TB/PLEX/MOVIES/
# rsync -avzn -e "ssh -i /home/bayaz/cron/tiger-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK4TB1/PLEX_TV/ VOLUMES/TIGER4TB/PLEX/TV_SHOWS/
# rsync -avzn -e "ssh -i /home/bayaz/cron/tiger-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK2TB/PLEX_MUSIC/ /VOLUMES/TIGER4TB/PLEX/MUSIC/
# rsync -avzn -e "ssh -i /home/bayaz/cron/tiger-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK2TB/PLEX_AUDIOBOOKS/ /VOLUMES/TIGER4TB/PLEX/AUDIOBOOKS/



# rsync PLEX: KODIAK to FROG
# ------------------------------------------------------------------
# rsync -avzn -e "ssh -i /home/bayaz/cron/frog-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK4TB1/PLEX_MOVIES/ /VOLUMES/FROG4TB/PLEX/MOVIES/
# rsync -avzn -e "ssh -i /home/bayaz/cron/frog-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK4TB1/PLEX_TV/ /VOLUMES/FROG4TB/PLEX/TV_SHOWS/
# rsync -avzn -e "ssh -i /home/bayaz/cron/tiger-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK2TB/PLEX_MUSIC/ /VOLUMES/FROG4TB/PLEX/MUSIC/
# rsync -avzn -e "ssh -i /home/bayaz/cron/tiger-rsync-key" bayaz@KODIAK:/VOLUMES/KODIAK2TB/PLEX_AUDIOBOOKS/ /VOLUMES/FROG4TB/PLEX/AUDIOBOOKS/


# rsync OTHER TOOLS
# ------------------------------------------------------------------
# find . "-name" ".DS_Store" -exec rm {} \;
