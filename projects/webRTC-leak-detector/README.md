<!--
  PERSONAL README TEMPLATE — not part of any project.
  Copy everything below the line into projects/<name>/README.md and fill the blanks.
  Delete sections you don't need. Placeholders are wrapped in <...>.
-->

---

# 🌐 WebRTC leak detector

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Progress-success.svg)

A simple tool which sniffs for unwanted WebRTC connections that are happening, WebRTC is a Peer 2 Peer connection mainly used by streaming services like discord web audio call or omegle video/audio sharing. For a Peer 2 Peer connection to work, both parties must expose their true IP to eachother or the middleservice, that means that for WebRTC to work, it must get your real IP regardless of VPN and etc, which compromises the OPSEC of someone.

---

## ✨ Features

* Monitors both **TCP** and **UDP** protocols
* Filters out **noise** from the payload
* Looks for a specific **magic cookie** that WebRTC STUN protocol uses in the payload hex code
* Alerts if a **WebRTC** connection was detected

---

## 🛠️ Setup

```bash
# from projects/WebRTC-leak-detector

# 1. Create a virtual environment
python -m venv .venv-WebRTC

# 2. Activate it
#   Windows (PowerShell)
.venv-WebRTC\Scripts\Activate.ps1
#   macOS / Linux
source .venv-WebRTC/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

Once started, the program will ask for admin rights in order to montior network packets (scapy request), then program will immediatley start looking for leaks

```
[*] initializing WebRTC sniffer...
[*] monitoring all network TCP and UDP protocols for signatures...

# When a WebRTC is detected 
[!] ALERT: WebRTC -p UDP -m STUN Handshake Detected!
   > Protocol : UDP
   > Method   : STUN
   > Direction: <source_ip> -> <destination_ip>

```

---

## 📦 Dependencies

| Package | Purpose |
| :--- | :--- |
| [`Scapy`](https://pypi.org/project/scapy/) | Montior and sniff incoming network packets |
