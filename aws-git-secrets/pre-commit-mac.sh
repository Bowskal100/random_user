#!/usr/bin/env bash
#cd .. 
# Note that this will be invoked by the git hook from the repo root, so cd .. isn't required

# These only need to be run once per workstation but are included to try and ensure they are present
./aws-git-secrets/git-secrets --add-provider -- cat aws-git-secrets/aws-rules-linux-mac.txt

# Just scan the files changed in this commit
./aws-git-secrets/git-secrets --pre_commit_hook
