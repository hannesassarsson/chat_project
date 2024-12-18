# Encrypted MQTT Chat

A simple encrypted chat application using MQTT and symmetric encryption.

## Features
- Encrypt and decrypt messages with Fernet encryption.
- Username support.
- Simple and secure communication over MQTT.

## Installation
1. Clone the repository: git clone https://github.com/hannesassarsson/chat_project.git

2. Install dependencies: pip install -r requirements.txt

## Usage
Run the application: python main.py

Enter your username and passphrase. Ensure all participants use the same passphrase.

## File Structure
- `chat/`: Contains the main functionality split into modules.
- `main.py`: Entry point to the application.
- `requirements.txt`: Dependency list.

## Dependencies
- `paho-mqtt`
- `cryptography`
- `colorama`