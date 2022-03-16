import collections


class Spiral:
    def __init__(self, text=""):
        self.elems = collections.Counter(text)

    def __iter__(self):
        return self.elems.elements()

    def __add__(self, other):
        return type(self)(self.elems + other.elems)

    def __sub__(self, other):
        return type(self)(self.elems - other.elems)

    def __mul__(self, cnt):
        return type(self)(list(self) * cnt)

    __rmul__ = __mul__

    def __len__(self):
        return sum(self.elems.values())

    def _show(self):
        (diffx, diffy) = ((0, 1, 0, -1), (1, 0, -1, 0))
        funct = {}
        X = Y = n = k = j = mx = MaxX = MinY = MaxY = 0
        for (idx, el) in enumerate(self):
            funct[X, Y] = el
            (mx, MinY, MaxX, MaxY) = (
                min(mx, X),
                min(MinY, Y),
                max(MaxX, X),
                max(MaxY, Y),
            )
            if idx >= n:
                k += 1
                n += k
                j = (j + 1) % 4
            (X, Y) = (X + diffx[j], Y + diffy[j])
        return (funct, (mx, MaxX), (MinY, MaxY))

    def __str__(self):
        (funct, (mx, MaxX), (MinY, MaxY)) = self._show()
        return "\n".join(
            (
                "".join((funct.get((X, Y), " ") for X in range(mx, MaxX + 1)))
                for Y in range(MinY, MaxY + 1)
            )
        )


def master():
    (First, Second) = (Spiral("QWERTY" * 2), Spiral("asdf" * 3))
    print(First + Second)


if __name__ == "__main__":
    master()
