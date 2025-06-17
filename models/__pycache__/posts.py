class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content

    def to_dict(self):
        return {
            "user": self.user,
            "content": self.content
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["user"], data["content"])