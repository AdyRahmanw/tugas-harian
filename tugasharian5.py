from datetime import datetime

data_login = {
    'admin': '1234',
    'user1': 'abcd',
    'user2': 'pass123',
}

rekap_login_db = []

def masukan_data():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    return username, password

def cek_login_username(username):
    return username in data_login

def cek_login_password(username, password):
    return password == data_login.get(username)

def status(username, password):
    if not cek_login_username(username):
        return "gagal: username tidak terdaftar"
    return "berhasil" if cek_login_password(username, password) else "gagal: password salah"

def format_waktu():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def rekap_login():
    username, password = masukan_data()
    hasil = {
        "username": username,
        "status": status(username, password),
        "waktu_login": format_waktu()
    }
    rekap_login_db.append(hasil)
    print("Data login tersimpan:", hasil)


rekap_login()
