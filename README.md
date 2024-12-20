
# Encrypted MQTT Chat

A secure, encrypted chat application using MQTT and symmetric encryption.

---

### **Features**
- **Symmetric Encryption:** Messages are encrypted and decrypted using a shared passphrase with Fernet encryption.
- **Dynamic GUI:** graphical interface created with Tkinter.
- **MQTT Broker Settings:** Modify broker and topic settings directly from the GUI.
- **Usernames:** Personalized usernames are displayed with messages.
- **Spam Protection:** Prevents users from sending messages too quickly.
-  **File Transfer:** (Under Development, dont work right now) Allows users to send and receive files securely.

---

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/hannesassarsson/chat_project.git
   cd chat_project
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### **Usage**

1. Run the application:
   ```bash
   python3 main.py
   ```

2. Enter your username and passphrase in the login window:
   - Ensure all participants use the same passphrase for encryption.

3. Start chatting!

---

### **How it Works**

The chat application uses Fernet encryption for secure communication over MQTT. Here’s how the key functionality aligns with the requirements:

1. **Initialization with Passphrase:**
   - On application start, the user is prompted to enter a passphrase. This is used to generate a Fernet encryption key.
   - The key ensures that all messages sent and received are securely encrypted.

2. **Encryption and Decryption:**
   - Messages are encrypted before being sent to the MQTT broker.
   - Received messages are decrypted before being displayed to the user.

3. **Defensive Programming:**
   - The program includes error handling for invalid inputs, message size limits.
   - Spam protection prevents users from overflood the chat.

4. **MQTT Integration:**
   - The program connects to an MQTT broker (in this case standard is Hive, you can change this) to handle message publishing and subscribing.

---

### **File Structure**

```
chat_project/
│
├── chat/
│   ├── client.py         # Handles the chat client and GUI.
│   ├── encryption.py     # Manages encryption and decryption.
│   ├── config.py         # Stores MQTT broker and topic configurations.
│   └── __init__.py       # Marks this directory as a package.
│
├── main.py               # Entry point to launch the chat application.
├── requirements.txt      # Lists all required dependencies.
└── README.md             # Documentation for the project.
```

---

### **Security**

- **Encryption:** Messages are secured with Fernet encryption using a shared passphrase.
- **Privacy:** Only participants with the correct passphrase can decrypt the messages.

---

### **Dependencies**

- **paho-mqtt:** Handles MQTT
- **cryptography:** Provides Fernet encryption.
- **colorama:** Adds colorized output

---

### **File Transfer (Under Development)**

File transfer functionality is currently being developed. The feature will allow users to:
- Encrypt and send files securely using the same encryption mechanism as chat messages.
- Receive and decrypt files sent by other users.

However, as of now, this feature is not fully functional and are not working as intended.

-- Created by Hannes --