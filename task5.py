# Name: Yanuar Audi Nugraha
# NIM: 221402137
# Tugas 1 Pemrograman Integrative Com C
# Soal 5

nominal = 0

number = int(input("Insert your number: "))

while True :
    nominal += number
    number = int(input("Insert your number: "))
    if number == -1:
        break
print("The sum of the entered numbers is:", nominal)
