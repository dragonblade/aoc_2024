#!/usr/bin/env python3


def a(line: str):
    disk = []
    n = 0
    occ = True
    for c in list(line.strip()):
        if occ:
            disk += [str(n)] * int(c)
            n += 1
        else:
            disk += ["."] * int(c)
        occ = not occ

    l, r = 0, len(disk) - 1
    while l < r:
        if disk[l] == ".":
            if disk[r] != ".":
                disk[l], disk[r] = disk[r], disk[l]
            else:
                r -= 1
        else:
            l += 1

    print(sum(i * int(c) for i, c in enumerate(disk) if c != "."))


def b(line: str):
    disk = []
    n = 0
    occ = True
    for c in list(line.strip()):
        if occ:
            disk += [(n, int(c))]
            n += 1
        else:
            disk += [(None, int(c))]
        occ = not occ

    r = len(disk) - 1
    while r > 0:
        if disk[r][0] is not None:
            l = 0
            while l < r:
                if disk[l][0] is None:
                    if disk[l][1] >= disk[r][1]:
                        if disk[l][1] == disk[r][1]:
                            disk[l], disk[r] = disk[r], disk[l]
                        else:
                            t = disk[r]
                            disk[r] = (None, t[1])
                            disk[l : l + 1] = [t, (None, disk[l][1] - t[1])]
                            r += 1
                        break
                l += 1
        r -= 1

    checksum = 0
    pos = 0
    for f, c in disk:
        for _ in range(c):
            if f is not None:
                checksum += f * pos
            pos += 1
    print(checksum)


if __name__ == "__main__":
    line = input()
    a(line)
    b(line)
