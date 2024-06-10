#!/usr/bin/env bash

echo "Provisioning virtual machine..."

dnf update -y
dnf install -y git
dnf install -y vim
dnf install -y wget
dnf install -y fastfetch
dnf group install -y "MATE Desktop"
dnf group install -y "MATE Applications"
localectl set-keymap de
localectl set-x11-keymap de
systemctl set-default graphical.target

fastfetch
echo "Please reboot the virtual machine to complete the installation."