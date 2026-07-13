import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check if the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Blur the image
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Save the blurred image
    cv2.imwrite("blurred_image.jpg", blur)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Blurred Image", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
