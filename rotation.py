
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("UNP.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

tinggi, lebar = img.shape[:2]

# Menentukan titik pusat
pusat = (lebar // 2, tinggi // 2)

# Rotasi 45 derajat
M1 = cv2.getRotationMatrix2D(
    pusat, 45, 1.0
)

hasil1 = cv2.warpAffine(
    img, M1, (lebar, tinggi)
)

# Rotasi 90 derajat
M2 = cv2.getRotationMatrix2D(
    pusat, 90, 1.0
)

hasil2 = cv2.warpAffine(
    img, M2, (lebar, tinggi)
)

# Rotasi 180 derajat
M3 = cv2.getRotationMatrix2D(
    pusat, 180, 1.0
)

hasil3 = cv2.warpAffine(
    img, M3, (lebar, tinggi)
)

# Menampilkan hasil
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(hasil1)
plt.title("Rotasi 45 Derajat")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(hasil2)
plt.title("Rotasi 90 Derajat")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(hasil3)
plt.title("Rotasi 180 Derajat")
plt.axis("off")

plt.tight_layout()
plt.show()
