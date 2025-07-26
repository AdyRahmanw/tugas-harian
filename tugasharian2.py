percobaan = 0

while percobaan < 3 :
    Username = input(str("Masukan Username: " ))
    Password = input(str("Masukan Password: "))
    percobaan += 1
    
    if Username == "admin" and Password == "1234":
        print("login berhasil")
    else:
        print ("Coba lagi data tidak sesuai")
print("gagal akun terkunci")

