import os
import json

def read_text_files(folder_path):
    text_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # Check if the file is a text file
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                text_data.append({"name": filename[:-4].replace("_", " "), "lyrics": content})
    return text_data

def write_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Specify your folder path and output JSON file
folder_path = './swedish_christmas_songs'
output_json_file = 'swedish_christmas_songs.json'

# Process the text files and write to JSON
text_files_data = read_text_files(folder_path)
write_json(text_files_data, output_json_file)
