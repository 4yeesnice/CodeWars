'''                                                                                                              
           |/////////////////////////////////////////////////////////////////////////////////////////////////|
           |Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria: |
           |Any digit followed by all zeros: 100, 90000                                                      |
           |Every digit is the same number: 1111                                                             |
           |The digits are sequential, incementing†: 1234                                                    |
           |The digits are sequential, decrementing‡: 4321                                                   |
           |The digits are a palindrome: 1221 or 73837                                                       |
           |The digits match one of the values in the awesome_phrases array                                  |
           |† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.               |
           |† For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.               |       
           |/////////////////////////////////////////////////////////////////////////////////////////////////|
'''

number = "255"
awesome_phrases = [1337,256]
def test_2(number, awesome_phrases):
    if int(number) in awesome_phrases:
        return 2

    else:
        for i in awesome_phrases:
            if abs(i-int(number))<=2:
                return 1
                break
            else:
                pass


'''

|-----------------------|
|check for same number  |
|-----------------------|

'''
def same_number(number):
    if len(number)==2:
        return 0
    elif number[1:]==("0"*(len(number[1:]))):
        return 2
    elif len(set(number))==1:
        return 2
    else:
        return 0


'''

|-----------------------|
|check for incrementing |
|-----------------------|

'''

def incrementing(number):
    if len(number)==2:
        return 0
    count = 0
    if number[::-1][0]=="0":
        number = number[:len(number)-1]
    while count!=len(number) and len(number)!=1 and len(number)!=2:
        for i in number:
            if count == len(number)-1 and len(number)!=1:
                return 2
                break
            elif int(number[number.index(i)+1])-int(number[number.index(i)])==1 and len(number)!=1:
                count+=1
                pass
            else:
                
                break
        break


'''

|-----------------------|
|check for decrementing |
|-----------------------|

'''

def decrementing(number):
    if len(number)==2:
        return 0

    count = 0
    while count!=len(number) and len(number)!=1 and len(number)!=2:
        for i in number:
            if count == len(number)-1:
                return 2
                break
            elif int(number[number.index(i)])-int(number[number.index(i)+1])==1:
                count+=1
                pass
            elif len(number)==1:
                break
            else:
                break
        break

def palindrome(number):
    if len(number)==2:
        return 0
    if len(number)!=1:
        temp=int(number)
        rev=0
        while(int(number)>0):
            dig=int(number)%10
            rev=rev*10+dig
            number=int(number)//10
        if(temp==rev):
            return 2
        else:
            return 0
    else:
        return 0


if test_2(number, awesome_phrases)==2 or same_number(number) or palindrome(number)==2 or incrementing(number)==2 or decrementing(number)==2:
    print(2)
elif test_2(str(int(number)+2), awesome_phrases)==1 or same_number(str(int(number)+2)) or incrementing(str(int(number)+2))==2 or decrementing(str(int(number)+2)) or palindrome(str(int(number)+2)):
    print(1)
elif test_2(str(int(number)+1), awesome_phrases)==1 or same_number(str(int(number)+1)) or incrementing(str(int(number)+1))==2 or decrementing(str(int(number)+1)) or palindrome(str(int(number)+1)):
    print(1)
else:
    if len(number)==2:
        print(0)
    else: 
        print(0)

def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0


#NOTE the code down below is the same as non-commented one. The difference is "return" instead of print and code down below is 1 function containing mupltiple functions.

# def is_interesting(number, awesome_phrases):
#     number = str(number)
#     def test_2(number, awesome_phrases):
#         if len(number)<=2:
#             return 0
#         if int(number) in awesome_phrases:
#             return 2

#         else:
#             for i in awesome_phrases:
#                 if abs(i-int(number))<=2:
#                     return 1
#                     break
#                 else:
#                     pass
                

#     '''
#     check for same number
#     '''
#     def same_number(number):
#         if len(number)<=2:
#             return 0
#         elif number[1:]==("0"*(len(number[1:]))):
#             return 2
#         elif len(set(number))==1:
#             return 2
#         else:
#             return 0

#     '''

#     |-----------------------|
#     |check for incrementing |
#     |-----------------------|

#     '''

#     def incrementing(number):
#         if len(number)<=2:
#             return 0
#         count = 0
#         if number[::-1][0]=="0":
#             number = number[:len(number)-1]
#         while count!=len(number) and len(number)!=1 and len(number)!=2:
#             for i in number:
#                 if count == len(number)-1 and len(number)!=1:
#                     return 2
#                     break
#                 elif int(number[number.index(i)+1])-int(number[number.index(i)])==1 and len(number)!=1:
#                     count+=1
#                     pass
#                 else:

#                     break
#             break


#     '''

#     |-----------------------|
#     |check for decrementing |
#     |-----------------------|

#     '''

#     def decrementing(number):
#         if len(number)<=2:
#             return 0
#         count = 0
#         while count!=len(number) and len(number)!=1 and len(number)!=2:
#             for i in number:
#                 if count == len(number)-1:
#                     return 2
#                     break
#                 elif int(number[number.index(i)])-int(number[number.index(i)+1])==1:
#                     count+=1
#                     pass
#                 elif len(number)==1:
#                     break
#                 else:
#                     break
#             break

#     def palindrome(number):
#         if len(number)<=2:
#             return 0
#         if len(number)!=1:
#             temp=int(number)
#             rev=0
#             while(int(number)>0):
#                 dig=int(number)%10
#                 rev=rev*10+dig
#                 number=int(number)//10
#             if(temp==rev):
#                 return 2
#             else:
#                 return 0
#         else:
#             return 0


#     if test_2(number, awesome_phrases)==2 or same_number(number) or palindrome(number)==2 or incrementing(number)==2 or decrementing(number)==2:
#         return 2
#     elif test_2(str(int(number)+2), awesome_phrases)==1 or same_number(str(int(number)+2)) or incrementing(str(int(number)+2))==2 or decrementing(str(int(number)+2)) or palindrome(str(int(number)+2)):
#         return 1
#     elif test_2(str(int(number)+1), awesome_phrases)==1 or same_number(str(int(number)+1)) or incrementing(str(int(number)+1))==2 or decrementing(str(int(number)+1)) or palindrome(str(int(number)+1)):
#         return 1
#     else:
#         if len(number)==2:
#             return 0
#         else: 
#             return 0