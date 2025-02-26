import zipfile

def zip_model():
    model_path = "runs/train/yolov7-train/weights/best.pt"
    tflite_path = "converted_model/yolov7.tflite"
    zip_path = "yolov7_model.zip"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(model_path, arcname="best.pt")
        zipf.write(tflite_path, arcname="yolov7.tflite")

    print(f"✅ Model berhasil dikompres: {zip_path}")

if __name__ == "__main__":
    zip_model()
