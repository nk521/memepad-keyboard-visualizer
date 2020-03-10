import pyaudio
import numpy as np
import sys
import os
import time

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

light = os.open("/sys/class/leds/tpacpi::kbd_backlight/brightness", os.O_RDWR)

def backlight(state):
    os.write(light,state)

try:
	while True:
		data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
		peak=np.average(np.abs(data))*20
		backlight(b'2') if peak >= 20000 else backlight(b'1') if 10000 <= peak < 20000 else backlight(b'0')
		time.sleep(0.01)

except:
	os.close(light)
	stream.stop_stream()
	stream.close()
	p.terminate()
	sys.exit()
