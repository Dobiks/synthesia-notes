import cv2
import os

SAVE_DIR = 'frames'

for f in os.listdir(SAVE_DIR):
    os.remove(os.path.join(SAVE_DIR, f))

vid_name = 'video.mp4'
vidcap = cv2.VideoCapture(vid_name)
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite(f"{SAVE_DIR}/{count}.jpg", image)
    success, image = vidcap.read()
    count += 1
print('Total frames: ', count)
