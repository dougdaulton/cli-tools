#!/bin/bash

# rsync-plex-source.sh
# ------------------------------------------------------------------
# 
# This will be a script that only manages rsync from the original 
# master to the new master.

# RUNNING THE SCRIPT
# ------------------------------------------------------------------

# From the BASH shell

# bash rsync-plex-master.sh sync-key REMOTEUSER REMOTEHOST LOCALHOST

# PLAN TO MAP TO AN ALIAS ON THE BOX



# Clean up any hidden files we dou not need in the source
# ------------------------------------------------------------------

find . -name '*.DS_Store' -type f -delete
find . -name '*._*' -type f -delete

# Execute A Dry Run
# ------------------------------------------------------------------
rsync -avn /VOLUMES/KMGN801/PLEX/Movies/ /VOLUMES/KODIAK4TB1/PLEX_MOVIES/

# Execute Sync if Dry Run is OK
# ------------------------------------------------------------------
rsync -av /VOLUMES/KMGN801/PLEX/Movies/ /VOLUMES/KODIAK4TB1/PLEX_MOVIES/


# ASK FOR PUSH TO REMOTES. EXECUTE IF CONFIRMED
# ------------------------------------------------------------------
rsync -av /VOLUMES/KMGN801/PLEX/Movies/ /VOLUMES/KODIAK4TB1/PLEX_MOVIES/