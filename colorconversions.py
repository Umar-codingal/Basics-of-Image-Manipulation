import cv2
import matplotlib.pyplot as plt

image= cv2.imread('Flowers.png')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale image")
plt.show()


cropped_image = image[100:400, 100:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)
plt.title("Cropped image")
plt.show()