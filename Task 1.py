#initialise i
i = ""
#initialise boolean to check program execution
exit = False
#create validation process inside while loop
while(exit == False):
    #initalise boolean to check correct value
    correctValue = False
    #input value & statement
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
                
                #if at least one digit doesn't match, valid number
                if (matchingDigits != 10):
                    correctValue = True
                    print(correctValue)
