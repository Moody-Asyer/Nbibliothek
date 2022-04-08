from nbibliothek.ui import NbibliothekUI
from nbibliothek.database import NbibliothekDatabase


class NbibliothekService:
    def __init__(self, db_url):
        self.__db = NbibliothekDatabase(db_url)
        self.__ui = NbibliothekUI(self)

    def begin_transaction(self):
        pass

    def run(self):
        self.__ui.title()
        self.__ui.book()
        self.__ui.member()

        self.__ui.find_nim()
        self.__ui.find_books()
        self.__ui.mainloop()


    def check_book_title(self, title):
        self.__db.begin_transaction()
        book = self.__db.get_book_by_title(title)
        if len(book) == 0:
            self.__db.commit()
            return False
        else:
            self.__db.commit()
            return book

    def check_member_by_nim(self, nim):
        self.__db.begin_transaction()
        member = self.__db.get_member_by_nim(nim)
        if len(member) == 0:
            self.__db.commit()
            return False
        else:
            self.__db.commit()
            return member

    def check_borrowed_books(self, nim):
        self.__db.begin_transaction()
        borrowed_book = self.__db.get_borrowed_book_by_nim(nim)
        if len(borrowed_book) == 0:
            self.__db.commit()
            return False
        else:
            self.__db.commit()
            return borrowed_book

    def get_borrowed_book(self, nim):
        borrowed_book = self.__db.get_borrowed_book(nim)
        return borrowed_book

    def get_available_book(self, title):
        avail_exemplar = self.__db.get_avail_exemplar(title)
        return avail_exemplar

    def check_if_available(self, title, nim, return_date):
        # today_date = date.today()
        # next_week = today_date + timedelta(days=7)
        if self.get_available_book(title) > 0 and self.get_borrowed_book(nim) < 3:
            self.__db.update_available_exemplar(title)
            self.__db.get_book_by_title(title)
            self.__db.insert_borrow_book(nim, title, return_date)
            self.__db.commit()
            return True

    def update_database(self, nim, peminjaman1, peminjaman2, peminjaman3):
        return self.__db.update_borrowed_book(nim, peminjaman1, peminjaman2, peminjaman3)

    def init_db(self):
        self.__db.init()

class AbstractObserver:
    def call(self, title):
        pass

class BookNotFoundFiveTimesObserver(AbstractObserver):
    def __init__(self, title, service):
        self.counter = title
        self.count = 0
        self.service = service

    def call(self, title):
        self.count = self.counter.get()
        self.count = self.count + 1
        if self.count >= 5:
            return f"buku {title} sudah dicari 5X"
        else:
            pass

class ReturnedBookObserver(AbstractObserver):
    def __init__(self, title, service):
        self.title = title
        self.service = service

    def call(self, title):
        return f"Buku {title} telah dikembalikan"