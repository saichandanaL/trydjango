#!/bin/bash

# Prompt the user to enter the commit message
echo "Enter commit message:"
read commit_message

# Add and commit the changes with the specified message
git add .
git commit -m "$commit_message"

# Push the changes to the remote repository
git push
