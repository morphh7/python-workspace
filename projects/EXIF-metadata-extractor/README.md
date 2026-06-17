# 📷 EXIF Metadata Extractor

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A small CLI tool that reads the EXIF metadata embedded in image files. It can surface
details such as the camera/device used, capture settings, timestamps, and — when present —
GPS coordinates, which it converts to decimal degrees and a clickable Google Maps link.

---

## ✨ Features

* Read EXIF tags from a **local image** (by path)
* Download and read EXIF from a **web image** (by URL)
* Read a **pre-downloaded** image from `./img`
* Decode GPS data into decimal coordinates + a Google Maps link

---

## 🛠️ Setup

```bash
# from projects/EXIF-metadata-extractor (navigate to the folder)

# 1. Create a virtual environment
python -m venv .venv-exif

# 2. Activate it
#   Windows (PowerShell)
.venv-exif\Scripts\Activate.ps1
#   macOS / Linux
source .venv-exif/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

You'll get an interactive menu:

```
? What do you want to do?
  1: Process local image (path)
  2: Process web image (url)
  3: Process pre-downloaded img (./img)
  q: quit app
```

Pick an option, point it at an image, and any EXIF metadata found is printed to the terminal.
Images without EXIF data are reported as such.

---

## 📦 Dependencies

| Package | Purpose |
| :--- | :--- |
| [`exif`](https://pypi.org/project/exif/) | Parse EXIF metadata from images |
| [`requests`](https://pypi.org/project/requests/) | Fetch images from a URL |
