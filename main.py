import os
import shutil

DOWNLOADS_FOLDER = "/path/to/your/Downloads"

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"],
}

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(file_path, dest_folder):
    create_folder(dest_folder)
    shutil.move(file_path, dest_folder)

def sort_downloads():
    for item in os.listdir(DOWNLOADS_FOLDER):
        item_path = os.path.join(DOWNLOADS_FOLDER, item)
        if os.path.isfile(item_path):
            moved = False
            for folder, extensions in EXTENSIONS.items():
                if any(item.endswith(ext) for ext in extensions):
                    move_file(item_path, os.path.join(DOWNLOADS_FOLDER, folder))
                    moved = True
                    break
            if not moved:
                move_file(item_path, os.path.join(DOWNLOADS_FOLDER, "Others"))

if __name__ == "__main__":
    sort_downloads()


