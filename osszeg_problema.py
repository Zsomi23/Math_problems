"""What is the smallest number that, when added to the numbers before it, results in a total of X?"""
x = int(input("Please enter an integer.\n"))
y = 0

"""Sums the numbers from a to b."""
def szamolas(a, b):
    print(sum(range(a, b + 1)))

"""Binary method."""
def bin_mod():
    bin_x = bin(x)
    print(len(list(bin_x.split('0b')[1])))
"""It doesn't work."""

"""Halving"""
def felevezes(x, y):
    x = [y, x]
    for i in range(y, max(x)):
        if x[1] % 2 == 0:
            x = [x[1]//2+1, x[1]//2-1]
            print(x)
        else:
            x = [x[1]//2+1, x[1]//2]
            print(x)
"""It doesn't work."""


"""Summing method"""
def oszeados(x, y):
    szam_list = []
    z = y
    while z < x:
        y = y + 1
        z = z + y
        szam_list.append(y)
        # print(szam_list)
        # print((sum(range(szam_list[0], szam_list[-1]))+szam_list[-1])-x)
        if (sum(range(szam_list[0], szam_list[-1]))+szam_list[-1])-x > 0:
            szam_list.remove((sum(range(szam_list[0], szam_list[-1]))+szam_list[-1])-x)
            # print(szam_list)
            # print((sum(range(szam_list[0], szam_list[-1])) + szam_list[-1]) - x)
            print(print(f"Original number: {x}, the smallest number when summing the previous numbers: {szam_list[-1]}, the list: {szam_list}, the sum of numbers in the list: {sum(szam_list)}"))



"""It works."""
"""6 and 10 do not work."""

if __name__ == '__main__':
    # szamolas(1, 64)
    # bin_mod()
    # felevezes(x, y)
    oszeados(x, y)
