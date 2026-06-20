# 🐍 Python Development Workspace

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A general Python workspace and portfolio showcasing standalone projects for exploration and testing, serving as a central repository to track development progress, utilities, and application scripts.

---

## 🛠️ Prerequisites
* **Runtime:** Python `3.10` or higher.
* **Environment:** Virtual environments (`venv`) are required per project.

> 💡 **Note:** Every subdirectory within `projects/` functions as an independent application containing a dedicated `README.md` (project info, feature breakdowns), standalone virtual environment setups (`requirements.txt`), and execution guides.

---

## 📂 Project Catalog

#### 🖥️ OSINT & Networking
* [EXIF-metadata-extractor](./projects/EXIF-metadata-extractor) : Extract metadata details from localized image files.
* [WebRTC-leak-detector](./projects/webRTC-leak-detector) : Network layer analysis to monitor for WebRTC-based IP leaks.

#### ⚙️ Automation & Desktop Utilities
* [NanoControl](./projects/nanocontrol) : Automated desktop assistant to handle your most tedious work.

#### 🫣 OPSEC & Anonymity
* [Voice-Changer](./projects/Voice-Changer) : Change your voice by writing altered voice packets and mask your voice.

---

## ⚙️ Repository Structure

```yaml
.
├── .gitignore               
├── README.md                
└── projects/                
    ├── EXIF-metadata-extractor/         
    │   ├── README.md        
    │   ├── main.py
    │   └── img/             
    │       └── palm-tree.jpg
    ├── WebRTC-leak-detector/
    │   ├── README.md        
    │   ├── requirements.txt
    │   └── main.py
    └── Voice-Changer/
        ├── README.md        
        ├── requirements.txt
        └── main.py
```

---

## ⚖️ Disclaimer

This repository exists for **educational purposes** to learn Python through small, approachable projects and tutorials, and to share that with anyone who wants to learn alongside me.

All tools here are provided **as-is**, with no warranty of any kind. They are intended only for lawful use and for inspecting data you own or have explicit permission to access.

I am **not responsible** for how anyone else chooses to use this code. By using, copying, or modifying anything in this repository, you accept full responsibility for your own actions and agree that the author is not liable for any misuse, damage, or legal consequences that result. If you use these tools, you do so at your own risk and in compliance with all applicable laws.