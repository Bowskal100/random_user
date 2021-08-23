#!/usr/bin/env bash
 
# cd ..

export PATH=$PATH:.

# # These only need to be run once per workstation/slave/agent but are included to try and ensure they are present
./git-secrets --register-history
./git-secrets --add-provider -- cat aws-git-secrets/aws-rules-linux-mac.txt

# Scan all files within this repo for this commit
./git-secrets --scan
