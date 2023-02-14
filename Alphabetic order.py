str = input("please enter ur string: ")
if str.isalpha():

    longest = str[0]
    current = str[0]
    # i want to compare each element with the previous one
    for i in str:
        if i > current[-1]:
            current += i
            if len(current) > len(longest):
                longest = current
        else:
            current = i
    print("Longest substring in alphabetical order is:", longest)
else:
    print("unvalid input")
