class Author:
    all = []
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("property 'name' must be of type 'str'")
        
        self._name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

class Book:
    all = []
    def __init__(self, title: str):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise ValueError("property 'title' must be of type 'str'")
        
        self._title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []
    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @property
    def book(self):
        return self._book
    
    @property
    def date(self):
        return self._date
    
    @property
    def royalties(self):
        return self._royalties
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("property 'author' must be an Author instance")
        
        self._author = author

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise ValueError("property 'book' must be a Book instance")
        
        self._book = book

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError("property 'date' must be of type 'str'")
        
        self._date = date

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise ValueError("property 'royalties' must be of type 'int'")
        
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if contract.date == date]
