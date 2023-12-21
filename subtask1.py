def largestsquare():
    largestsquarenum = 0
    next_number_value = 1
    squarenum = 0 
    largestsquarenum = squarenum
    num = int(input("Enter a number: "))
    while True:
        if squarenum <= num:
            squarenum = next_number_value * next_number_value
            next_number_value = next_number_value + 1
        else:
            break
        largestsquarenum = squarenum
    print(squarenum)
largestsquare()
