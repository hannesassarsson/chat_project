from chat.client import ChatClientGUI
from chat.encryption import Encryption
import tkinter as tk
from tkinter import ttk, messagebox

class ChatLauncher:
    def __init__(self):
        """
        Create a login window for the user to enter their username and passphrase.
        """
        self.root = tk.Tk()
        self.root.title("Chat Login")
        self.root.geometry("400x250")

        # Username entry
        ttk.Label(self.root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.username_entry = ttk.Entry(self.root, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Passphrase entry
        ttk.Label(self.root, text="Passphrase:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.passphrase_entry = ttk.Entry(self.root, width=30, show="*")  # Mask input
        self.passphrase_entry.grid(row=1, column=1, padx=10, pady=10)

        # Start button
        self.start_button = ttk.Button(self.root, text="Start Chat", command=self.validate_and_start_chat)
        self.start_button.grid(row=2, column=1, pady=20, sticky="e")

        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

    def validate_and_start_chat(self):
        """
        Validate user input and start the chat application if valid.
        """
        username = self.username_entry.get().strip()
        passphrase = self.passphrase_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Username cannot be empty.")
            return
        if len(username) > 50:
            messagebox.showerror("Error", "Username cannot exceed 50 characters.")
            return
        if len(passphrase) < 8:
            messagebox.showerror("Error", "Passphrase must be at least 8 characters long.")
            return

        # close the login popup and open client
        self.root.destroy()
        encryption = Encryption(passphrase)
        chat_client_gui = ChatClientGUI(username, encryption)
        chat_client_gui.run()

    def run(self):
        """
        Run the login GUI.
        """
        self.root.mainloop()


if __name__ == "__main__":
    launcher = ChatLauncher()
    launcher.run()