import cv2
import numpy as np

# Fungsi untuk mendeteksi warna
def detect_color(frame):
    # Mengubah gambar ke ruang warna HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rentang warna untuk deteksi
    colors = {
        "Merah": ([0, 100, 100], [10, 255, 255]),
        "Hijau": ([40, 100, 100], [80, 255, 255]),
        "Biru": ([100, 100, 100], [140, 255, 255]), 
        "Kuning": ([20, 100, 100], [30, 255, 255])
    }

    for color_name, (lower, upper) in colors.items():
        lower_color = np.array(lower)
        upper_color = np.array(upper)

        # Membuat mask untuk warna
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Menemukan kontur
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Mengabaikan kontur kecil
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(f"Warna terdeteksi: {color_name}")  # Output warna yang terdeteksi

    return frame

# Fungsi utama
def main():
    cap = cv2.VideoCapture(0)  # Menggunakan kamera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Deteksi warna
        frame = detect_color(frame)

        # Menampilkan hasil
        cv2.imshow('Deteksi Warna', frame)

        # Keluar jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
