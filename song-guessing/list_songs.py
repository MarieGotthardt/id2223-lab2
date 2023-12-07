import os

class ListSongs:
    @staticmethod
    def get_song_list():
        folder_path = './swedish_christmas_songs'

        list_output = ""

        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith('.txt'):  # Check if the file is a text file
                list_output += "- " + filename[:-4].replace("_", " ") + "\n"

        return list_output.strip()