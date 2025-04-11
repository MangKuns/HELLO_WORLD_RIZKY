# Hello World Main Blowing
print("🔥 Hello World from Main Blowing 🔥\n")

def input_identitas():
    data = []
    print("== Masukkan 5 Identitas ==")
    for i in range(5):
        print(f"Identitas ke-{i+1}")
        nama = input("Nama: ")
        umur = input("Umur: ")
        email = input("Email: ")
        data.append({
            "nama": nama,
            "umur": umur,
            "email": email
        })
        print()
    return data

# Contoh pemanggilan
# data = input_identitas()
