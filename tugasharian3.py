
DataLogin ={
    'admin': '1234',
    'user1': 'abcd',
    'user2': 'pass123'
}

percobaan = 0

while percobaan < 3 :
    Username = input(str("Masukan Username: " ))
    Password = input(str("Masukan Password: "))
    percobaan += 1
    
    if Username in DataLogin:
        if Password == DataLogin[Username]:
            print("login berhasil")
            break
        else:
            print("pasword salah")
    else:
        print("username tidak ada")

if percobaan >= 3:
    print("gagal akun terkunci")