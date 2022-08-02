from services import NoteService

if __name__ == '__main__':
    # note_1 = NoteService.create(
    #     film_name='Battle for Sevastopol',
    #     note="It tells the story of heroic Russian sniper without glamorizing war. "
    #          "Instead the horror of war is pervasive and though she is a survivor her story is tragic. It's also very "
    #          "interesting to get a glimpse of Stalin-era Soviet culture. It's a must see for anyone interested in "
    #          "WW2, history, biographies, or intense drama.",
    #     rating=5)

    note_2 = NoteService.create(film_name='Homeward', note='"Homeward" is a great story, with catchy characters, good morale, funny jokes, catchy drama, charming characters in an unusual setting, and, most importantly, an amazing finale that will not leave anyone indifferent.', rating=5)
    print(note_2)
