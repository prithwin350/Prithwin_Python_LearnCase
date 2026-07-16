from pathlib import Path

def generate_test_files():
    test_folder = Path("test_folder")
    test_folder.mkdir(exist_ok=True)

    files = [
        "photo1.jpg",
        "photo2.jpeg",
        "image1.png",
        "document1.pdf",
        "notes.txt",
        "song.mp3",
        "video.mp4",
        "archive.zip"
    ]

    for filename in files:
        (test_folder / filename).touch()

    print("Test files created.")

def main():
    generate_test_files()

if __name__ == "__main__":
    main()