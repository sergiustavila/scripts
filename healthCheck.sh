#!/bin/bash

while true; do
  echo "Show date and time: "
  date

  echo "Machine uptime: "
  uptime | awk -F',' '{ print $1 }' | awk -F' ' '{ printf $2" " $3" " $4" " }'

  echo "SSD disk usage: "
  df -h | grep "/dev/nvme0n1p2" | awk -F' ' '{ print $5 }'

  echo "Hard disk usage: "
  df -h | grep "/dev/sda2" | awk -F' ' '{ print $5 }'

  echo "Memory usage: "
  free

  echo "Top 5 processes with the most used CPU: "
  top -b -o +%CPU | head -n 12

  sleep 2
done