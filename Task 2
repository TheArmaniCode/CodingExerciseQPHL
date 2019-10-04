#initialise i
i = ""
#initialise exit boolean
exit = False
# create function for weighting values
def weighting(x):
    weight = 12 - x
    return weight
#create while loop to check validation
while(exit == False):
    #initalise boolean to check correct value
    correctValue = False
    i = input("Please input a value: ")
    #break if exit command entered
    if (i == "Exit"):
        exit = True
    else:
        #catch exception for non integer values (string, float etc)
        try:
            int(i)
        except:
            print(correctValue)
        else:
            #Check if not ten digits exactly
            if(len(i) != 10):
                print(correctValue)
            #Check if negative number
            elif(float(i) < 0):
                print(correctValue)
            else:
                #split number into digits & store in array
                digits = [int(x) for x in str(i)]

                #initialise value to count matching digits
                matchingDigits = 0

                #increment counter for each matching digit
                for j in digits:
                     if (digits[0] == j):
                        matchingDigits += 1

                #check if all digits match, no less
                if (matchingDigits == 10):
                    print(correctValue)
                else:
                    #initialise total
                    total = 0
                    #weight each digit and then add to result
                    for j in digits:
                        w = weighting(j)
                        total += w
                    #modulus total by 12 to find remainder
                    remainder = total%12
                    #subtract remainder from 12 to get result
                    result = 12 - remainder
                    #initialise expected value
                    expectedValue = 0
                    #if result 10 or 12, false value
                    if (result == 10 | result == 12):
                        print(correctValue)
                    #else if result 11, keep expected value at 0
                    elif (result == 11):
                        expectedValue = 0
                    #else set result as expectedValue
                    else:
                        expectedValue = result
                    #compare expected value to 10th digit
                    if (expectedValue == digits[9]):
                        #if equal, correct value
                        correctValue = true
                        print(correctValue)
                    #else false value
                    else:
                        print(correctValue)
