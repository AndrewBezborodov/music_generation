sudo apt-get install libatlas-base-dev libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo nano /etc/pulse/daemon.conf - https://bbs.archlinux.org/viewtopic.php?id=185736
sudo python3 render_midi.py 
https://github.com/waveshare/WM8960-Audio-HAT/issues/19 - sudo raspi-config
sudo nano /usr/share/alsa/alsa.conf

START
cd Documents/music_generation/
source venv/bin/activate
sudo python3 render_midi.py


# INSTALL PYAUDIO
sudo apt-get install libatlas-base-dev libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev
pip3 install PyAudio

# USB sucess
sudo nano /etc/udev/rules.d/99-garmin.rules
HERE:
SUBSYSTEM == "usb", ATTR{idVendor} == "0582", ATTR{idProduct} == "0156", MODE = "666"

sudo udevadm trigger
