from hashlib import (
    sha256, sha1, sha512, sha3_384, sha224, md5
)
from task_1 import hash_string
from task_2 import convert_video_to_gif
from task_3 import Note

if __name__ == '__main__':
    s = "Python Bootcamp"
    # task 1
    print(f'Hashed: {(hash_string(s, sha512))}')

    # task 2
    path = convert_video_to_gif(
        'https://v16-webapp.tiktok.com/b764ab3dc3700e10183f390c8ea4d570/62e835b5/video/tos/useast2a/tos-useast2a-ve-0068c001/55f7326b057745d1b3a8d3736bede59d/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2528&bt=1264&btag=80000&cs=0&ds=3&ft=gKSYZ84Uo0PD1P7GQsg9wfUE75LiaQ2D~j8&mime_type=video_mp4&qs=0&rc=NzpoOjRlODVoPDQ2PGU7NUBpanJuOjo6Zmx4ZTMzNzczM0BhLmFgYGMvNmMxYS9eMGIzYSNkci5wcjRfNS1gLS1kMTZzcw%3D%3D&l=202208011419080102170870300733AC62')
    print(f'Path to gif: {path}')

    # task 3
    note_1 = Note(
        "Shadows of Forgotten Ancestors",
        "It's one of the most unusual films I've seen, a barrage of images, music and noises, shot with such an "
        "active camera we almost need seatbelts.",
        5)
    note_1.add()

    note_2 = Note("Earth", "The film is told as a melodrama and romance, not docudrama, and that makes it all the "
                           "more effective.", 4)
    note_2.add()

    note_3 = Note("Vechir na Ivana Kupala",
                  "I was very lucky recording this movie on VHS in 2001 on the french / German Arte "
                  "TV-Channel. It's in the same line as Sergei Parjanov's 'shadows of forgotten ancestors' "
                  "from 1964. Yuri Iljenko did most of the camera work for 'Shadows'.", 2)
    note_3.add()

    Note.print_notes()

    Note.read_notes()

    print(Note.get_average_rating())

    print("Highly rated:")
    for note in Note.get_films_with_highest_rating():
        print(str(note))

    print("Lower rated")
    for note in Note.get_films_with_lowest_rating():
        print(str(note))
