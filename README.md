# Encrypted MQTT Chat

secure encrypted chat application using MQTT and symmetric encryption.

## Features
- **Fernet encryption:** Messages are encrypted and decrypted using a shared passphrase.
- **Dynamic GUI:** Graphical interface created with Tkinter.
- **Broker Settings:** Modify MQTT broker and topic settings directly from the GUI.
- **Username Support:** Personalized usernames displayed with messages.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hannesassarsson/chat_project.git
   navigate to chat_project folder
   pip install -r requirements.txt

## Usage
1.	Run the application: python3 main.py
2.	Enter your username and passphrase in the login window:
	    •	Ensure all participants use the same passphrase for encryption.
3. Done, start chat! 

## File Structure
    •	chat/: Contains the program and files:
	•	client.py: Handles the chat client and GUI.
	•	encryption.py: Manages encryption and decryption.
	•	config.py: Stores MQTT broker and topic configurations.
	•	main.py: Entry point to launch the chat application.
	•	requirements.txt: Lists all required dependencies.

## Security
	•	Uses Fernet encryption to secure messages.
	•	Shared passphrase ensures only authorized participants can decrypt messages.

## Dependencies
	•	paho-mqtt: Handles MQTT communication.
	•	cryptography: Provides Fernet encryption.
	•	colorama: Adds colorized terminal output for debugging.