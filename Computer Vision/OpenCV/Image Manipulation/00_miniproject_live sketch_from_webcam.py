import cv2


def sketch(image):
    # Convert to graysclae
    grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean using Gaussian Blur
    blurred = cv2.GaussianBlur(src=grayscaled, ksize=(3, 3), sigmaX=0)

    # Detect Edge using Canny Edge Detection Algorithm
    canny_edge = cv2.Canny(blurred, 20, 35)

    # Thresholding of image
    ret, mask = cv2.threshold(canny_edge, thresh=10, maxval=255, type=cv2.THRESH_BINARY_INV)
    return mask


capture = cv2.VideoCapture(0)
while True:
    bool, frame = capture.read()
    cv2.imshow('Live Sketch', sketch(frame))
    if cv2.waitKey(1) == 13:
        break

capture.release()
cv2.destroyAllWindows()


