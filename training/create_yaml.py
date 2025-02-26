import yaml
import os

def create_yaml(classes):
    data = {
        'train': 'dataset/images/train',
        'val': 'dataset/images/val',
        'nc': len(classes),
        'names': classes
    }

    os.makedirs('../dataset', exist_ok=True)
    with open('../dataset/data.yaml', 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

    print("✅ File data.yaml berhasil dibuat!")

if __name__ == "__main__":
    create_yaml(['Glasses', 'Goggles', 'Gloves', 'Helmet', 'Safety-Vest', 'Safety_shoes', 'protective_suit', 'Person'])  # Ganti dengan kelas dataset
