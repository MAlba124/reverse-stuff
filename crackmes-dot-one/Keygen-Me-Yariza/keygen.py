# Challange from:
# https://crackmes.one/crackme/60c24a7133c5d410b8842d3c

from random import choice, randint

chars: str = "abcdefghijklmnopqrstuvwxyz"
chars += chars.upper()
chars += "12334567890"

def randomKey(length: int) -> str:
    return "".join(choice(chars) for _ in range(length))

def validate(key: str) -> str:
    key_array = list(key)
    key_array.insert(4, '@')
    key_array.insert(6, '-')
    key_array.insert(9, 'l')
    key_array.insert(15, '?')
    return "".join(c for c in key_array)

def main() -> None:
    print("Generating 50 valid keys...")
    for i in range(1, 51):
        print("[ %d ] -> %s" % (i, validate(randomKey(randint(13, 17)))))


if __name__ == "__main__":
    main()
