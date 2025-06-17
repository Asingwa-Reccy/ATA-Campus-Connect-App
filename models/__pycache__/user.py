class User:
    def __init__(self, username):
        self.username = username

    def to_dict(self):
        return {
            "username": self.username
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"])