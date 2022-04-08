from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import timedelta


class NbibliothekUI:
    def __init__(self, nbibliothek_service):
        self.__root = Tk()
        self.__service = nbibliothek_service
        self.__tabs = self.tab()
        self.frame_book = LabelFrame(self.__tabs[0], bd=5, bg='Ghost White', font=('Arial', 10, 'bold'), text='Buku')
        self.frame_book.grid(row=12, column=1, padx=15, pady=15)
        self.__frame_member = LabelFrame(self.__tabs[0], bd=5, bg='Ghost White', font=('Arial', 10, 'bold'),
                                       text='Anggota')
        self.__frame_member.grid(row=25, column=0, columnspan=4, padx=15, pady=15)
        self.frame_judul_terpopuler = LabelFrame(self.__tabs[1], bd=5, bg='Ghost White', font=('Arial', 10, 'bold'),
                                       text='Buku')
        self.frame_judul_terpopuler.grid(row=25, column=3, columnspan=6, padx=15, pady=15)

        # book
        self.__booktitle_var = StringVar()
        self.__booktitle_entry = Entry(self.frame_book, width=25, fg='black', font=('Arial', 10, 'bold'),
                                     textvariable=self.__booktitle_var)
        self.__booktitle_entry.grid(row=0, column=1)

        self.__author_var = StringVar()
        self.__author_entry = Entry(self.frame_book, width=25, fg='black', font=('Arial', 10, 'bold'),
                                  textvariable=self.__author_var)
        self.__author_entry.grid(row=1, column=1)

        self.__publisher_var = StringVar()
        self.__publisher_entry = Entry(self.frame_book, width=25, fg='black', font=('Arial', 10, 'bold'),
                                     textvariable=self.__publisher_var)
        self.__publisher_entry.grid(row=2, column=1)

        self.__classification_var = StringVar()
        self.__classification_entry = Entry(self.frame_book, width=25, fg='black', font=('Arial', 10, 'bold'),
                                          textvariable=self.__classification_var)
        self.__classification_entry.grid(row=3, column=1)

        self.__barcode_var = StringVar()
        self.__barcode_entry = Entry(self.frame_book, width=25, fg='black', font=('Arial', 10, 'bold'),
                                   textvariable=self.__barcode_var)
        self.__barcode_entry.grid(row=4, column=1)

        self.__exemplar_total_var = StringVar()
        self.__exemplar_total_entry = Entry(self.frame_book, width=25, fg='black', font=('Arial', 10, 'bold'),
                                          textvariable=self.__exemplar_total_var)
        self.__exemplar_total_entry.grid(row=5, column=1)

        self.__exemplar_max = 5

        self.__find_book_entry = Entry(self.__tabs[0], fg="black", bg="yellow", borderwidth=1, text="enter book title")
        self.__find_book_entry.grid(row=5, column=2, columnspan=2)

        self.__find_button = Button(self.__tabs[0], text="Cari", command=lambda: self.find_book_clicked())
        self.__find_button.grid(row=5, column=6)

        self.__find_book_message = Label(self.__tabs[0])
        self.__find_book_message.grid(row=7, column=1)

        # member

        self.__nim_var = StringVar()
        self.__nim_entry = Entry(self.__frame_member, width=25, fg='black', font=('Arial', 10, 'bold'),
                               textvariable=self.__nim_var)
        self.__nim_entry.grid(row=1, column=1)

        self.__member_name_var = StringVar()
        self.__member_name_entry = Entry(self.__frame_member, width=25, fg='black', font=('Arial', 10, 'bold'),
                                       textvariable=self.__member_name_var)
        self.__member_name_entry.grid(row=0, column=1)

        self.__return_date_var = StringVar()
        self.__return_date_entry = Entry(self.__frame_member, width=25, fg='black', font=('Arial', 10, 'bold'),
                                       textvariable=self.__return_date_var)
        self.__return_date_entry.grid(row=2, column=1)

        self.__borrowed_book_var_1 = StringVar()
        self.__borrowed_book_entry_1 = Entry(self.__frame_member, width=25, fg='black', font=('Arial', 10, 'bold'),
                                           textvariable=self.__borrowed_book_var_1)
        self.__borrowed_book_entry_1.grid(row=4, column=1)

        self.__borrowed_book_var_2 = StringVar()
        self.__borrowed_book_entry_2 = Entry(self.__frame_member, width=25, fg='black', font=('Arial', 10, 'bold'),
                                           textvariable=self.__borrowed_book_var_2)
        self.__borrowed_book_entry_2.grid(row=5, column=1)

        self.__borrowed_book_var_3 = StringVar()
        self.__borrowed_book_entry_3 = Entry(self.__frame_member, width=25, fg='black', font=('Arial', 10, 'bold'),
                                           textvariable=self.__borrowed_book_var_3)
        self.__borrowed_book_entry_3.grid(row=6, column=1)

        self.__find_member_entry = Entry(self.__tabs[0], fg="black", bg="yellow", borderwidth=1, text="enter NIM")
        self.__find_member_entry.grid(row=17, column=2, columnspan=2)
        self.__find_member_button = Button(self.__tabs[0], text="Cari", command=lambda: self.find_member_clicked())
        self.__find_member_button.grid(row=17, column=6)
        self.__borrow_button = Button(self.__tabs[0], text="Pinjam",
                                    command=lambda: self.borrowing_button_clicked(self.__find_member_entry.get(),
                                                                                  self.__find_book_entry.get(),
                                                                                  self.return_date()))
        self.__borrow_button.grid(row=18, column=6)
        self.__return_button_1 = Button(self.__frame_member, text="Kembalikan", command=lambda: self.return_book_clicked())
        self.__return_button_1.grid(row=4, column=2)
        self.__return_button_2 = Button(self.__frame_member, text="Kembalikan", command=lambda: self.return_book_clicked())
        self.__return_button_2.grid(row=5, column=2)
        self.__return_button_3 = Button(self.__frame_member, text="Kembalikan", command=lambda: self.return_book_clicked())
        self.__return_button_3.grid(row=6, column=2)

        self.__find_member_message = Label(self.__tabs[0])
        self.__find_member_message.grid(row=22, column=1)
        self.__borrow_message = Label(self.__tabs[0])
        self.__borrow_message.grid(row=23, column=1)

        # judul terpopuler
        self.__judul_terpopuler_var_1 = StringVar()
        self.__judul_terpopuler_entry_1 = Entry(self.frame_judul_terpopuler, width=25, fg='black', font=('Arial', 10, 'bold'),
                                           textvariable=self.__judul_terpopuler_var_1)
        self.__judul_terpopuler_entry_1.grid(row=0, column=3)

        self.__judul_terpopuler_var_2 = StringVar()
        self.__judul_terpopuler_entry_2 = Entry(self.frame_judul_terpopuler, width=25, fg='black',font=('Arial', 10, 'bold'),
                                            textvariable=self.__judul_terpopuler_var_2)
        self.__judul_terpopuler_entry_2.grid(row=1, column=3)

        self.__judul_terpopuler_var_3 = StringVar()
        self.__judul_terpopuler_entry_3 = Entry(self.frame_judul_terpopuler, width=25, fg='black',font=('Arial', 10, 'bold'),
                                            textvariable=self.__judul_terpopuler_var_3)
        self.__judul_terpopuler_entry_3.grid(row=2, column=3)

        self.__judul_terpopuler_var_4 = StringVar()
        self.__judul_terpopuler_entry_4 = Entry(self.frame_judul_terpopuler, width=25, fg='black',font=('Arial', 10, 'bold'),
                                            textvariable=self.__judul_terpopuler_var_4)
        self.__judul_terpopuler_entry_4.grid(row=3, column=3)

        self.__judul_terpopuler_var_5 = StringVar()
        self.__judul_terpopuler_entry_5 = Entry(self.frame_judul_terpopuler, width=25, fg='black',
                                            font=('Arial', 10, 'bold'),
                                            textvariable=self.__judul_terpopuler_var_5)
        self.__judul_terpopuler_entry_5.grid(row=4, column=3)


    def title(self):
        title_label = Label(self.__root, text="Neugierig bibliothek", borderwidth=1, bg="white", font=("Arial", 10))
        title_label.grid(row=0, column=0, columnspan=4, sticky=W)
        address_label = Label(self.__root, text="Ilse. Str No.21 Berlin - 12053", borderwidth=1, bg="white",
                              font=("Arial", 10))
        address_label.grid(row=1, column=0, columnspan=4, sticky=W)
        date_label = Label(self.__root, text=date.today(), borderwidth=1, bg="white", font=("Arial", 10))
        date_label.grid(row=0, column=6, columnspan=2, sticky=E)

    def tab(self):
        tab_control = ttk.Notebook(self.__root)
        find_tab = ttk.Frame(tab_control)
        report_tab = ttk.Frame(tab_control)
        tab_control.add(find_tab, text="Cari")
        tab_control.add(report_tab, text="Laporan")
        tab_control.grid(row=3, column=0, columnspan=7, sticky=W)
        return find_tab, report_tab

    def find_books(self):
        find_label = Label(self.__tabs[0], text="Cari", borderwidth=1, font=("Arial", 10))
        find_label.grid(row=5, column=0)
        find_label_1 = Label(self.__tabs[0], text=":", borderwidth=1, font=("Arial", 10))
        find_label_1.grid(row=5, column = 1)

    def book(self):
        booktitle_label = Label(self.frame_book, text='Judul :', padx=2, pady=2, bg='Ghost White')
        booktitle_label.grid(row=0, column=0, sticky=W)
        author_label = Label(self.frame_book, text='Pengarang :', padx=2, pady=2, bg='Ghost White')
        author_label.grid(row=1, column=0, sticky=W)
        publisher_label = Label(self.frame_book, text='Penerbit :', padx=2, pady=2, bg='Ghost White')
        publisher_label.grid(row=2, column=0, sticky=W)
        classification_label = Label(self.frame_book, text='No. Klasifikasi :', padx=2, pady=2, bg='Ghost White')
        classification_label.grid(row=3, column=0, sticky=W)
        barcode_label = Label(self.frame_book, text='No. Barcode :', padx=2, pady=2, bg='Ghost White')
        barcode_label.grid(row=4, column=0, sticky=W)
        exemplar_total_label = Label(self.frame_book, text='Jumlah Exemplar :', padx=2, pady=2, bg='Ghost White')
        exemplar_total_label.grid(row=5, column=0, sticky=W)

    def find_nim(self):
        nim_label = Label(self.__tabs[0], text="Nomor Induk Mahasiswa", borderwidth=1, font=("Arial", 10))
        nim_label.grid(row=17, column=0)
        nim_label_1 = Label(self.__tabs[0], text=":", borderwidth=1, font=("Arial", 10))
        nim_label_1.grid(row=17, column=1)

    def member(self):
        member_label = Label(self.__frame_member, text='Nama :', padx=2, pady=2, bg='Ghost White')
        member_label.grid(row=0, column=0, sticky=W)
        nim_label = Label(self.__frame_member, text='NIM :', padx=2, pady=2, bg='Ghost White')
        nim_label.grid(row=1, column=0, sticky=W)
        return_date_label = Label(self.__frame_member, text='Tanggal Kembali :', padx=2, pady=2, bg='Ghost White')
        return_date_label.grid(row=2, column=0, sticky=W)
        borrowed_book_label = Label(self.__frame_member, text='Peminjaman :', padx=2, pady=2, bg='Ghost White')
        borrowed_book_label.grid(row=4, column=0, sticky=W)
        borrow_time_label = Label(self.__frame_member, text='(satu minggu dari sekarang)', padx=2, pady=2,
                                  bg='Ghost White')
        borrow_time_label.grid(row=3, column=1, sticky=W)

    def find_book_clicked(self):
        find_book = self.__find_book_entry.get()
        get_book = self.__service.check_book_title(find_book)

        if get_book is False:
            for row_number, row in enumerate(get_book):
                self.__booktitle_var.set('')
                self.__author_var.set('')
                self.__publisher_var.set('')
                self.__classification_var.set('')
                self.__barcode_var.set('')
                self.__exemplar_total_var.set('')
                return self.__find_book_message.config(text='Judul buku tidak ditemukan!', bg='red', fg='white')
        else:
            for row_number, row in enumerate(get_book):
                self.__booktitle_var.set(row.judul)
                self.__author_var.set(row.pengarang)
                self.__publisher_var.set(row.penerbit)
                self.__classification_var.set(row.no_klasifikasi)
                self.__barcode_var.set(row.no_barcode)
                self.__exemplar_total_var.set(str(row.jumlah_eksemplar) + '/' + str(self.__exemplar_max))
                return self.__find_book_message.config(text='Judul buku ditemukan!', bg='green', fg='white')


    def find_member_clicked(self):
        find_member = self.__find_member_entry.get()
        get_member = self.__service.check_member_by_nim(find_member)
        if get_member is False:
            self.__nim_var.set('')
            self.__member_name_var.set('')
            self.__return_date_var.set('')
            return self.__find_member_message.config(text='NIM tidak ditemukan!!!', bg='red', fg='white')

        else:
            for row_number, row in enumerate(get_member):
                self.__nim_var.set(row.nim)
                self.__member_name_var.set(row.nama)
                self.__return_date_var.set(row.tanggal_kembali)

            return self.__find_member_message.config(text='NIM ditemukan!', bg='green', fg='white')

    def borrowing_button_clicked(self, title, nim, return_date):
        data = self.__service.check_if_available(title, nim, return_date)
        if not data:
            self.__borrow_message.config(text="Telah melebihi Quota Peminjaman!!!", bg="red", fg='white')
        else:
            data1 = self.__service.check_book_title(self.__booktitle_entry.get())
            print(data1)
            for row_number, row in enumerate(data1):
                self.__booktitle_var.set(row.judul)
                self.__author_var.set(row.pengarang)
                self.__publisher_var.set(row.penerbit)
                self.__classification_var.set(row.no_klasifikasi)
                self.__barcode_var.set(row.no_barcode)
                self.__exemplar_total_var.set(str(row.jumlah_eksemplar) + '/' + str(self.__exemplar_max))
                break
            for row_number, row in enumerate(self.__service.check_member(nim)):
                self.__member_name_var.set(row.nama)
                self.__nim_var.set(row.nim)
                break
            for row_number, row in enumerate(self.__service.check_borrowed_book(nim)):
                self.__borrowed_book_var_1.set(row.peminjaman1)
                self.__borrowed_book_var_2.set(row.peminjaman2)
                self.__borrowed_book_var_3.set(row.peminjaman3)
                break
            self.__borrow_message.config(text="Peminjaman Berhasil!!!", bg="lime green", fg='white')

    def return_date(self):
        today_date = date.today()
        next_week = today_date + timedelta(days=7)
        return next_week

    def return_book_clicked(self):
        pass

    def mainloop(self):
        self.__root.mainloop()
