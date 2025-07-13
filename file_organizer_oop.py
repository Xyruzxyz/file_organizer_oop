import os
import shutil

#Ask where is the file that you want to organize
#This is the mother class that will organize files based on their extensions
class FileOrganizer:
    def __init__ (self, path):
        self.path = path
        self.files = os.listdir(path)

    def organize(self):
        for file in self.files:
            full_path = os.path.join(self.path, file)
            # Abstraction: only process files (not folders)
            if os.path.isfile(full_path):
                self._organize_file(file)

    def _organize_file(self, file):
        filename, file_extension = os.path.splitext(file)
        extension = file_extension[1:] # Remove the leading dot
        if extension == '':
            extension = "no_extension"
        folder_path = os.path.join(self.path, extension)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        shutil.move(
            os.path.join(self.path, file),
            os.path.join(folder_path, file)         
        )
        print(f"Moved {file} to {folder_path}")
        
#Next is create a subclass that will handle specific file types
class ImageOrganizer(FileOrganizer):
    def _organize_file(self, file):
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            super()._organize_file(file)

if __name__ == "__main__":
    user_path = input("Enter the path of the directory to organize: ")
    organizer = FileOrganizer(user_path)
    organizer.organize()
    print("Files organized successfully!")
        
    

