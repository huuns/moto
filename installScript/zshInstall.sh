#!/bin/bash

#install 
apt-get install -y zsh
wget --no-check-certificate http://install.ohmyz.sh -O - | sh
git clone https://github.com/rupa/z



#configure 
$zshrcFile="~/.zshrc"

currentLocation=$PWD
new="$currentLocation/z/z.sh"
sed -i "$ a\
$new" $zshrcFile

old="robbyrussell"
new="dieter"
sed -i "s/$old/$new/g" $zshrcFile
