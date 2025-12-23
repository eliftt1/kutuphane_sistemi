class Menu:
    def __init__(self, library):
        self.library = library

    def show_menu(self):
        print("\n--- KÜTÜPHANE KİTAP ARAMA SİSTEMİ ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Ara (İsme Göre)")
        print("4. Kitap Ara (Yazara Göre)")
        print("5. Tüm Kitapları Listele")
        print("6. Çıkış")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Seçiminizi giriniz (1-6): ")

            if choice == "1":
                name = input("Kitap adı: ")
                author = input("Yazar adı: ")

                try:
                    year = int(input("Yayın yılı: "))
                except ValueError:
                    print("Yayın yılı sayı olmalıdır.")
                    continue

                self.library.add_book(name, author, year)

            elif choice == "2":
                name = input("Silinecek kitabın adı: ")
                self.library.remove_book(name)

            elif choice == "3":
                name = input("Aranacak kitap adı: ")
                self.library.search_by_name(name)

            elif choice == "4":
                author = input("Aranacak yazar adı: ")
                self.library.search_by_author(author)

            elif choice == "5":
                self.library.list_books()

            elif choice == "6":
                print("Programdan çıkılıyor...")
                break

            else:
                print("Geçersiz seçim. Lütfen 1-6 arasında bir değer giriniz.")