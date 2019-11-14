secret = "ngeh"
guess = ""

while guess != secret:
    guess = (input("Masukkan Kata : "))
    print("Wrong")
    if guess == 3:
        exit()

print("Sukses")