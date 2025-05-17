from pathlib import Path

# Set your folder
root = Path("/content/drive/MyDrive/TMN/Maahi")

# Collect all image files (you can add more extensions if needed)
image_files = sorted([f for f in root.rglob("*") if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"]])

# Rename them sequentially
for idx, f in enumerate(image_files, start=1):
    new_name = f"Maahi_{idx}.jpg"
    new_path = f.with_name(new_name)
    
    try:
        f.rename(new_path)
        print(f"✓ Renamed: {f.name} → {new_name}")
    except Exception as e:
        print(f"✗ Failed to rename {f.name}: {e}")
