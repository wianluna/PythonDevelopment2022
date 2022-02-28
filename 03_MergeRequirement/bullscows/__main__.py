import sys
import urllib.request

from bullscows import ask, gameplay, inform


def main():
    words_list = urllib.request.urlopen(sys.argv[1])
    words_len = 0
    if len(sys.argv) == 3:
        words_len = sys.argv[2]

    words = []
    for w in words_list:
        word = w.decode("utf-8").strip()
        if words_len == 0 or len(word) == words_len:
            words.append(word)

    print(gameplay(ask=ask, inform=inform, words=words))


if __name__ == "__main__":
    main()
