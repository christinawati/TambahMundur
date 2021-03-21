x = print(int(input("Masukkan angka 1: ")))
y = print(int(input("Masukkan angka 2: ")))
print("nilai x sebelum di swap: {}".format(x))
print("nilai y sebelum di swap: {}".format(y))


#function tambah mundur
def tambahMundur(x, y):
    y,x = x,y
    if x.isnumeric() and x <= 359999:
        z = x + y
    else:
        print("Invalid Input!")

    return tambahMundur

#reverse the number
n = z
reverse = 0

while (n > 0):
    a = n % 10
    reverse = reverse * 10 + a
    n = n // 10
print(reverse)