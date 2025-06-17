import tkinter as tk
from tkinter import ttk
from gui.new_post_form import NewPostForm
from models.post import Post
import json

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("InstaCampus")
        self.root.geometry("600x600")

        self.posts_frame = ttk.Frame(self.root)
        self.posts_frame.pack(fill=tk.BOTH, expand=True)

        self.load_posts()

        btn = ttk.Button(self.root, text="+ New Post", command=self.open_new_post_form)
        btn.pack(pady=10)

    def load_posts(self):
        try:
            with open("data/posts.json", "r") as f:
                posts = json.load(f)
            for post_data in posts:
                post = Post(**post_data)
                self.display_post(post)
        except FileNotFoundError:
            pass

    def display_post(self, post):
        post_label = ttk.Label(self.posts_frame, text=f"{post.user}: {post.content}", wraplength=500)
        post_label.pack(pady=5, anchor="w")

    def open_new_post_form(self):
        NewPostForm(self.root, self.display_post)