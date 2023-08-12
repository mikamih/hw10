numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

user_input = input("Input a Roman number: ")

if user_input in numbers:
    arabic_number = numbers[user_input]
    print("Arabic number:", arabic_number)
else:
    print("Not found")