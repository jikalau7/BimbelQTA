def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi nol"
    return a / b

if __name__ == "__main__":
    print("Tambah:", tambah(10, 5))
    print("Kurang:", kurang(10, 5))
    print("Kali:", kali(10, 5))
    print("Bagi:", bagi(10, 5))
