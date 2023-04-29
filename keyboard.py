import cv2
import pandas as pd

def mouse_callback(event, x, y, flags, param):
    global coords, click_count

    if event == cv2.EVENT_LBUTTONDOWN:
        if click_count == 0:
            coords[0] = (x, y)
            click_count += 1
        elif click_count == 1:
            coords[1] = (x, y)
            click_count += 1


starting_frame = 120
img = cv2.imread(f"frames/{starting_frame}.jpg")

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

coords = [(0, 0), (0, 0)]
click_count = 0

while click_count < 2:
    cv2.imshow('image', img)
    cv2.waitKey(1)

df = pd.DataFrame(coords, columns=['x', 'y'])
df.to_csv('coords.csv', index=False)

cv2.destroyAllWindows()
