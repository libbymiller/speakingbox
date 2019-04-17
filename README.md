# Burn a card with Etcher.

(Assuming a Mac) Enable ssh

touch /Volumes/boot/ssh

# Put a wifi password in

nano /Volumes/boot/wpa_supplicant.conf

```
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
  ssid="foo"
  psk="bar"
}
```

# Put the card in the pi

eject and put it in the pi

# update

sudo apt-get update

# enable camera

sudo raspi-config # and enable camera

change name

# fix the audio

sudo nano /boot/config.txt

Disable on-board audio by commenting out dtparam=audio=on:

```
#dtparam=audio=on
dtoverlay=hifiberry-dac
```

reboot

# test audio

aplay /usr/share/sounds/alsa/Front_Center.wav

# install tensorflow

sudo apt install python3-dev python3-pip
sudo apt install libatlas-base-dev -y

sudo nano /etc/dphys-swapfile

```
CONF_SWAPSIZE=1024
```

sudo pip install virtualenv
virtualenv -p python3 env
cd env/
source bin/activate
pip3 install numpy

(lots of errors but does seem to work)

pip3 install tensorflow

# Test it

python3 -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"

# get imagenet

cd
git clone https://github.com/tensorflow/models.git
cd ~/models/tutorials/image/imagenet

and test it

python3 classify_image.py

# install openCV

pip3 install opencv-python
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install libqt4-test

test opencv

python3 -c 'import cv2; print(cv2.__version__)'

# install the pieces for talking to the camera

pip3 install imutils picamera

sudo apt-get install mplayer
sudo apt-get install libttspico-utils

# test audio file generation

/usr/bin/pico2wave -w test.wav hello | mplayer test.wav

# scp the following to your device

buttons.py
classify_image_client.py
classify_image_server.py
classify-image-client.service
classify-image-server.service
pulseaudio.service
install_pulse.sh

# install dependencies

pip3 install flask
pip3 install phatbeat
pip3 install requests

sudo cp classify-image-server.service /lib/systemd/system/classify-image-server.service
sudo systemctl enable classify-image-server.service
sudo systemctl start classify-image-server.service

# install pulse

sudo ./install.sh

reboot




