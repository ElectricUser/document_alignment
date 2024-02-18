import cv2
import numpy as np

# Substitute img src
img = cv2.imread("images/book3.png")
img_copy = img.copy()

dest_points = np.array([[0, 0], [299, 0], [299, 399], [0, 399]], dtype=float)
src_points = np.empty((4, 2), dtype=float)
idx = 0


def collect_points(event, x, y, flags, params):
    global idx
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_copy, (x, y), 5, (0, 255, 0), -1)
        src_points[idx] = [x, y]
        idx += 1
        print(src_points)



cv2.namedWindow("image align")
cv2.setMouseCallback("image align", collect_points)

while 1:
    cv2.imshow("image align", img_copy)
    if cv2.waitKey(20) == 113:
        break
    if idx == 4:
        # Calculate Homography
        homography, status = cv2.findHomography(src_points, dest_points)
        print(homography)
        # Warp source image to destination based on homography
        im_out = cv2.warpPerspective(img, homography, (300, 400))
        cv2.imwrite("images/output.png", im_out)
        break

cv2.destroyAllWindows()
