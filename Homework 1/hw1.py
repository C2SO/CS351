#CS351 -- HW1
# Nicholas Rahbany


def greatest_difference(nums1, nums2):
    maxlength = 0
    if len(nums1) == len(nums2):
        for index, val in enumerate(nums1):
            length = 0
            if val < nums2[index]:
                length = int(nums2[index]) - int(val)
            else:
                length = int(val) - int(nums2[index])
            if length > maxlength:
                maxlength = length
        print("Maxlength: ", maxlength)
    else:
        print("List sizes do not match")


def can_pay_with_two_coins(denoms, amount):
    # amount = int(input("What amount would you like to check? >>> "))
    # denomInput = input("What are the denomminators? >>> ")
    # denoms = list(map(int, denomInput.split()))
    finalAmount = amount
    finalResult = False
    index = 3
    while index >= 0:
        if finalResult == False:
            finalAmount = finalAmount - int(denoms[index])
            newIndex = index
            secondCoin = False
            while newIndex >= 0:
                if finalAmount == int(denoms[newIndex]):
                    finalResult = True
                    break
                else:
                    newIndex -= 1
            index -= 1
            finalAmount = amount
        else:
            break
    print(finalResult)


def all_fluffy(s):
    # input = input("What string you like to check? >>> ")
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


def digital_sum(nums_list):
    # nums_list = input("What string you like to check? >>> ")
    print(sum(int(x) for x in nums_list if x.isdigit()))


def count_collatz_steps(n):
    # n = int(input("Input a number >>> "))
    totalSteps = 0
    while n != 1:
        if (n % 2 == 0):
            n = n/2
            totalSteps += 1
        else:
            n = (3*n)+1
            totalSteps += 1
    print(totalSteps)
