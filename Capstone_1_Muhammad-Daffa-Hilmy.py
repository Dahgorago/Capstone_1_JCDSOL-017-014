import re

# Database awal
database = [
    {"id": 1, "nama": "Fadhil Faruq", "gender": "Pria", "tanggal_lahir": "1990-01-01",
     "alamat": "Jl.Kedoya", "status": "Perawatan", "telepon": "08123456789"},
    {"id": 2, "nama": "Aisya Fara", "gender": "Wanita", "tanggal_lahir": "1985-05-15",
     "alamat": "Jl.Tomang Raya", "status": "Sembuh", "telepon": "08198765432"},
    {"id": 3, "nama": "Alfan Ul-haq", "gender": "Pria", "tanggal_lahir": "1978-12-12",
     "alamat": "Jl.Kebon Jeruk", "status": "Meninggal", "telepon": "08134567890"}
]

# Login credentials
USERNAME = "admin"
PASSWORD = "1234"

# Fungsi login
def login():
    while True:  # Loop terus sampai login berhasil
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        if username == USERNAME and password == PASSWORD:
            print("Login berhasil!\n")
            return True  # Keluar dari loop jika login berhasil
        else:
            print("Login gagal. Silakan coba lagi.\n")


# SEBELUM MENGGUNAKAN REGEX UNTUK VALIDASI INPUT
# def validate_id(prompt, error_message):
#     while True:
#         value = input(prompt)
#         if value.isdigit():
#             return int(value)
#         print(error_message)

# def is_valid_name(name):
#     name = name.strip()
#     if len(name) > 100:
#         return False
#     # Memeriksa setiap karakter dalam nama
#     for char in name:
#         if not (char.isalpha() or char == ' ' or char == "'" or char == "-"):
#             return False
#     return True

# def validate_input_manual(prompt, error_message):
#     while True:
#         value = input(prompt)
#         if is_valid_name(value):
#             return value
#         print(error_message)

# def validate_gender(prompt, error_message):
#     while True:
#         value = input(prompt).strip()
#         if value in ["Pria", "Wanita"]:
#             return value
#         print(error_message)

# def validate_date(prompt, error_message):
#     while True:
#         value = input(prompt).strip()
#         parts = value.split('-')
#         if len(parts) == 3 and all(part.isdigit() for part in parts):
#             year, month, day = map(int, parts)
#             if 1 <= month <= 12 and 1 <= day <= 31:  # Sederhana, tidak validasi bulan panjang
#                 return value
#         print(error_message)

# def validate_status(prompt, error_message):
#     while True:
#         value = input(prompt).strip()
#         if value in ["Sembuh", "Perawatan", "Meninggal"]:
#             return value
#         print(error_message)

# def validate_phone(prompt, error_message):
#     while True:
#         value = input(prompt).strip()
#         if value.startswith("08") and value[2:].isdigit() and 9 <= len(value) <= 12:
#             return value
#         print(error_message)



# Fungsi validasi input
def validate_input(prompt, pattern, error_message):
    while True:
        value = input(prompt)
        if re.fullmatch(pattern, value):
            return value
        print(error_message)



# Fungsi untuk menampilkan database dalam bentuk tabel
def display_table(data):
    if not data:
        print("Tidak ada data untuk ditampilkan.")
        return

    # Header tabel
    headers = ["ID", "Nama Pasien", "Gender", "Tanggal Lahir", "Alamat", "Status", "Telepon"]
    print("=" * 90)
    print(f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<10} {headers[3]:<15} {headers[4]:<15} {headers[5]:<10} {headers[6]:<15}")
    print("=" * 90)

    # Isi tabel
    for patient in data:
        print(f"{patient['id']:<5} {patient['nama']:<20} {patient['gender']:<10} {patient['tanggal_lahir']:<15} {patient['alamat']:<15} {patient['status']:<10} {patient['telepon']:<15}")
    print("=" * 90)

# Fungsi untuk membaca database
def read_data():
    while True:
        print("\n=== Read Data ===")
        print("1. Lihat semua data pasien")
        print("2. Cari data pasien berdasarkan ID")
        print("3. Kembali ke menu utama")
        choice = input("Pilih opsi: ")
        if choice == "1":
            print("\nDaftar Pasien:")
            display_table(database)
        elif choice == "2":
            patient_id = validate_input("Masukkan ID pasien: ", r"\d+", "ID harus berupa angka.")
            patient = next((p for p in database if p["id"] == int(patient_id)), None)
            if patient:
                print("\nData Pasien:")
                display_table([patient])
            else:
                print("Pasien tidak ditemukan.")
        elif choice == "3":
            return
        else:
            print("Opsi tidak valid.")



# Fungsi untuk menambahkan data baru
def add_patient():
    print("\n=== Tambah Data Pasien ===")
    new_id = max([p["id"] for p in database], default=0) + 1
    nama = validate_input("Masukkan nama pasien: ",r"[A-Za-z' -]{1,100}","Nama hanya boleh mengandung huruf, spasi, tanda petik tunggal (') atau tanda hubung (-)")
    gender = validate_input("Masukkan gender (Pria/Wanita): ", r"Pria|Wanita", "Gender hanya bisa 'Pria' atau 'Wanita'.")
    tanggal_lahir = validate_input("Masukkan tanggal lahir (YYYY-MM-DD): ", r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", "Format tanggal tidak valid.")
    alamat = input("Masukkan alamat: ")
    status = validate_input("Masukkan status (Sembuh/Perawatan/Meninggal): ", r"Sembuh|Perawatan|Meninggal","Status hanya bisa 'Sembuh', 'Perawatan', atau 'Meninggal'.")
    telepon = validate_input("Masukkan nomor telepon: ", r"08\d{9,12}", "Nomor telepon tidak valid.")
    database.append({
        "id": new_id,
        "nama": nama,
        "gender": gender,
        "tanggal_lahir": tanggal_lahir,
        "alamat": alamat,
        "status": status,
        "telepon": telepon
    })
    print("Data pasien berhasil ditambahkan.")

# Fungsi untuk menu tambah data pasien
def create_data():
    while True:
        print("\n=== Create Data ===")
        print("1. Tambah data pasien baru")
        print("2. Kembali ke menu utama")
        choice = input("Pilih opsi: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            return
        else:
            print("Opsi tidak valid.")



# Fungsi untuk memperbarui data pasien
def update_patient():
    print("\n=== Update Data Pasien ===")
    patient_id = validate_input("Masukkan ID pasien: ", r"\d+", "ID harus berupa angka.")
    patient = next((p for p in database if p["id"] == int(patient_id)), None)
    if not patient:
        print("Pasien tidak ditemukan.")
        return
    print("\nData Lama:")
    display_table([patient])

    print("\nMasukkan data baru, jika input tidak valid data tidak akan diubah. (Kosongkan untuk tidak mengubah)")

    nama = input("Nama pasien baru (hanya boleh huruf,spasi dan tanda baca (')(-): ")
    if nama.strip() and re.fullmatch(r"[A-Za-z' -]{1,100}",nama):  
        patient["nama"] = nama.strip()

    gender = input("Gender baru (Pria/Wanita): ")
    if gender in ["Pria", "Wanita"]:
        patient["gender"] = gender

    tanggal_lahir = input("Tanggal lahir baru (YYYY-MM-DD): ")
    if tanggal_lahir.strip() and re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", tanggal_lahir):
        patient["tanggal_lahir"] = tanggal_lahir

    alamat = input("Alamat baru: ")
    if alamat.strip():  
        patient["alamat"] = alamat.strip()

    status = input("Status baru (Sembuh/Perawatan/Meninggal): ")
    if status in ["Sembuh", "Perawatan", "Meninggal"]:
        patient["status"] = status

    telepon = input("Nomor telepon baru (dimulai dengan '08'): ")
    if telepon.strip() and re.fullmatch(r"08\d{9,12}", telepon):  # Nomor telepon valid
        patient["telepon"] = telepon.strip()

    print("\nData pasien berhasil diperbarui.")
    print("\nData Baru:")
    display_table([patient])

# Fungsi menu update data pasien
def update_data():
    while True:
        print("\n=== Update Data ===")
        print("1. Ubah data pasien")
        print("2. Kembali ke menu utama")
        choice = input("Pilih opsi: ")
        if choice == "1":
            update_patient()
        elif choice == "2":
            return
        else:
            print("Opsi tidak valid.")



# Fungsi untuk menghapus data pasien
def delete_data():
    while True:
        print("\n=== Hapus Data Pasien ===")
        print("1. Hapus data pasien")
        print("2. Kembali ke main menu")
        choice = validate_input("Pilih opsi: ", r"[1-2]", "Pilihan harus berupa angka 1 atau 2.")

        if choice == "1":
            patient_id = validate_input("Masukkan ID pasien yang ingin dihapus: ", r"\d+", "ID harus berupa angka.")
            patient = next((p for p in database if p["id"] == int(patient_id)), None)

            if not patient:
                print("Pasien tidak ditemukan.")
            else:
                print("\nData Pasien yang Akan Dihapus:")
                display_table([patient])
                confirm = validate_input("Apakah Anda yakin ingin menghapus data ini? (yes/no): ", r"yes|no",
                                         "Input hanya bisa 'yes' atau 'no'.")
                if confirm == "yes":
                    database.remove(patient)
                    print("Data pasien berhasil dihapus.")
                else:
                    print("Data pasien tidak jadi dihapus.")
        elif choice == "2":
            print("Kembali ke menu utama.")
            break



# Menu utama
def main_menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Membaca Data Pasien Rumah Sakit")
        print("2. Menambahkan Data Pasien Rumah Sakit")
        print("3. Mengubah Data Pasien Rumah Sakit")
        print("4. Menghapus Data Pasien Rumah Sakit")
        print("5. Keluar dari Program")
        choice = input("Pilih opsi: ")
        if choice == "1":
            read_data()
        elif choice == "2":
            create_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

# Eksekusi program
if login():
    main_menu()
        
