score = 0
score = int(score)

#user
nama = input("Nama user?")
nama = nama.title()
print("""Halo {}, input angka untuk memilih jawaban yang ingin dipilih
Good luck!""".format(nama))

#pertanyaan1
print("""Indonesia memiliki berapa provinsi?
1. 35 
2. 37 
3. 38 
4. 40""")

jawaban1 = "3"
response1 = input("jawabanmu adalah:")

if (response1 != jawaban1):
    score = score
else:
    score = score + 50

#pertanyaan2
print("""Pulau terpadat di Indonesia?
1. Sumatra 
2. Papua 
3. Jawa 
4. Kalimantan""")

jawaban2 = "3"
response2 = input("jawabanmu adalah:")

if (response2 != jawaban2):
    score = score
else:
    score = score + 50

#mediumQuiz
print("Total scoremu adalah " + str(score))
if(score>50):
    medium = "ya"
    responeMedium = input("apakah kamu mau lanjut ke soal medium?(ya/tidak)\n")
    if(responeMedium == medium):
        score = 0
        score = int(score)
        print("Medium Quiz, Score kembali 0")
        print("""Ibukota Indonesia?\n"""
        """1. Surabaya\n"""
        """2. Semarang\n"""
        """3. Jakarta\n"""
        """4. Bandung""")

        jawabanMedium1 = "3"
        responseMedium1 = input("jawabanmu adalah:")

        if (responseMedium1 != jawabanMedium1):
            score = score
        else:
            score = score + 100
        print("Total scoremu adalah " + str(score))
    #tidakLanjutMedium
    else:
        print("goodbye {}!".format(nama))
#gagalEasyQuiz
else:
    print("Terima kasih sudah menjawab {}, maaf anda belum bisa masuk ke soal medium.\n"""
    """Silahkan coba lagi""".format(nama))
