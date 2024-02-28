# Name: Yanuar Audi Nugraha
# NIM: 221402137
# Tugas 1 Pemrograman Integrative Com C
# Soal 3

number = int(input("Insert your number: "))

if number < 100 :
    size = "Small"
elif number > 200 :
    size = "Large"
else :
    size = "Medium"
    
    print("Your number which is",number, "are", size)