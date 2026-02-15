import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        with open(self.filename, "w") as f:
            f.write("Hello World")

    def __exit__(self) -> None:
        os.remove(self.filename)
