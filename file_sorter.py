import shutil
from pathlib import Path

# Defines how the files are going to be sorted and which extensions should be 
categories = {
    "Images": [".jpg",".png",".jpeg",".gif",".tif"],
    "Documents":[".doc",".docx",".txt",".pdf"],
    "Video": [".mp4", ".m4a", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Presentations": [".ppt", ".pptx", ".pptm"]
}

# Main function
def sort_files(folder_path: str):
   # Uses the exact directory given by the user
    source = Path(folder_path) 

    # Counter for how many files have been sorted
    files_moved = 0

    # Check if the provided directory actually exists. 
    if not source.exists:
        raise FileNotFoundError

    # Main loop for every item in a folder
    for file in source.iterdir():
        # Checks if the item is a file
        if file.is_file():
            
            # Goes through all categories and extensions
            for category, extensions in categories.items():
                if file.suffix.lower() in extensions:

                    # Creates a new folder if needed
                    destination = source / category
                    destination.mkdir(exist_ok=True)

                    # Moves the file in the approperiate folder
                    shutil.move(str(file), str(destination/ file.name))

                    print(f"Moved {file.name} to {category}")
                    files_moved += 1
                    break                  
    return files_moved
                
