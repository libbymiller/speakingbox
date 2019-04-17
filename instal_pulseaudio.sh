#!/bin/bash
set -e
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi


echo "*** Pulse Audio"
apt-get install pulseaudio -y

echo "*** Pulse Audio system mode"
adduser pi pulse
sed -i '/load-module module-native-protocol-unix/c load-module\ module-native-protocol-unix auth-anonymous=1\ socket=/tmp/pulseaudio-system.sock\nload-module module-native-protocol-tcp auth-anonymous=1 auth-ip-acl=127.0.0.1;192.168.178.0/24' /etc/pulse/system.pa
mkdir -p /home/pi/.config/pulse/
echo "default-server = unix:/tmp/pulseaudio-system.sock" >> /home/pi/.config/pulse/client.conf
chown -R pi:pi /home/pi/.config/pulse/
cp pulseaudio.service /etc/systemd/system/
systemctl enable pulseaudio
systemctl start pulseaudio

#echo "Update complete, please reboot to continue"
