# KÜTÜPHANE YÖNETİM SİSTEMİ (OOP)
# Book - Member - StudentMember - Library

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def info(self):
        durum = "Müsait" if self.is_available else "Ödünçte"
        return f"{self.title} - {self.author} ({durum})"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} -> '{book.title}' kitabını ödünç aldı.")
        else:
            print("Bu kitap şu an müsait değil.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} -> '{book.title}' kitabını iade etti.")
        else:
            print("Bu kitap sende görünmüyor.")

    def list_borrowed_books(self):
        if len(self.borrowed_books) == 0:
            print("Şu an ödünç aldığın kitap yok.")
            return

        print(f"{self.name} adlı üyenin aldığı kitaplar:")
        for i, book in enumerate(self.borrowed_books, start=1):
            print(f"{i}. {book.title} - {book.author}")


class StudentMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.limit = 2

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.limit:
            print("Öğrenci limiti doldu. En fazla 2 kitap alabilirsin.")
            return

        super().borrow_book(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def list_books(self):
        if len(self.books) == 0:
            print("Kütüphanede kitap yok.")
            return

        print("\n--- KÜTÜPHANEDEKİ KİTAPLAR ---")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book.info()}")

    def find_book_by_title(self, title):
        title = title.strip().lower()
        for book in self.books:
            if book.title.lower() == title:
                return book
        return None


def menu():
    print("\n--- KÜTÜPHANE SİSTEMİ ---")
    print("1 - Kitapları listele")
    print("2 - Kitap ödünç al")
    print("3 - Kitap iade et")
    print("4 - Aldığım kitapları göster")
    print("5 - Çıkış")


def main():
    # örnek kitaplar
    library = Library()
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("Dune", "Frank Herbert"))
    library.add_book(Book("Sefiller", "Victor Hugo"))

    # örnek üye
    member = StudentMember("Cansu")
    library.add_member(member)

    while True:
        menu()
        secim = input("Seçim: ").strip()

        if secim == "1":
            library.list_books()

        elif secim == "2":
            library.list_books()
            kitap_adi = input("Ödünç almak istediğin kitabın adını yaz: ").strip()
            book = library.find_book_by_title(kitap_adi)

            if book is None:
                print("Bu isimde kitap bulunamadı.")
            else:
                member.borrow_book(book)

        elif secim == "3":
            member.list_borrowed_books()
            kitap_adi = input("İade etmek istediğin kitabın adını yaz: ").strip()

            # Üyenin listesinde arıyoruz
            book_to_return = None
            for b in member.borrowed_books:
                if b.title.lower() == kitap_adi.lower():
                    book_to_return = b
                    break

            if book_to_return is None:
                print("Bu kitap sende görünmüyor.")
            else:
                member.return_book(book_to_return)

        elif secim == "4":
            member.list_borrowed_books()

        elif secim == "5":
            print("Çıkış yapıldı.")
            break

        else:
            print("Hatalı seçim. Tekrar dene.")


main()
