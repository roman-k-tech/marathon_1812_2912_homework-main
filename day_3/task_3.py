from typing import Any


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

    def __init__(self, **kwargs: str | int | list):
        self.title: str | None = None
        self.description: str | None = None
        self.lang: str | None = None
        self.authors: list[Author, ...] | None = None
        self.genres: list[Genre, ...] | None = None
        self.year: int | None = None
        self.isbn: int | None = None

        self.possible_attrs = ['title', 'description', 'lang', 'authors', 'genres', 'year', 'isbn']
        self.set_attributes(**kwargs)

    def set_attributes(self, **kwargs: str | list) -> None:

        """
        sets book attributes,  possible keys: 'title', 'description', 'lang', 'authors', 'genres', 'year', 'isbn'
        """

        for attribute, value in kwargs.items():
            if attribute not in self.possible_attrs:
                raise AttributeError('incorrect attribute: ' + attribute)

            setattr(self, attribute, value)

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
a2 = Author('wwww', 'www2', 1234)

print({a1} == {a1, a2})

print(Book(title='qqqq', description='wwww', year=1234, authors=[a1]))
