array = []

n = int (input("enter number your length array "))

for i in range (0,n):
    adad = int (input("enter number "))
    array.append(adad)
arraye_sort = sorted(array)

if arraye_sort == array:
    print("moratab ast😉")

else:
    print("moratab nist😑", arraye_sort)