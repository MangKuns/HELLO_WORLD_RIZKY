# Hello World Main Blowing
print("🔥 Hello World from Main Blowing 🔥\n")

def validasi_identitas(data):
    print("== Validasi Data Identitas ==")
    for idx, identitas in enumerate(data):
        errors = []
        if not identitas["nama"].isalpha():
            errors.append("Nama tidak valid (hanya boleh huruf)")
        if not identitas["umur"].isdigit() or not (0 < int(identitas["umur"]) < 120):
            errors.append("Umur tidak valid (1-119)")
        if "@" not in identitas["email"]:
            errors.append("Email tidak valid")

        if errors:
            print(f"Identitas ke-{idx+1} ada kesalahan:")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"Identitas ke-{idx+1} valid.")
        print()

# Contoh pemanggilan (asumsi sudah punya data)
# validasi_identitas(data)
