import sys
import locale

from figdate import date


def main():
    locale.setlocale(locale.LC_TIME, "ru_RU.utf8")

    if len(sys.argv) == 2:
        date(format=sys.argv[1])
    elif len(sys.argv) == 3:
        date(format=sys.argv[1], font=sys.argv[2])
    else:
        date()


if __name__ == "__main__":
    main()
