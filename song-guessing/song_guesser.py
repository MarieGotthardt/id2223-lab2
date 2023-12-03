import json
from datasketch import MinHash

class SongGuesser:
    @staticmethod
    def guess_song(query):
        with open("./swedish_christmas_songs.json", "r", encoding='utf-8') as f: 
            songs = json.load(f)
            shingle_size = 5

            query_shingles = get_shingles(query, shingle_size)
            query_minhash = create_minhash(query_shingles)

            max_sim = 0
            max_name = ""
            
            for song in songs:
                song_lyrics = song['lyrics'].lower()
                song_shingles = get_shingles(song_lyrics, shingle_size)
                song_minhash = create_minhash(song_shingles)
                
                estimated_jaccard = query_minhash.jaccard(song_minhash)
                if estimated_jaccard > max_sim:
                    max_sim = estimated_jaccard
                    max_name = song['name']
                
            return max_name

def get_shingles(text, shingle_size):
    return set(text[i:i+shingle_size] for i in range(len(text) - shingle_size + 1))

def create_minhash(shingles, num_perm=256):
    m = MinHash(num_perm=num_perm)
    for shingle in shingles:
        m.update(shingle.encode('utf8'))
    return m
