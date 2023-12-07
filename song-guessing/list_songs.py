import os

folder_path = './swedish_christmas_songs'

list_output = ""

for filename in sorted(os.listdir(folder_path)):
    if filename.endswith('.txt'):  # Check if the file is a text file
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            list_output += "- " + filename[:-4].replace("_", " ") + "\n"

print(list_output.strip())