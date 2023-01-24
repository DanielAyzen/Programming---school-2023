#Exercise 1
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
    if element < 5:
      print (element)

# Сдался и скопировал с файла. Хотел посмотреть, какой такой второй способ. :)
print(list(filter(lambda elem: elem < 5, a))) 

"""

#Exercise 2
"""
year = int (input ("Enter year: "))

if year % 4 == 0:
    print ("Leap year is in 4 years")

elif (year + 3) % 4 == 0:
    print ("Leap year is in 3 years")

elif (year + 2) % 2 == 0:
    print ("Leap year is in 2 years")

elif (year + 1) % 2 == 0:
    print ("Leap year is in 1 years")
"""

#Exercise 3
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def match_elements(a, b):
    match = []
    for i in a:
        if i in b:
            match.append(i)
    return match
       
match = match_elements(a,b)
print("Match elements: ", match)
"""



