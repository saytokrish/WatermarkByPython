import cv2
import numpy as np

# Load the base image
image = cv2.imread('example_image.jpg', cv2.IMREAD_GRAYSCALE)
watermark = "SecretKey"  # Sample watermark text

# Perform DCT on the image
dct_image = cv2.dct(np.float32(image))

# Embed watermark by modifying DCT coefficients
for i, char in enumerate(watermark):
    dct_image[0, i] += ord(char)  # Add ASCII value of each character

# Perform inverse DCT to get the watermarked image
watermarked_image = cv2.idct(dct_image)

# Save the watermarked image
cv2.imwrite('invisibly_watermarked_image.jpg', np.uint8(watermarked_image))
