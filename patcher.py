from python_imagesearch.imagesearch import imagesearch, click_image
import pickle
import pyautogui
import time
from subprocess import Popen
import _thread

actions = []
with open('rule.pr', 'rb') as file:
    actions = pickle.load(file)

# jalanin rule
for id, action in enumerate(actions):
    if(action['action'] == 'keyboard'):
        pyautogui.write(action['value'], interval=0.25)
    elif(action['action'] == 'image_right_click'):
        pos = imagesearch(action['value'])
        if pos[0] != -1:
            click_image(action['rgb_image'], pos, "right", 0.2, offset=5)
    elif(action['action'] == 'image_left_click'):
        pos = imagesearch(action['value'])
        if pos[0] != -1:
            click_image(action['rgb_image'], pos, "left", 0.2, offset=5)
    elif(action['action'] == 'wait'):
        time.sleep(int(action['value']))
    elif(action['action'] == 'command'):
        p = Popen([action['value']])

print("Done")

