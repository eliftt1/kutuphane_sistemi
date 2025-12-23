from services.library import Library

def run_tests():
    print("=== KÜTÜPHANE KİTAP ARAMA SİSTEMİ TESTLERİ ===\n")

    library = Library()

    # 1. Başlangıç Kontrolü
    print("1. Başlangıç Kontrolü")
    if len(library.books) == 0:
        print("✔ Liste başlangıçta boş\n")
    else:
        print("✘ Liste boş değil\n")

    # 2. Veri Ekleme Testi
    print("2. Veri Ekleme Testi")
    library.add_book("Sefiller", "Victor Hugo", 1862)
    library.add_book("Suç ve Ceza", "Dostoyevski", 1866)

    if len(library.books) == 2:
        print("✔ Kitaplar başarıyla eklendi\n")
    else:
        print("✘ Kitap ekleme hatalı\n")

    # 3. Listeleme Testi
    print("3. Listeleme Testi")
    print("Beklenen kitaplar:")
    print("- Sefiller | Victor Hugo | 1862")
    print("- Suç ve Ceza | Dostoyevski | 1866\n")

    print("Gerçek çıktı:")
    library.list_books()
    print("✔ Listeleme çalıştı\n")

    # 4. Arama Testi (İsim)
    print("4. Arama Testi (İsme Göre)")
    results_name = [b for b in library.books if "sefiller" in b.name.lower()]
    if len(results_name) == 1:
        print("✔ İsme göre arama başarılı\n")
    else:
        print("✘ İsme göre arama başarısız\n")

    # 4. Arama Testi (Yazar)
    print("4. Arama Testi (Yazara Göre)")
    results_author = [b for b in library.books if "hugo" in b.author.lower()]
    if len(results_author) == 1:
        print("✔ Yazara göre arama başarılı\n")
    else:
        print("✘ Yazara göre arama başarısız\n")

    # 5. Silme Testi
    print("5. Silme Testi")
    library.remove_book("Sefiller")

    results_after_delete = [b for b in library.books if "sefiller" in b.name.lower()]
    if len(results_after_delete) == 0:
        print("✔ Kitap başarıyla silindi\n")
    else:
        print("✘ Kitap silme başarısız\n")

    print("=== TÜM TESTLER TAMAMLANDI ===")

if __name__ == "__main__":
    run_tests()
