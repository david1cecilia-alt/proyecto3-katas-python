
def es_anagrama(palabra1, palabra2):
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()

    return sorted(p1) == sorted(p2)

if __name__ == "__main__": print(es_anagrama("amor", "roma"))