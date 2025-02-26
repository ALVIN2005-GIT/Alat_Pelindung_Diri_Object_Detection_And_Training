import subprocess
import os
import sys

def train_yolov7(epochs=5, batch_size=2, img_size=640, resume=False):
    yolov7_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Folder utama YOLOv7
    train_script = os.path.join(yolov7_dir, "train.py")  # Pastikan train.py ada
    weights_dir = os.path.join(yolov7_dir, "runs/train/yolov7-train/weights")  # Folder penyimpanan model
    weights_last = os.path.join(weights_dir, "last.pt")  # Path model terakhir
    weights_best = os.path.join(weights_dir, "best.pt")  # Path model terbaik
    data_yaml = os.path.join(yolov7_dir, "dataset/data.yaml")  # Path dataset
    weights_init = os.path.join(yolov7_dir, "yolov7.pt")  # Model awal
    hyp_path = os.path.join(yolov7_dir, "data/hyp.scratch.p5.yaml")  # Hyperparameter

    # 🛑 Cek jika ingin resume tetapi last.pt tidak ada
    if resume and not os.path.exists(weights_last):
        print("❌ ERROR: Tidak ada `last.pt`, tidak bisa melanjutkan training!")
        sys.exit(1)

    # ✅ Perintah untuk training baru atau resume
    if resume:
        command = f"python {train_script} --resume --device cpu"
        print("🔄 Melanjutkan training dari checkpoint terakhir...\n")
    else:
        print("🚀 Memulai training YOLOv7 dari awal di CPU...\n")
        command = (
            f"python {train_script} --workers 0 --device cpu --batch-size {batch_size} "
            f"--epochs {epochs} --img-size {img_size} --data {data_yaml} --weights {weights_init} "
            f"--hyp {hyp_path} --name yolov7-train --project {os.path.join(yolov7_dir, 'runs/train')} "
            f"--exist-ok --noautoanchor --save_period 1"
        )

    # 🔄 Jalankan perintah training
    subprocess.run(command, shell=True)

    # ✅ Cek apakah model berhasil disimpan
    if os.path.exists(weights_last):
        print(f"✅ Model terakhir ditemukan: {weights_last}")
    else:
        print("❌ WARNING: `last.pt` tidak ditemukan setelah training!")

    if os.path.exists(weights_best):
        print(f"🏆 Model terbaik ditemukan: {weights_best}")
    else:
        print("❌ WARNING: `best.pt` tidak ditemukan setelah training!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train YOLOv7 on CPU with optional resume")
    parser.add_argument("--resume", action="store_true", help="Lanjutkan training dari checkpoint terakhir")
    args = parser.parse_args()

    train_yolov7(resume=args.resume)
