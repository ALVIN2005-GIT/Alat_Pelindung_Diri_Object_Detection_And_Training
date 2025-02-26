import os
import shutil
import random

def split_dataset(image_dir, label_dir, train_ratio=0.8):
    images = [img for img in os.listdir(image_dir) if img.endswith('.jpg')]

    # 🔍 Debug: Pastikan file gambar ditemukan
    print(f"📂 Path absolute: {os.path.abspath(image_dir)}")
    print(f"📂 Ditemukan {len(images)} file gambar di {image_dir}: {images[:5]} ...")

    if not images:
        print("⚠️ Tidak ada gambar yang ditemukan! Periksa kembali path raw_dataset.")
        return

    random.shuffle(images)

    train_size = int(len(images) * train_ratio)
    train_images = images[:train_size]
    val_images = images[train_size:]

    # 📌 Simpan dataset di `yolov7/dataset/`
    yolov7_path = os.path.abspath(os.path.join(os.getcwd(), ".."))  # Arahkan ke `yolov7/`
    output_path = os.path.join(yolov7_path, "dataset")

    os.makedirs(os.path.join(output_path, "images/train"), exist_ok=True)
    os.makedirs(os.path.join(output_path, "images/val"), exist_ok=True)
    os.makedirs(os.path.join(output_path, "labels/train"), exist_ok=True)
    os.makedirs(os.path.join(output_path, "labels/val"), exist_ok=True)

    for img in train_images:
        shutil.move(os.path.join(image_dir, img), os.path.join(output_path, "images/train", img))
        shutil.move(os.path.join(label_dir, img.replace('.jpg', '.txt')), os.path.join(output_path, "labels/train", img.replace('.jpg', '.txt')))

    for img in val_images:
        shutil.move(os.path.join(image_dir, img), os.path.join(output_path, "images/val", img))
        shutil.move(os.path.join(label_dir, img.replace('.jpg', '.txt')), os.path.join(output_path, "labels/val", img.replace('.jpg', '.txt')))
    
    print(f"✅ Dataset dibagi: {len(train_images)} training, {len(val_images)} validasi. Disimpan di {output_path}.")

if __name__ == "__main__":
    split_dataset("../raw_dataset/images", "../raw_dataset/labels")
