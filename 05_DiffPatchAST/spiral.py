import collections


class Spiral:
    def __init__(self, string=""):
        # Just use collections
        self.cells = collections.Counter(string)

    def __iter__(self):
        # Iterator
        return self.cells.elements()

    def __add__(self, other):
        # Sum
        return type(self)(self.cells + other.cells)

    def __sub__(self, other):
        # Diff
        return type(self)(self.cells - other.cells)

    def __mul__(self, num):
        # Multiplication
        return type(self)(list(self) * num)

    __rmul__ = __mul__

    def __len__(self):
        # Legnth
        return sum(self.cells.values())

    def _square(self):
        # Output
        dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
        F = {}
        x = y = n = k = j = mx = Mx = my = My = 0
        for i, c in enumerate(self):
            F[x, y] = c
            mx, my, Mx, My = min(mx, x), min(my, y), max(Mx, x), max(My, y)
            if i >= n:
                k += 1
                n += k
                j = (j + 1) % 4
            x, y = x + dx[j], y + dy[j]
        return F, (mx, Mx), (my, My)

    def __str__(self):
        # Stringify
        F, (mx, Mx), (my, My) = self._square()
        return "\n".join(
            "".join(F.get((x, y), " ") for x in range(mx, Mx + 1))
            for y in range(my, My + 1)
        )


def main():
    # This is main function
    A, B = Spiral("QWERTY" * 2), Spiral("asdf" * 3)
    print(A + B)


if __name__ == "__main__":
    main()
