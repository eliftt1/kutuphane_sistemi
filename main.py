from services.library import Library
from ui.menu import Menu


def main():
    library = Library()
    menu = Menu(library)
    menu.run()


if __name__ == "__main__":
    main()