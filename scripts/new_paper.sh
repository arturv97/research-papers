#!/bin/bash

YEAR=$(date +%Y-%m-%d)

if [ -z "$1" ]; then
  echo "Usage: ./new_paper.sh filename"
  exit 1
fi

FILE="papers/$YEAR/$1.md"

mkdir -p papers/$YEAR
cp templates/paper_template.md "$FILE"

echo "Created $FILE"
