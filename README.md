# Thinkpad laptop backlight visualizer
(might work on other laptops too)

```
sudo apt-get install portaudio19-dev
python3.7 -m pip install numpy, pyaudio
sudo python3.7 main.py
```

if it throws an error then try this

```
sudo chmod 666 /sys/class/leds/tpacpi::kbd_backlight/brightness
python3.7 main.py
```

told ya its shit
