# ESPRecon

A PC-controlled ESP8266/ESP32 hardware toolkit for security research, wireless analysis and electronics experiments.

## Overview

ESPRecon is a portable hardware toolkit built around the idea of using an ESP board as a remote hardware module controlled entirely from a computer.

Unlike standalone ESP firmware projects, ESPRecon uses a Python-based command interface on the PC side. The computer acts as the main controller, while the ESP device handles hardware operations through a serial connection using **PySerial**.

```
+----------------+
|   PC / Laptop  |
| Python Console |
+-------+--------+
        |
        | USB Serial (PySerial)
        |
+-------v--------+
| ESP8266/ESP32  |
| Hardware Node  |
+-------+--------+
        |
        +---- WiFi
        +---- IR
        +---- NRF24
        +---- Sub-GHz
        +---- GPIO
```

The project is designed for learning, experimentation, wireless analysis and embedded development.

---

# Features

## WiFi Module

Current features:

- WiFi network scanner
- SSID detection
- BSSID detection
- Signal strength (RSSI)
- Channel information
- Encryption type detection
- WiFi spectrum/channel analyzer

Planned features:

- Advanced WiFi scanning tools
- Beacon testing features
- Evil Portal (for authorized security testing and education)

---

## Sub-GHz Module

Support for Sub-GHz wireless experiments.

Planned:

- Frequency analysis
- Signal testing
- External radio modules support

---

## NRF24 Module

Support for NRF24L01 wireless modules.

Planned:

- Wireless communication experiments
- Packet analysis
- NRF24 utilities

---

## Infrared Module

IR transmitter and receiver support.

Features:

- IR signal receiving
- IR signal transmitting
- Remote control experiments
- Custom IR commands

---

## Hardware

Current hardware:

- Wemos D1 Mini (ESP8266)
- ESP32 support planned
- IR transmitter
- IR receiver
- NRF24L01 module
- Sub-GHz module
- 2 status LEDs
- Serial USB connection

---

# Software

## PC Side

Written in Python.

Libraries:

- PySerial - communication with ESP
- Colorama - terminal interface colors
- PyFiglet - ASCII interface

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## ESP Firmware

The ESP firmware is written in Arduino C++.

Communication:

```
Baud rate: 115200
Protocol: Serial commands
```

Example:

Python sends:

```
scanapp
```

ESP executes the command and returns:

```
SSID: Example_WiFi
RSSI: -45 dBm
Channel: 6

END
```

---

# Project Structure

```
ESPRecon/

├── python/
│   ├── main.py
│   └── requirements.txt
│
├── firmware/
│   └── esp_firmware.ino
│
├── docs/
│
└── README.md
```

---

# Roadmap

## Completed

✅ Python control interface  
✅ Automatic ESP serial detection  
✅ WiFi scanner  
✅ WiFi channel analyzer  
✅ IR transmitter/receiver support  

## Planned

⬜ ESP32 support  
⬜ NRF24 tools  
⬜ Sub-GHz tools  
⬜ More WiFi analysis features  
⬜ Web interface  
⬜ Portable enclosure  

---

# Purpose

This project was created for:

- Learning embedded systems
- Understanding wireless technologies
- Experimenting with ESP boards
- Building a portable electronics toolkit

Use only on your own devices and networks or with proper authorization.

---

# Author

Created by **President**
