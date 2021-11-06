from binascii import hexlify



def Calamity(p: str):
    if not p:
        print(None)
        return 'None'

    l = len(p)*sum(int(i) for i in str(bin(int("".join(str(ord(c)) for c in p)))[2:]))

    p = "".join(chr(ord(char)+l) for char in p)
    p = "".join(hexlify(char.encode('utf-8')).decode() for char in p)
    p = "".join(i if i in '1234567890' else '' for i in p)
    p = "".join(chr(int(char) + l) for char in p)
    p = "".join(str(ord(char) + l) for char in p)

    return p


def main():
    print("Hashed: " + hash(input("-> ")))


if __name__ == '__main__':
    while True:
        main()
