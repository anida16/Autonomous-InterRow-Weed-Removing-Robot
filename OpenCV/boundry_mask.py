# Import required packages:
import cv2

# Load the image and convert it to grayscale:
image = cv2.imread("test_image.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply cv2.threshold() to get a binary image
ret, thresh = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

# Find contours:
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Draw contours:
cv2.drawContours(image, contours, 0, (0, 255, 0), 2)

# Calculate image moments of the detected contour
M = cv2.moments(contours[0])
print(M)

# Print center (debugging):
print("center X : '{}'".format(round(M['m10'] / M['m00'])))
print("center Y : '{}'".format(round(M['m01'] / M['m00'])))



# Draw a circle based centered at centroid coordinates
cv2.circle(image, (int(round(M['m10']) / M['m00']), int(round(M['m01'] / M['m00']))), 5, (0, 255, 0), -1)

# Show image:

cv2.imshow("outline contour & centroid", image)
cv2.imshow("Threshold",thresh)

# Wait until a key is pressed:
cv2.waitKey(0)

# Destroy all created windows:
cv2.destroyAllWindows()