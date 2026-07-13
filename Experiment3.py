import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check if image is loaded
if img is None:
    print("Error: image.jpg not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Save the output image
    cv2.imwrite("outline_image.jpg", edges)

    print("Outline image saved successfully!")

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Outline Image", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
