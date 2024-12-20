import paho.mqtt.client as mqtt
from chat.encryption import Encryption
from chat.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json


class ChatClientGUI:
    def __init__(self, username, encryption: Encryption):
        """
        Initialize the chat application with MQTT and GUI components.
        """
        self.username = username
        self.encryption = encryption
        self.active_users = set()  # track avtive users

        # MQTT setup
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # GUI setup
        self.root = tk.Tk()
        self.root.title("MQTT Chat")
        self.root.geometry("800x600")
        self.setup_gui()

    def setup_gui(self):
        """
        Set up the main GUI layout and components.
        """
        # Chat Display
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled', width=60, height=25, bg="#f9f9f9", fg="black")
        self.chat_display.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Message Entry
        self.message_entry = tk.Entry(self.root, width=50, bg="#fff", fg="black")
        self.message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.message_entry.bind("<Return>", lambda event: self.send_message())

        # Send Button
        self.send_button = ttk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Active users counter
        self.active_users_label = ttk.Label(self.root, text="Active Users: 0", font=("Helvetica", 12))
        self.active_users_label.grid(row=0, column=1, padx=10, pady=5, sticky="n")

        # Active Users List
        self.user_list = tk.Listbox(self.root, height=25, bg="#f0f0f0", fg="black", selectmode=tk.SINGLE)
        self.user_list.grid(row=0, column=1, padx=10, pady=5, sticky="n")

        # Settings button
        self.settings_button = ttk.Button(self.root, text="Settings", command=self.show_settings)
        self.settings_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def append_message(self, message):
        """
        Append a message to the chat display.
        """
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def update_user_list(self, username):
        """
        Add a new user to the active users list and update the user count.
        """
        if username not in self.active_users:
            self.active_users.add(username)
            self.user_list.insert(tk.END, username)
            self.active_users_label.config(text=f"Active Users: {len(self.active_users)}")

    def send_message(self):
        """
        Encrypt and send a message to the MQTT topic.
        """
        message = self.message_entry.get().strip()
        if not message:
            self.append_message("Message cannot be empty.")
            return

        if len(message) > 200:
            self.append_message("Message cannot exceed 200 characters.")
            return

        full_message = {
            "username": self.username,
            "text": message
        }
        encrypted_message = self.encryption.encrypt(json.dumps(full_message))
        self.client.publish(MQTT_TOPIC, encrypted_message)
        self.append_message(f"You: {message}")
        self.message_entry.delete(0, tk.END)

    def on_connect(self, client, userdata, flags, rc):
        """
        Handle connection to the MQTT broker.
        """
        if rc == 0:
            self.append_message("Connected to MQTT Broker.")
            client.subscribe(MQTT_TOPIC)
        else:
            self.append_message(f"Failed to connect, return code {rc}.")

    def on_message(self, client, userdata, msg):
        """
        Handle incoming messages, decrypt them, and display them in the chat.
        """
        try:
            decrypted_message = self.encryption.decrypt(msg.payload)
            message_data = json.loads(decrypted_message)
            self.append_message(f"{message_data['username']}: {message_data['text']}")
            self.update_user_list(message_data['username'])
        except Exception:
            self.append_message("Failed to decrypt or parse the message. It may be corrupted or the key is incorrect.")

    def show_settings(self):
        """
        this shows a popup to change broker and topic
        """
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x200")

        ttk.Label(settings_window, text="MQTT Broker:").grid(row=0, column=0, padx=10, pady=10)
        broker_entry = ttk.Entry(settings_window, width=30)
        broker_entry.insert(0, MQTT_BROKER)
        broker_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(settings_window, text="MQTT Topic:").grid(row=1, column=0, padx=10, pady=10)
        topic_entry = ttk.Entry(settings_window, width=30)
        topic_entry.insert(0, MQTT_TOPIC)
        topic_entry.grid(row=1, column=1, padx=10, pady=10)

        def save_settings():
            global MQTT_BROKER, MQTT_TOPIC
            MQTT_BROKER = broker_entry.get()
            MQTT_TOPIC = topic_entry.get()
            messagebox.showinfo("Settings", "Settings updated!")
            settings_window.destroy()

        ttk.Button(settings_window, text="Save", command=save_settings).grid(row=2, column=1, pady=20)

    def on_close(self):
        """
        Handle GUI window closing.
        """
        self.client.loop_stop()
        self.client.disconnect()
        self.root.destroy()

    def run(self):
        """
        Start the MQTT client and GUI main loop.
        """
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.loop_start()
        self.root.mainloop()