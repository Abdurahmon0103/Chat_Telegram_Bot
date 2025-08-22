# Foydalanuvchidan sonlar va amalni so'rash
malumot = input("Ikki son va amalni vergul bilan kiriting (masalan: 5,7,+): ")

# Ajratib olish
son1, son2, amal = malumot.split(",")

# Sonlarni float qilib olamiz (butun va kasr sonlar uchun)
son1 = float(son1)
son2 = float(son2)

# Amalni bajarish
if amal == "+":
    natija = son1 + son2
elif amal == "-":
    natija = son1 - son2
elif amal == "*":
    natija = son1 * son2
elif amal == "/":
    if son2 != 0:
        natija = son1 / son2
    else:
        natija = "Nolga bo'lish mumkin emas!"
else:
    natija = "Noto‘g‘ri amal kiritildi!"

print("Natija:", natija)
