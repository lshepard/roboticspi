#!/bin/bash

# install dependencies
sudo apt-get update
sudo apt-get install -y libav-tools

# move streaming command to PATH
cp ./twstream /home/pi/twstream
cp ./start_tw_stream /home/pi/start_tw_stream

# setup systemd service
sudo cp ./twstream.service /lib/systemd/system/twstream.service
# set the service to start on boot
sudo systemctl enable twstream.service

# setup ngrok auth and config
mkdir ~/.ngrok2
cp ./ngrok.yml ~/.ngrok2/ngrok.yml

