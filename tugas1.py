class Login:
    def __init__(self):
        self.akun ={
            "admin": "1234",
            "user1": "abcd",
            "user2": "pass123"
        }
        self.nama = None
        self.password = None
    
    def Login(self):
        percobaan = 0
        
        while percobaan < 3:
            self.nama =input("masukan nama: ")
            self.password = str(input("masukan password: "))
                 
            percobaan +=1
            
            if self.nama in self.akun:
                if self.password == self.akun[self.nama]:
                    print("Login berhasil")
                    return True
                else:
                    print("Password salah")
            else:
                print("username tidak ditemukan")
        
User1 = Login()
User1.Login()