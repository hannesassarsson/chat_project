import paho.mqtt.client as mqtt
from chat.encryption import Encryption
from chat.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
from colorama import Fore, Style

class ChatClient:
    def __init__(self, username, encryption: Encryption):
        self.username = username
        self.encryption = encryption
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(Fore.GREEN + "Connected to MQTT Broker." + Style.RESET_ALL)
            client.subscribe(MQTT_TOPIC)
        else:
            print(Fore.RED + f"Failed to connect, return code {rc}." + Style.RESET_ALL)

    def on_message(self, client, userdata, msg):
        try:
            decrypted_message = self.encryption.decrypt(msg.payload)
            print(Fore.YELLOW + f"Received: {decrypted_message}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Failed to decrypt message: The message may be corrupted or the key is incorrect." + Style.RESET_ALL)

    def send_message(self, message):
        if not message.strip():
            print(Fore.RED + "Message cannot be empty." + Style.RESET_ALL)
            return
        full_message = f"{self.username}: {message}"
        encrypted_message = self.encryption.encrypt(full_message)
        self.client.publish(MQTT_TOPIC, encrypted_message)
        print(Fore.GREEN + "Message sent successfully." + Style.RESET_ALL)

    def run(self):
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.loop_start()
        try:
            print(Fore.CYAN + "Chat is running! Type 'exit' to quit." + Style.RESET_ALL)
            while True:
                message = input("You: ")
                if message.lower() == "exit":
                    break
                self.send_message(message)
        finally:
            self.client.loop_stop()
            self.client.disconnect()
            print(Fore.CYAN + "Chat has been terminated." + Style.RESET_ALL)