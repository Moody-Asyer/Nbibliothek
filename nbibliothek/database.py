import sqlite3
from datetime import date
from datetime import timedelta
from nbibliothek.model import BooksDTO, AnggotaDTO, PeminjamanDTO


class NbibliothekDatabase:
    def __init__(self, db_url):
        self.__db_url = db_url
        self.__conn = self.__create_connection()

    def __create_connection(self):
        return sqlite3.connect(self.__db_url)

    def get_con(self):
        self.__create_connection()

    def commit(self):
        self.__conn.commit()

    def begin_transaction(self):
        pass

    def __toDto_book(self, rows):
        book_dtos = []

        for row in rows:
            book_dtos.append(BooksDTO(row[0], row[1], row[2], row[3], row[4], row[5]))

        return book_dtos

    def __toDto_member(self, rows):
        member_dtos = []

        for row in rows:
            member_dtos.append(AnggotaDTO(row[0], row[1], row[2]))

        return member_dtos

    def __toDto_borrowed_book(self, rows):
        borrowed_book_dtos = []

        for row in rows:
            borrowed_book_dtos.append(PeminjamanDTO(row[0], row[1], row[2], row[3]))

        return borrowed_book_dtos

    def init(self):
        drop_books_table = """
            DROP TABLE IF EXISTS books;
        """
        self.__conn.cursor().execute(drop_books_table)

        create_books_table = """        
            CREATE TABLE IF NOT EXISTS books (
                judul            text    PRIMARY KEY NOT NULL,
                pengarang        text    NOT NULL,
                penerbit         text    NOT NULL,
                no_klasifikasi   integer NOT NULL,
                no_barcode       integer NOT NULL,
                jumlah_eksemplar integer NOT NULL
            );
        """
        self.__conn.cursor().execute(create_books_table)

        drop_member_table = """
            DROP TABLE IF EXISTS anggota;
        """
        self.__conn.cursor().execute(drop_member_table)

        create_member_table = """
            CREATE TABLE IF NOT EXISTS anggota (
                nomor_induk_mahasiswa integer PRIMARY KEY NOT NULL,
                nama                  text    NOT NULL,
                tanggal_kembali       date
            );
        """
        self.__conn.cursor().execute(create_member_table)

        drop_borrowing_table = """
            DROP TABLE IF EXISTS peminjaman;
        """
        self.__conn.cursor().execute(drop_borrowing_table)

        create_borrowing_table = """
            CREATE TABLE IF NOT EXISTS peminjaman (
                nomor_induk_mahasiswa integer NOT NULL,
                judul                 text,
                CONSTRAINT fk_nim FOREIGN KEY (nomor_induk_mahasiswa) REFERENCES anggota,
                CONSTRAINT fk_judul FOREIGN KEY (Judul) REFERENCES books
            ); 
        """

        self.__conn.cursor().execute(create_borrowing_table)

        # today = date.today()
        # date format : yyyy-mm-dd


        # drop_borrowed_book_table = """
        #     DROP TABLE IF EXISTS peminjaman;
        # """
        # self.__conn.cursor().execute(drop_borrowed_book_table)

        insert_books_table = """   
            INSERT INTO books VALUES("Sepuluh Hukum Allah", "Pdt. Dr. Stephen Tong", "Momentum", 200, 200001, 5),
                                    ("Allah Tri Tunggal", "Pdt. Dr. Stephen Tong", "Momentum", 200, 200002, 5),
                                    ("Cosmos", "Carl Sagan", "Random House", 500, 500001, 5),
                                    ("The Biology of Belief", " Bruce H. Lipton", "Hay House Inc", 500, 500002, 5),
                                    ("The Most Powerful Idea in the World", "William Rosen", 
                                    "University Of Chicago Press", 600, 600001, 5),
                                    ("Homo Deus", "Yuval Noah Harari", "Harvill Secker", 600, 600002, 5),
                                    ("AIR KATA KATA", "Sindhunata", "Gramedia Pustaka Utama", 800, 800001, 5),
                                    ("Lelaki Tua dan Laut", "Ernest Hemingway", "Pustaka Jaya", 800, 800002, 5),
                                    ("A History of the Twentieth Century", "Martin Gilbert", 
                                    "William Morrow Paperbacks", 900, 900001, 5),
                                    ("The Rise and Fall of the Third Reich", "William L. Shirer", "Simon & Schuster", 
                                    900, 900002, 5);
        """
        self.__conn.cursor().execute(insert_books_table)

        insert_member_table = """   
            INSERT INTO anggota VALUES(10101190129, "Charis Hulu", ''),
                                    (10101190602, "Badia Tuahman", ''),
                                    (10101190564, "Michael David", ''),
                                    (10101190694, "Elson P R S", ''),
                                    (10101190476, "Yehezkiel Purnama", ''),
                                    (10101190202, "Arnold Christian", ''),
                                    (10101190203, "Edgar Tigor", ''),
                                    (10101190378, "Jody N Imanuel", ''),
                                    (10101190478, "Yosia Farianto", ''),
                                    (10101190479, "Christopher V", '');
        """
        self.__conn.cursor().execute(insert_member_table)
        
    def insert_borrow_book(self, nim, title, return_date):
        insert_borrowed_book_statement = """
            INSERT INTO peminjaman VALUES (?, ?, ?):
        """

        self.__conn.cursor().execute(insert_borrowed_book_statement, (nim, title, return_date))

    def get_borrowed_book(self, nim):
        select_statement = """
            SELECT COUNT(nomor_induk_mahasiswa)
             FROM peminjaman
            WHERE nomor_induk_mahasiswa = ?
        
        """

        cursor = self.__conn.cursor()
        cursor.execute(select_statement, (nim,))
        rows = cursor.fetchall()

        return rows[0][0]

    def get_avail_exemplar(self, title):
        select_statement = """
            SELECT jumlah_eksemplar
             FROM books
            WHERE judul=?
        """

        cursor = self.__conn.cursor()
        cursor.execute(select_statement, (title,))
        rows = cursor.fetchall()

        return rows[0][0]

    def get_borrowing_by_nim(self, nim):
        select_from_borrowing = """   
                SELECT *
                  FROM peminjaman
                 WHERE nomor_induk_mahasiswa = ?;
        """

        cursor = self.__conn.cursor().execute(select_from_borrowing, (nim,))

        rows = cursor.fetchall()

        return self.__toDto_borrowed_book(rows)


    def update_available_exemplar(self, title):
        update_statement = f"""
            UPDATE books
             SET jumlah_eksemplar = jumlah_eksemplar - 1
             WHERE judul = ?;
        """
        cursor = self.__conn.cursor().execute(update_statement, (title))
        return cursor

    def update_borrowed_book(self, nim, borrowed_1, borrowed_2, borrowed_3):
        update_statement = f"""
            UPDATE peminjaman
             SET peminjaman_1 = ?,
                 peminjaman_2 = ?,
                 peminjaman_3 = ?
              WHERE nomor_induk_mahasiswa = ?;
        """

        cursor = self.__conn.cursor()
        cursor.execute(update_statement, (borrowed_1, borrowed_2, borrowed_3, nim))
        # rows = cursor.fetchall()
        # return self.__toDto_borrowed_book(rows)

    def update_borrow_date(self, nim):
        today_date = date.today()
        next_week = today_date + timedelta(days=7)
        update_statement = f"""
            UPDATE anggota
             SET tanggal_kembali = ?
             WHERE nomor_induk_mahasiswa=  ?;
        """

        cursor = self.__conn.cursor()
        cursor.execute(update_statement, (next_week, nim,))

    def get_book_by_title(self, judul):
        select_from_books = """   
                SELECT *
                  FROM books
                 WHERE judul=?;
        """

        cursor = self.__conn.cursor().execute(select_from_books, (judul,))
        rows = cursor.fetchall()
        # return rows
        return self.__toDto_book(rows)


    def get_book(self):
        select_from_books = """   
                SELECT *
                  FROM books;
        """

        cursor = self.__conn.cursor().execute(select_from_books)
        rows = cursor.fetchall()

        return rows

    def get_member(self):
        select_from_member = """   
                SELECT *
                  FROM anggota;
        """

        cursor = self.__conn.cursor().execute(select_from_member)
        rows = cursor.fetchall()

        return rows

    def get_member_by_nim(self, nim):
        select_from_anggota = """   
                SELECT *
                  FROM anggota
                 WHERE nomor_induk_mahasiswa=?;
        """

        cursor = self.__conn.cursor().execute(select_from_anggota, (nim,))
        rows = cursor.fetchall()
        return self.__toDto_member(rows)


    def get_borrowed_book_by_nim(self, nim):
        select_statement = """
            SELECT *
            FROM peminjaman
            WHERE nomor_induk_mahasiswa = ?
        """

        cursor = self.__conn.cursor().execute(select_statement, (nim,))
        rows = cursor.fetchall()

        return self.__toDto_borrowed_book(rows)




    # print(get_rows[0].judul)
