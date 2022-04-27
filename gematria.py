# https://en.wikipedia.org/wiki/Gematria

# this maps from Hebrew characters to their corresponding values.
mapping = {
    "aleph": 1,
    "bet": 2,
    "gimel": 3,
    "dalet": 4,
    "he": 5,
    "vav": 6,
    "zayin": 7,
    "het": 8,
    "tet": 9,
    "yod": 10,
    "kaf": 20,
    "lamed": 30,
    "mem": 40,
    "nun": 50,
    "samekh": 60,
    "ayin": 70,
    "pe": 80,
    "tsadi": 90,
    "kof": 100,
    "resh": 200,
    "shin": 300,
    "tav": 400,
}

# this maps from the last 5 characters in the Hebrew alphabet to their corresponding values.
final_mapping = {
    "kaf": 500,
    "mem": 600,
    "nun": 700,
    "pe": 800,
    "tsadi": 900,
}


def gematria_loop(characters):
    """Calculate the gematria for a word using a loop"""
    result = 0
    for c in characters:
        result += mapping[c]
    return result


def gematria(characters):
    """Calculate the gematria for a word using a comprehension"""
    return sum(mapping[c] for c in characters)


def gematria_mispar_gadol(characters):
    """Calculate the gematria for a word using the dictionary get() method"""
    return sum(final_mapping.get(c, mapping[c]) if i == len(characters)-1 else mapping[c] for i, c in enumerate(characters))


snake = "dalet resh kof vav nun"
satan = "he shin tet nun"
alive = "het yod"
benjamin = "bet nun yod mem yod nun"

print("Standard encoding:")
print(gematria(snake.split()))
print(gematria(satan.split()))
print(gematria(alive.split()))
print(gematria(benjamin.split()))

print("Mispar gadol encoding:")
print(gematria_mispar_gadol(snake.split()))
print(gematria_mispar_gadol(satan.split()))
print(gematria_mispar_gadol(alive.split()))
print(gematria_mispar_gadol(benjamin.split()))
