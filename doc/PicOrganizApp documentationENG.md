# `PicOrganizApp Documentation`
PicOrganizApp is a Python desktop app designed to organize image files based on their creation date. It provides a GUI using Tkinter lib to interact with the user. 
## `Usage`
To use PicOrganizApp, follow the steps below:
### `Selecting a Folder`
1. Launch the PicOrganizApp app. 
2. Click on the "Wybierz folder" button to select a folder containing image files. 
3. The selected folder path will be displayed on the screen. 
### `Creating a new folder`
1. After selecting a folder, click on the "Stwórz folder" button. 
2. A prompt will ask if you want to create a new folder insde the selected folder. Choose "Yes" or "No" accordingly. 
3. If "Yes" is selected, choose a destination folder for the new folder.
4. If "No" is selected, choose the desired destination folder. 
5. The new folder will be created, and its path will be displayed on the screen. 
### `Organizing Images`
1. Once the new folder is created, PicOrganizApp will automatically organize the images based on their creation date. 
2. The images will be moved to appropriate subfolders within the new folder, based on their creation year and month. 
### `Removing Previous Images`
1. After organizing the images, a prompt will ask if you want to remove the previous images from the selected folder. 
2. Choose "Yes" or "No" based on your preference. 
3. If "Yes" is selected, the previous images will be removed from the selected folder. 
## `Code Overview`
The code is divided into several functions to handle different functionalities of the application. Here's an overview of each function:

### `Global Variables`
* `selected_folder_path`: Stores the path of the selected folder.
* `new_folder_path`: Stores the path of the newly created folder.
### `Function: select_folder`
* Responsible for opening a file dialog to allow the user to select a folder.
* Stores the selected folder path in the selected_folder_path variable.
* Prints the selected folder path on the console.
### `Function: create_folder`
* Asks the user if they want to create a new folder inside the selected folder.
* Opens a file dialog to choose the destination folder for the new folder.
* If a new folder path is selected, stores it in the new_folder_path variable.
* Creates a new folder at the specified path.
* Prints the new folder path on the console.
* Calls the organize_images function to organize the images in the new folder.
* Asks the user if they want to remove previous images from the selected folder.
* If confirmed, calls the remove_previous_images function to remove the previous images.
### `Function: create_new_folder`
* Takes a folder path as input and creates a new folder named "PicOrganizApp" at that path.
* Checks if the folder already exists and prompts the user to confirm whether to replace it or create a new one.
* If confirmed to replace, deletes the existing folder and recreates a new one with the same name.
* If confirmed to create a new one, appends "New" to the folder name.
* Prints the new folder path on the console.
* Calls the organize_images function to organize the images in the new folder.
### `Function: organize_images`
* Takes a folder path as input and organizes the images in that folder based on their creation date.
* Retrieves the list of image files in the selected folder.
* For each image file, reads its creation date using the get_creation_date function.
* If the creation date is available, creates year and month subfolders within the new folder.
* Moves the image file to the appropriate month subfolder.
### `Function: remove_previous_images`
* Takes a folder path as input and removes the previous images in that folder.
* Retrieves the list of image files in the selected folder.
* Deletes each image file from the folder.
### `Function: get_creation_date`
* Takes a file path as input and extracts the creation date from the image file's EXIF metadata.
* Uses the exifread library to read the EXIF metadata and extract the creation date.
* Returns the creation date as a datetime object.
## `Contributing`
Contributions to OrganizApp are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request on the GitHub repository.
