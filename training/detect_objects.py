import subprocess

def detect_objects():
    command = "python detect.py --weights runs/train/yolov7-train/weights/best.pt --img 640 --source dataset/images/val"
    subprocess.run(command, shell=True)
    print("✅ Deteksi selesai! Lihat hasil di folder runs/detect/")

if __name__ == "__main__":
    detect_objects()
