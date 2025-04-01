from random import*
#1
while True:
    try: 
        n=int(input("Mitu linnumajad (1-9) on vaja näita?"))
        if 1 <= n <= 9:
            break
        else:
            print("Viga! Number peab olema 1-9")
    except ValueError:
        print("Viga! On vaja kirjutada täisarv 1-9")
linnumaja= [
    "  -----  ",
    " |  O  | ",
    " !  -  ! ",
    "  -----  "
    ]
for line in linnumaja:
    print((line + " ") * n)

#2
while True:
    try:
        n = int(input("Sisesta arv n: "))  # Ввод n
        p = int(input("Sisesta astendaja p: "))  # Ввод p
        if n > 0 and p > 0:
            break
        else:
            print("Viga: sisesta naturaalarvud (suurem kui 0).")
    except ValueError:
        print("Viga: palun sisesta täisarv.")

limit = n ** 3  # Ülemine piir
num = 1  # Alustame 1-st

while num ** p <= limit:
    print(num ** p, end=" ")  # Väljasta arvu aste
    num += 1

#3

num_students = random.randint(10, 30)  # случайное количество учеников от 10 до 30
marks = [random.randint(2, 5) for _ in range(num_students)]  # случайные оценки от 2 до 5

average = sum(marks) / len(marks) if marks else 0

print(f"Оценки учеников: {marks}")
print(f"Средняя оценка: {average:.2f}")
#4
age = 1
gift = 1
while gift <= 100:
    age += 1
    gift += age
print(f"Kingitus ületas 100$ {age}-aastaselt.")

#5
n1, n2 = 0, 1
print(n1, n2, end=" ")
for _ in range(7):
    n1, n2 = n2, n1 + n2
    print(n2, end=" ")
print()