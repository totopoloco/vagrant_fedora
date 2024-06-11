#!/usr/bin/env bash

# Check if the script was run with an argument
if [ $# -eq 1 ]; then
    SUDO="sudo"
    IS_SUDO="yes"
else
    SUDO=""
    IS_SUDO="no"
fi

echo "Provisioning virtual machine..."
echo "Are we needing to use sudo? $IS_SUDO"

#Start by updating the package list
#and installing some basic packages
$SUDO dnf update -y
$SUDO dnf install -y git
$SUDO dnf install -y vim
$SUDO dnf install -y wget
$SUDO dnf install -y fastfetch

#Install the development tools need to create rpms
$SUDO dnf install -y gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools

#Install the MATE desktop environment for Fedora and the MATE applications for Fedora.
#This will take a while and will require a lot of disk space.
$SUDO dnf group install -y "MATE Desktop"
$SUDO dnf group install -y "MATE Applications"

#Set the keyboard layout to German
$SUDO localectl set-keymap de
$SUDO localectl set-x11-keymap de
#Uncomment the following line to enable the graphical login
#systemctl set-default graphical.target

#Display some system information after the end of the installation
fastfetch

#A message to the user to reboot the virtual machine
echo "Please reboot the virtual machine to complete the installation."