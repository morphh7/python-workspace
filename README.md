# 🐍 Python Development Workspace

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A general Python workspace and portfolio showcasing standalone projects for exploration and testing, serving as a central repository to track development progress, utilities, and application scripts.

---

## 🛠️ Prerequisites
* **Runtime:** Python `3.10` or higher.
* **Environment:** Virtual environments (`venv`) are required per project.

---

## 📂 Project Catalog

| Project | Description | Core Dependencies | Status |
| :--- | :--- | :--- | :--- |
| [NanoControl](./projects/nanocontrol) | Automated desktop assistant to handle your most tedious work | alot... | 🔵 Planned |
| [EXIF-metadata-extractor](./projects/EXIF-metadata-extractor) | Extract exif meta data info from images, it can reveal info such as location and the device it was taken on | exif, requests | 🟢 Active |
| [project-name](./projects/project_name) | One-sentence description of the project's utility | lib_1, lib_2, lib_3 | 🔵 Planned |

> 💡 **Note:** Every subdirectory within `projects/` functions as an independent application. Each contains a dedicated `README.md` detailing quick project info, feature breakdowns, isolated virtual environment setup instructions (`requirements.txt`), and CLI usage execution guides.

<!-- DO NOT REMOVE: Update the status indicators (🟢 Active, 🟡 In Progress, 🔵 Planned) and relative link paths as new modules are initialized. -->

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
    └── project_template_2/
        ├── README.md        
        ├── requirements.txt
        └── main.py