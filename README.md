# Downloads Organizer
This Python script organizes files in your Downloads folder by categorizing them into subfolders based on their file types, making it easier to find files and maintain a clutter-free Downloads directory.

## How It Works
The script sorts files in the specified Downloads folder into folders according to their file extensions. It moves each file into one of the following predefined folders:

- Images: .jpg, .jpeg, .png, .gif, .bmp, .svg
- Documents: .pdf, .docx, .txt, .xlsx, .pptx
- Videos: .mp4, .mov, .avi, .mkv
- Music: .mp3, .wav, .aac
- Archives: .zip, .rar, .7z, .tar, .gz
- Scripts: .py, .js, .html, .css, .sh
- Others: Any files that don’t match the above categories
- Each file is moved to the corresponding folder, which is created automatically if it doesn’t already exist.

## Requirements
- Python 3.x
- shutil and os libraries (included in the Python standard library)

## Usage
1. Clone or Download the Repository:
```
git clone https://github.com/YosimarFlores/FileOrganizer.git
```
2. Set the Path:
- Update the DOWNLOADS_FOLDER variable in downloads_organizer.py to match the path of your Downloads folder. For example:
```
DOWNLOADS_FOLDER = "/Users/yourname/Downloads"
```
3. Run the Script:
- Run the script to organize your Downloads folder:
```
python downloads_organizer.py
```
## Function Overview
- create_folder(path): Creates a folder if it does not already exist.
- move_file(file_path, dest_folder): Moves a file to the specified destination folder.
- sort_downloads(): Main function that iterates through files in the Downloads folder, moving each file based on its extension to the appropriate category folder.

## Example
- After running the script, your Downloads folder will look like this:
```
Downloads
│
├── Images
│   ├── example.jpg
│   └── example.png
│
├── Documents
│   ├── example.pdf
│   └── example.docx
│
├── Videos
│   └── example.mp4
│
├── Music
│   └── example.mp3
│
├── Archives
│   └── example.zip
│
├── Scripts
│   └── example.py
│
└── Others
    └── example.other
```
