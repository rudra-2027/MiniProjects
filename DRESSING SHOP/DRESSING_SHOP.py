f = open("C:\\Users\\rudra\\Downloads\\image_ids_and_rotation.csv","r")
import cv2
import numpy as np

# Path to your CSV file containing image data
csv_file_path = "C:\\Users\\rudra\\Downloads\\image_ids_and_rotation.csv"

# Load data from CSV file
data = np.genfromtxt(csv_file_path, delimiter=',')

# Reshape data to image dimensions (assuming the image is grayscale)
image_data = data.reshape((200, 300))  # Replace height and width with actual values

# Convert data to uint8 for image display
image_data = image_data.astype(np.uint8)

# Display the image using OpenCV
cv2.imshow("Image", image_data)
cv2.waitKey(0)
cv2.destroyAllWindows()
