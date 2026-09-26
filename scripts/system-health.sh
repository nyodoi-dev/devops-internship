#!/bin/bash
echo
echo "the hostname is" $(hostname)
echo
echo "the current user is"$(whoami)
echo
echo "it is currently" $(date)
echo
echo "the private IP for the host is" $(hostname -I)
echo
echo "the default gateway is" $(ip route | awk ' {print $3}')
echo
echo "Disk usage"
 df -h
echo
echo "Memory usage"
free -h |awk {'print $3 $2'}
echo
echo "top processes"
 ps -aux | head -n 2
echo 
echo "listening ports"
 ss -tuln
