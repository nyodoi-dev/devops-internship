#!/bin/bash
if [ -z "$1" ]; then 
   echo "no dir was provided"
   exit 1
fi

dir=$1
if [ ! -d "$dir" ]; then
  echo "dir not found"
  exit 1
fi

date=$(date +"%Y%m%d_%H%M%S")

backup="backups/backup_${date}.tar.gz"

tar -czvf "$backup" "$dir"
if [ $? -eq 0 ]; then
   echo "Success"
else
   echo "Error"
   exit 1
fi
