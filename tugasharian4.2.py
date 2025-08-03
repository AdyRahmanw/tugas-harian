
data_login ={
    'admin': '1234',
    'user1': 'abcd',
    'user2': 'pass123',
}

percobaan = 0
def masukan_data():
    username = input("Masukan Username: " )
    password = input("Masukan Password: ")
    return username, password

def cek_login_username(username):
    return username in data_login

def cek_login_password(username,password):
    return password == data_login[username]

        
while percobaan < 3 :
    username, password = masukan_data()
    cek_username = cek_login_username(username)
  
    
    if cek_username:
        cek_password = cek_login_password(username,password)
        if cek_password:
            print("login berhasil")
            break
        else:
            print("password salah")
    else:
        print("username tidak ditemukan")
    
    percobaan += 1

if percobaan >= 3:
    print("gagal akun terkunci")