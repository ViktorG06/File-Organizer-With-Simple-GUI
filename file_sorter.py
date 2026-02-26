import shutil
from pathlib import Path

categories = {
    "Images": [".jpg",".png",".jpeg",".gif",".tif"],
    "Documents":[".doc",".docx",".txt",".pdf"],
    "Video": [".mp4", ".m4a", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Presentations": [".ppt", ".pptx", ".pptm"]
}

def sort_files(folder_path: str):
    source = Path(folder_path) # Ask user for exact directory
    files_moved = 0

    if not source.exists:
        raise FileNotFoundError

    for file in source.iterdir():

        if file.is_file():
            
            for category, extensions in categories.items():

                if file.suffix.lower() in extensions:

                    destination = source / category
                    destination.mkdir(exist_ok=True)

                    shutil.move(str(file), str(destination/ file.name))

                    print(f"Moved {file.name} to {category}")
                    files_moved += 1
                    break                  
    return files_moved
                