
import cv2
import matplotlib.pyplot as plt

# 1. Membaca citra
img = cv2.imread("UNP.png")

if img is None:
    raise FileNotFoundError("Gambar UNP.png tidak ditemukan!")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

tinggi, lebar = img.shape[:2]

# 2. Translation (Pergeseran)
M_translation = cv2.getRotationMatrix2D(
    (0, 0), 0, 1
)
M_translation[0, 2] = 100
M_translation[1, 2] = 50

translation = cv2.warpAffine(
    img, M_translation, (lebar, tinggi)
)

# 3. Scaling (Perubahan ukuran)
scaling_05 = cv2.resize(
    img, None, fx=0.5, fy=0.5
)

scaling_2 = cv2.resize(
    img, None, fx=2, fy=2
)

# 4. Rotation (Rotasi)
pusat = (lebar // 2, tinggi // 2)

M1 = cv2.getRotationMatrix2D(pusat, 45, 1.0)
M2 = cv2.getRotationMatrix2D(pusat, 90, 1.0)
M3 = cv2.getRotationMatrix2D(pusat, 180, 1.0)

rotasi_45 = cv2.warpAffine(img, M1, (lebar, tinggi))
rotasi_90 = cv2.warpAffine(img, M2, (lebar, tinggi))
rotasi_180 = cv2.warpAffine(img, M3, (lebar, tinggi))

# 5. Flip (Pencerminan)
horizontal_flip = cv2.flip(img, 1)
vertical_flip = cv2.flip(img, 0)

# 6. Menampilkan seluruh hasil transformasi
plt.figure(figsize=(15, 12))

gambar = [
    (img, "Citra Asli"),
    (translation, "Translation"),
    (scaling_05, "Scaling 0.5"),
    (scaling_2, "Scaling 2"),
    (rotasi_45, "Rotation 45 Derajat"),
    (rotasi_90, "Rotation 90 Derajat"),
    (rotasi_180, "Rotation 180 Derajat"),
    (horizontal_flip, "Horizontal Flip"),
    (vertical_flip, "Vertical Flip")
]

for i, (hasil, judul) in enumerate(gambar):
    plt.subplot(3, 3, i + 1)
    plt.imshow(hasil)
    plt.title(judul)
    plt.axis("off")

plt.tight_layout()
plt.show()
