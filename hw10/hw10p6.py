def count_characters():
    sequence = input("Nhập vào chuỗi ký tự: ")
    frequency = {}

    for char in sequence:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print("Tần suất xuất hiện của các ký tự trong chuỗi:")
    print(frequency)

count_characters()