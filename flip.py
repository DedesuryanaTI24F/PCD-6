
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("UNP.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Horizontal Flip
hasil1 = cv2.flip(img, 1)

# Vertical Flip
hasil2 = cv2.flip(img, 0)

# Menampilkan hasil
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(hasil1)
plt.title("Horizontal Flip")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(hasil2)
plt.title("Vertical Flip")
plt.axis("off")

plt.show()
