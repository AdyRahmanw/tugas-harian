DataLogin = {
    'admin': '1234',
    'user1': 'abcd',
    'user2': 'pass123'
}

def cek_login():
    percobaan = 0
    while percobaan < 3:
        username = input("Masukan Username: ")
        password = input("Masukan Password: ")
        percobaan += 1

        if username in DataLogin:
            if password == DataLogin[username]:
                return "Login berhasil"
            else:
                print(f"password salah")
        else:
            print("username salah")

    return "Gagal, akun terkunci."

hasil = cek_login()
print(hasil)