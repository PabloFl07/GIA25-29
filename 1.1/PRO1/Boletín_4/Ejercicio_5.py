str1 = str(input("String 1: "))
str2 = str(input("String 2: "))


def formatt(str1 , str2 ):
    return str2[:2] + str1[2] + " " + str1[:2] + str2[2]

print(formatt(str1 , str2))