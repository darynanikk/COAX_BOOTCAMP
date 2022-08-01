import csv
import os
import pandas as pd
from functools import reduce

file_name = 'notes.csv'
file_exists = os.path.exists(file_name)


class Note:
    notes = []

    def __init__(self, film_name, note, rating):
        self.film_name = film_name
        self.note = note
        self.rating = rating

    def __str__(self):
        return f'{self.film_name}:{self.note}:{self.rating}'

    def add(self):
        """Add note"""

        Note.notes.append(self)
        with open(file_name, 'a', newline='') as csv_writer:
            fieldnames = ['film_name', 'note', 'rating']
            writer = csv.DictWriter(csv_writer, fieldnames=fieldnames)

            if not file_exists and len(Note.notes) < 2:
                writer.writeheader()

            writer.writerow({'film_name': self.film_name, 'note': self.note, 'rating': self.rating})

    @classmethod
    def print_notes(cls):
        """Print notes"""

        for note in cls.notes:
            print(f'film_name:{note.film_name}\nnote: {note.note}\nrating: {note.rating}')

    @staticmethod
    def read_notes():
        """Read notes from csv file"""

        with open('notes.csv', 'r') as csv_reader:
            next(csv_reader)
            reader = csv.reader(csv_reader, delimiter=',')
            for row in reader:
                print(row)

    def remove(self):
        """Removing note by name"""

        Note.notes.remove(self)
        df = pd.read_csv(file_name)
        df = df[df.film_name != self.film_name]
        df.to_csv('notes.csv', index=False)

    @classmethod
    def get_films_with_highest_rating(cls):
        """Get films with the highest rating"""
        max_rated_film = max(cls.notes, key=lambda note: note.rating)
        return list(filter(lambda note: note.rating == max_rated_film.rating, cls.notes))

    @classmethod
    def get_films_with_lowest_rating(cls):
        """Get films with the lowest rating"""
        min_rated_film = min(cls.notes, key=lambda note: note.rating)
        return list(filter(lambda note: note.rating == min_rated_film.rating, cls.notes))

    @classmethod
    def get_average_rating(cls):
        """Get average rating of all films"""

        average_rating = reduce(lambda acc, el: acc + el.rating, cls.notes, 0) / len(cls.notes)
        return average_rating
