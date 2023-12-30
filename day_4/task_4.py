from typing import Any
import datetime


class Author:

    def __init__(self, first_name: str, second_name: str, year_of_birth: int):
        self.first_name = first_name
        self.second_name = second_name
        self.year_of_birth = year_of_birth

    def __str__(self):
        return '{} {}'.format(self.first_name, self.second_name)

    def __repr__(self):
        return 'Author({}, {}, {})'.format(self.first_name, self.second_name, self.year_of_birth)

    def __eq__(self, other: Any):
        if self.__class__ is not type(other):
            return False

        if (self.first_name == other.first_name
                and self.second_name == other.second_name
                and self.year_of_birth == other.year_of_birth):
            return True

        return False

    def __hash__(self):
        return hash(self.first_name + self.second_name + str(self.year_of_birth))


class Genre:

    def __init__(self, genre: str, genre_desc: str):
        self.genre = genre
        self.genre_desc = genre_desc

    def __str__(self):
        return '{} {}'.format(self.genre, self.genre_desc)

    def __repr__(self):
        return 'Genre({}, {})'.format(self.genre, self.genre_desc)


class Book:

    def __init__(self, title: str, language: str, year: int, /, *authors: Author,
                 description: str | None = None, isbn: int | None = None, genres: list[Genre] | None = None):
        self.title = title
        self.language = language
        self.year = year

        if not authors:
            raise ValueError('Author is not specified. At least one author should be specified.')
        if any(type(author) is not Author for author in authors):
            raise TypeError('Invalid author specified.')
        self.authors = authors

        self.description = description
        self.isbn = isbn

        if genres is not None and type(genres) not in (list, tuple):
            genres = [genres]

            if any(type(genre) is not Genre for genre in genres):
                raise TypeError('Invalid genre specified.')
        self.genres = genres

    def get_age(self):
        """returns book's age"""
        current_year = datetime.date.today().year

        return current_year - self.year

    def __str__(self):
        return '{}: {}'.format(self.title, ', '.join(str(author) for author in self.authors))

    def __repr__(self):
        return 'Book({}, {})'.format(self.title, self.authors)

    def __eq__(self, other: Any):
        if self.__class__ is not type(other):
            return False

        if self.title == other.title and set(self.authors) == set(other.authors):
            return True

        return False


a1 = Author('qqqq', 'qqq1', 1234)
# a2 = Author('wwww', 'www2', 1234)
#
# print({a1} == {a1, a2})
#
print(Book('qqqq', 'wwww', 1234, a1, description='zzzz').get_age())
