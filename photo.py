import cv2
import numpy as np

# Use double backslashes or raw string for file paths
image_path = r"D:\D3 Teknik Informatika\Semester 3\Praktik Sistem Keamanan Data\TUGAS SKD FULL\RSA\Photo\pexels-aron-visuals-1694621.jpg"

demo = cv2.imread(image_path, 0)
r, c = demo.shape

key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)

cv2.imshow("encryption", encryption)

# Save the images with different filenames
cv2.imwrite("D:\D3 Teknik Informatika\Semester 3\Praktik Sistem Keamanan Data\TUGAS SKD FULL\RSA\Photo\encrypted_pexels-aron-visuals-1694621.jpg", encryption)


decryption = cv2.bitwise_xor(encryption, key)

cv2.imshow("decryption", decryption)

# Save the images with different filenames
cv2.imwrite("D:\D3 Teknik Informatika\Semester 3\Praktik Sistem Keamanan Data\TUGAS SKD FULL\RSA\Photo\decrypted_pexels-aron-visuals-1694621.jpg", decryption)


cv2.waitKey(-1)
cv2.destroyAllWindows()
