def sumMinMean():
    counter = 0
    sum = 0
    minin = list()
    meanval = 0

    try:
        num = int(input("Enter a number: "))
        counter = counter + 1
    except ValueError:
        counter = None
                
    if counter == None:
        minin = -1
        meanval = -1        
    else:
        while(num != -1):
            sum = sum + num
            counter = counter + 1
            minin.append(num)
            num = int(input("Enter a number: "))
        meanval = sum/counter
        minin = min(minin)
    print("Mean value: ", meanval)
    print("Minimum Value: ", minin)
sumMinMean()
