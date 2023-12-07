import json

class ListSongs:
    @staticmethod
    def get_song_list():
        list_output = ""

        with open("./swedish_christmas_songs.json", "r", encoding='utf-8') as f: 
            songs = json.load(f)
            
            for song in songs:
                list_output += "- " + song['name'] + "\n"

        return list_output.strip()