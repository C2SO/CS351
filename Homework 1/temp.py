# def all_fluffy(s):
input = input("What string you like to check? >>> ")
finalResult = True
for index, val in enumerate(input):
    if finalResult == True:
        if val in "fluffy":
            pass
        else:
            finalResult = False
    else:
        break
print(finalResult)