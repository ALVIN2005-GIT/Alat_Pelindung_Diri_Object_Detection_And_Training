import subprocess
import os

def convert_to_tflite():
    model_path = "runs/train/yolov7-train/weights/best.pt"
    onnx_path = "converted_model/yolov7.onnx"
    saved_model_dir = "converted_model/tf_saved_model"
    tflite_path = "converted_model/yolov7.tflite"

    os.makedirs("converted_model", exist_ok=True)

    print("🔄 Mengonversi model ke ONNX...")
    subprocess.run(f"python export.py --weights {model_path} --grid --simplify --dynamic --onnx {onnx_path}", shell=True)

    print("🔄 Mengonversi ONNX ke TensorFlow SavedModel...")
    subprocess.run(f"python -m tf2onnx.convert --input {onnx_path} --output {saved_model_dir}", shell=True)

    print("🔄 Mengonversi TensorFlow SavedModel ke TFLite...")
    subprocess.run(f"python -c \"import tensorflow as tf; converter = tf.lite.TFLiteConverter.from_saved_model('{saved_model_dir}'); tflite_model = converter.convert(); open('{tflite_path}', 'wb').write(tflite_model)\"", shell=True)

    print(f"✅ Model berhasil dikonversi ke .tflite: {tflite_path}")

if __name__ == "__main__":
    convert_to_tflite()
