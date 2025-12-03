from pathlib import Path

image_path = Path(r"C:\TEMP\A.JPG")
image_dir = image_path.parent
image_dirname = image_path.parent.name
image_filename = image_path.name
image_stem = image_path.stem
image_ext = image_path.suffix.lower()

print(f"image_path = {image_path}")
print(f"image_dir = {image_dir}")
print(f"image_dirname = {image_dirname}")
print(f"image_filename = {image_filename}")
print(f"image_stem = {image_stem}")
print(f"image_ext = {image_ext}")