import cv2

def contour(image):
    #Convert to grayscale
    grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Clear Image
    blurred = cv2.GaussianBlur(grayscaled, (3,3), 0)

    #Canny Edge Detection
    canny_edge = cv2.Canny(blurred, 20, 100)

    #thresholding
    _, threshold = cv2.threshold(canny_edge, 127, 255, cv2.THRESH_BINARY_INV)

    # Find Contour
    image_, find, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    #Draw counters
    cv2.drawContours(image, find, -1, (0, 255, 0), 3)
    
    return image



capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    print(ret)
    cv2.imshow("Live contour", contour(frame))
    if cv2.waitKey(1) == 13:
        break

capture.release()
cv2.destroyAllWindows()