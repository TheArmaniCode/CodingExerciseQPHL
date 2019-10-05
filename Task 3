#initialise counters for valid and invalid numbers
validNumbers = 0
invalidNumbers = 0

#create function for weighting values
def weighting(x):
    weight = 12 - x
    return weight

#create validation function
def validate(i, validNumbers, invalidNumbers):
    #catch exception for non integer values (string, float etc)
    try:
        int(i)
    except:
        invalidNumbers += 1
    else:
        #Check if not ten digits exactly
        if(len(i) != 10):
            invalidNumbers += 1
            #Check if negative number
        elif(float(i) < 0):
            invalidNumbers += 1
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
                    invalidNumbers += 1
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
                        invalidNumbers += 1
                    #else if result 11, keep expected value at 0
                    elif (result == 11):
                        expectedValue = 0
                    #else set result as expectedValue
                    else:
                        expectedValue = result
                    #compare expected value to 10th digit
                    if (expectedValue == digits[9]):
                        #if equal, correct value
                        validNumbers+= 1
                    #else false value
                    else:
                        invalidNumbers += 1
#creat empty array to store data
dataList = []

#scan text file, split into rows and eliminate quotation marks
with open('data.txt') as f:
  data = f.read().replace('"','').replace(',','\n')

#append data to dataList
for i in data:
    dataList.append(data)

#Validate each item in dataList
for i in dataList:
    validate(i, validNumbers, invalidNumbers)

#Print final totals when done
print("Valid Numbers : ", validNumbers)
print("Invalid Numbers : ", invalidNumbers)
