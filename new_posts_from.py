import tkinter as tk
from tkinter import ttk
from models.post import Post
import json
import os

class NewPostForm:
    def __init__(self, parent, callback):
        self.top = tk.Toplevel(parent)
        self.top.title("New Post")
        self.callback = callback

        ttk.Label(self.top, text="User:").pack(pady=(10, 0))
        self.user_entry = ttk.Entry(self.top, width=40)
        self.user_entry.pack(pady=5)

        ttk.Label(self.top, text="Content:").pack(pady=(10, 0))
        self.content_entry = ttk.Entry(self.top, width=40)
        self.content_entry.pack(pady=5)

        ttk.Button(self.top, text="Submit", command=self.save_post).pack(pady=15)

    def save_post(self):
        user = self.user_entry.get().strip()
        content = self.content_entry.get().strip()

        if not user or not content:
            return  # Optionally show a warning message

        post = Post(user, content)

        # Load existing posts
        data = []
        if os.path.exists("data/posts.json"):
            with open("data/posts.json", "r") as f:
                data = json.load(f)

        # Append new post and save
        data.append(post.to_dict())

        with open("data/posts.json", "w") as f:
            json.dump(data, f, indent=2)

        self.callback(post)
        self.top.destroy()