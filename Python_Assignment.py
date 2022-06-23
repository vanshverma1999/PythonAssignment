#Q1). Python program to remove given character from String. 
str1 = 'python programming'
char = 'p'
print(str1.replace('p',''))

#Q2). Python Program to count occurrence of a given characters in string. 
str2 = 'python programminggggg' #g is occurring 6 times
char = 'g'
count2 = 0
for i in str2:
    if char is i:
        count2 = count2+1
print(count2)

#Q3). Python Program to check if two Strings are Anagram. 
str31 = 'abcda'
str32 = 'dcba'
if len(str31)==len(str32):
    sorted_str31 = sorted(str31)
    sorted_str32 = sorted(str32)
    if sorted_str31==sorted_str32:
        print('Strings are anagram')
    else:
        print('Not anagram')
else :
    print('Not anagram')

#Q4). Python program to check a String is palindrome or not. 
str4 = "abcba"
flag = str4==str4[::-1]
if flag : print('is Palindrome')
else : print('not Palindrome')

#Q5). Python program to check given character is vowel or consonant. 
def isVowel(char):
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
char = 'a'
flag5 = isVowel(char)
if flag5 : print('is vowel')
else : print('is consonent')

#Q6). Python program to check given character is digit or not. 
char6 = '5'
if char6>='0' and char6<='9': print('is Digit')
else : print('not a digit')

#Q7). Python program to check given character is digit or not using isdigit() method. 
char7 = '7'
if char7.isdigit() : print('is Digit')
else : print('not a digit')

#Q8). Python program to replace the string space with a given character. 
str8 = 'Hello world haha'
str81 = ''
for i in str8:
    if i==' ' : str81 = str81 + 'b'
    else : str81 = str81 + i
print(str81)

#Q9). Python program to replace the string space with a given character using replace() method. 
str9 = 'Hello world haha'
print(str9.replace(' ','c'))

#Q10). Python program to convert lowercase char to uppercase of string. 
str10 = 'this was lowercase first'
print(str10.upper())

#Q11). Python program to convert lowercase vowel to uppercase in string. 
str_copy = ''
for i in str10 :
    if isVowel(i):
        str_copy = str_copy + i.upper()
    else:
        str_copy = str_copy + i
print(str_copy)

#Q12). Write a program in Python for, In array 1-100 numbers are stored, one number is missing how do you find it.
lst = list(range(1,101))
lst[6] = 8
for i in range(0,100):
    if i+1!=lst[i] : print(i+1,'is not there in the lst')

#Q13). Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it. 
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]==lst[j]):
            print(lst[i],'is Duplicate')

#Q14). Write a program in Python for, How to find all pairs in array of integers whose sum is equal to given number. 
arr14 = [1,2,3,4,5,6]
sum = 5
for i in range(0,len(arr14)):
    for j in range(i+1,len(arr14)):
        if arr14[i]+arr14[j]==sum:
            print('[',arr14[i],',',arr14[j],'] has sum = ', sum)

#Q15). Write a program in Python for, How to compare two array is equal in size or not. 
lst15_1 = [1,2,3,4]
lst15_2 = [1,2,3,4,5]
if len(lst15_1)==len(lst15_2) : print('Arrays are equal in length')
else : print('Arrays does not have same length')

#Q16). Write a program in Python to find largest and smallest number in array. 
lst16 = [4,1,5,6,2,4,7,4,2,8]
min = lst16[0]
max = lst16[1]
if min>max : min,max = max,min
for i in range(2,len(lst16)):
    if min>lst16[i] : min = lst16[i]
    elif max<lst16[i] : max = lst16[i]
print('Max : ',max,'Min : ',min)

#Q17). Write a program in Python to find second highest number in an integer array. 
lst17 = [4,1,5,6,2,4,7,4,2,8]
sec_max = lst17[0]
max = lst17[1]
if sec_max>max : sec_max,max = max,sec_max
for i in range(2,len(lst17)):
    if max < lst17[i]:
        sec_max = max
        max = lst17[i]
print('Max : ',max,'Second Max : ', sec_max)  

#Q18). Write a program in Python to find top two maximum number in array? 
lst17 = [4,1,5,6,2,4,7,4,2,8]
sec_max = lst17[0]
max = lst17[1]
if sec_max>max : sec_max,max = max,sec_max
for i in range(2,len(lst17)):
    if max < lst17[i]:
        sec_max = max
        max = lst17[i]
print('1st Max no. : ',max,'2nd Max no. :', sec_max) 

#Q19). Write a program in Python to remove duplicate elements form array. 
lst19 = [1,1,1,3,4,5,5,5,5,6]
lst19_copy = []
for i in lst19:
    if i in lst19_copy:continue
    else : lst19_copy.append(i)
print(lst19_copy)

#Q20). Python program to find top two maximum number in array. 
lst17 = [4,1,5,6,2,4,7,4,2,8]
sec_max = lst17[0]
max = lst17[1]
if sec_max>max : sec_max,max = max,sec_max
for i in range(2,len(lst17)):
    if max < lst17[i]:
        sec_max = max
        max = lst17[i]
print('1st Max no. : ',max,'2nd Max no. :', sec_max) 

#Q21). Python program to print array in reverse Order. 
lst21 = [1,2,3,4,5,6]
print(lst21[::-1])

#Q22). Python program to reverse an Array in two ways. 
lst22 = [1,2,3,4,5,6]
for i in range(len(lst22)-1,-1,-1):
    print(lst[i],end=' ')

#Q23). Python Program to calculate length of an array. 
lst23 = [1,2,3,4,5,6]
print('\nLength of array is',len(lst23))

#Q24). Python program to insert an element at end of an Array. 
lst24 = [1,2,3,4,5,6]
a = 7
lst24.append(a)
print(lst24)
    