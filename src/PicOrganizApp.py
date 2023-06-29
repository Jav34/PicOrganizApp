#PicOrganizApp version 1.0
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import datetime
import shutil
import exifread

# Global variables
selected_folder_path = ""
new_folder_path = ""

def select_folder():
    global selected_folder_path
    folder_path = filedialog.askdirectory()
    selected_folder_path = folder_path
    print("Wybrany folder:", selected_folder_path)
    update_file_list(selected_folder_path)

# Function to update the file list in the text widget
def update_file_list(folder_path):
    global file_list_text
    file_list_text.delete("1.0", tk.END)  # Clear the existing content

    # Iterate through files in the selected folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_list_text.insert(tk.END, file_name + "\n")

def create_folder():
    global new_folder_path
    result = messagebox.askquestion("Tworzenie folderu", "Czy chcesz utworzyć nowy folder wewnątrz wybranego folderu?")

    if result == 'yes':
        new_folder_path = filedialog.askdirectory(initialdir=selected_folder_path)
    else:
        new_folder_path = filedialog.askdirectory()

    if new_folder_path:
        print("Nowy folder:", new_folder_path)
        create_new_folder(new_folder_path)

def create_new_folder(folder_path):
    now = datetime.datetime.now()
    folder_name = "PicOrganizApp"
    new_folder_path = os.path.join(folder_path, folder_name)

    try:
        if os.path.exists(new_folder_path):
            result = messagebox.askquestion("Zastąpić folder", "Folder 'PicOrganizApp' już istnieje. Czy chcesz go zastąpić?")
            if result == 'yes':
                shutil.rmtree(new_folder_path)
            else:
                new_folder_path = os.path.join(folder_path, "PicOrganizApp New")

        os.makedirs(new_folder_path)
        print("Utworzono nowy folder:", new_folder_path)
        organize_images(new_folder_path)

        result = messagebox.askquestion("Usuwanie poprzednich plików", "Czy chcesz usunąć poprzednie pliki z wybranego folderu?")

        if result == 'yes':
            remove_previous_images(selected_folder_path)

        messagebox.showinfo("Sukces", "Wszystko zostało poprawnie wykonane!")

    except OSError:
        messagebox.showerror("Błąd", "Wystąpił problem. Możliwe, że istnieją już takie foldery")

def organize_images(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = []

    # Separate image files
    for file_name in os.listdir(selected_folder_path):
        if os.path.isfile(os.path.join(selected_folder_path, file_name)):
            if any(file_name.lower().endswith(ext) for ext in image_extensions):
                image_files.append(file_name)

    if len(image_files) > 0:
        for file_name in image_files:
            file_path = os.path.join(selected_folder_path, file_name)
            creation_date = get_creation_date(file_path)
            if creation_date:
                year_month = creation_date.strftime("%Y-%m")
                year_folder = os.path.join(folder_path, year_month[:4])
                month_folder = os.path.join(year_folder, year_month[5:])
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                if not os.path.exists(month_folder):
                    os.makedirs(month_folder)
                destination_path = os.path.join(month_folder, file_name)
                shutil.copy(file_path, destination_path)

def remove_previous_images(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = []

    # Separate image files
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            if any(file_name.lower().endswith(ext) for ext in image_extensions):
                image_files.append(file_name)

    if len(image_files) > 0:
        for file_name in image_files:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

def get_creation_date(file_path):
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal')
            creation_date = tags.get('EXIF DateTimeOriginal')
            if creation_date:
                return datetime.datetime.strptime(str(creation_date), "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return None

# Create the main window
window = tk.Tk()
window.title("OrganizApp")

# Create a button to select the photo folder
select_button = tk.Button(window, text="Wybierz folder", command=select_folder)
select_button.grid(row=0, column=0, padx=10, pady=10)

# Create a button to create a new folder
create_button = tk.Button(window, text="Stwórz folder", command=create_folder)
create_button.grid(row=0, column=1, padx=10, pady=10)

# Label to display the selected folder path
selected_folder_label = tk.Label(window, text="Zawartość wybranego folderu: ")
selected_folder_label.grid(row=1, column=0, pady=10)

# Text widget to display the processed files
file_list_text = tk.Text(window, width=60, height=20)
file_list_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

window.mainloop()