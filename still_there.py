from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController
import time, random, math, datetime, sys, ctypes

def log(data):
	print(str(datetime.datetime.now())+" : LOG : "+data)

def rng(min, max):
	return math.ceil((random.random() * (max-min)) + min)

def alt_tab():
	time.sleep(0.5)
	keyboard.press(Key.alt_l)
	keyboard.press(Key.tab)
	time.sleep(0.5)
	keyboard.release(Key.tab)
	keyboard.release(Key.alt_l)

def tick():
	w = ctypes.windll.user32.GetSystemMetrics(0)
	h = ctypes.windll.user32.GetSystemMetrics(1)
	alt_tab()
	time.sleep(rng(1, 5))
	dx = rng(50, 200)
	mouse.position = ((w/2) + dx, h/2);
	mouse.click(Button.left)
	time.sleep(rng(1, 5))
	mouse.position = ((w/2) - dx, h/2);
	mouse.click(Button.left)
	alt_tab()


mouse = Controller()
keyboard = KeyboardController()

log("Starting in 20s")
time.sleep(20)

while(True):
	try:
		tick()
		s = rng(590, 610)
		log("ticked, sleeping for "+str(s)+"s")
		time.sleep(s)
	except KeyboardInterrupt:
		log("oh you are back")
		sys.exit(0)