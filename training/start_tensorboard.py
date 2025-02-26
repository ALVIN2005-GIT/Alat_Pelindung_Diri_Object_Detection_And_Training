import subprocess

def start_tensorboard():
    command = "tensorboard --logdir runs/train --host=0.0.0.0 --port=6010"
    print("🚀 Jalankan perintah ini di terminal lain untuk melihat GUI TensorBoard:")
    print("   tensorboard --logdir runs/train --host=0.0.0.0 --port=6010")
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    start_tensorboard()
