#REVERSE STRING
Original_String="Hello olleH"
reverse_string=Original_String[::-1]
# print(reverse_string)


#REVERSE WORD
split_String=Original_String.split(" ")
reversed_word=" ".join(split_String[::-1])
# for str in split_String:
#    reversed_word=reversed_word+" "+str
# print(reversed_word.strip())
# print(reversed_word)

#PALINDDROME
# print("PALINDROME" if Original_String==reverse_string else "NOT PALINDROME")

#Reverse Number
Original_Number=5
# Reverse_Number=0
# while Original_Number>0 :
#     Reverse_Number=Reverse_Number*10+(Original_Number%10)
#     Original_Number=Original_Number//10
# print(Reverse_Number)
# print(int(str(Original_Number)[::-1]))

#FACTORIAL
Factorial=1
# for i in range(1,Original_Number+1) :
#     Factorial=Factorial*i
# print(Factorial)

#FIBONACCI
# Prev_Number=0
# Current_Number=1
# Step=int(input("Enter the step for fibonacci calculation : "))
# for i in range(Step+1):
#         print(Prev_Number)
#         Print_Number=Prev_Number+Current_Number
#         Prev_Number=Current_Number
#         Current_Number=Print_Number

#Prime and Count the Prime Number
def IsPrime(num):
    for i in range(2,num) :
        if num%i==0:
            return False
    return True
# checkNumber=int(input("ENTER THE NUMBER : "))
# # print("Prime" if IsPrime(checkNumber) else "Not Prime")
# count=0;
# for i in range(1,checkNumber) :
#     if IsPrime(i):
#         count+=1
# print(count)

#Count Vowel
# Count=0;
# words="Hello Anand how are you"
# for word in words:
#     if(word.lower() in 'aeiou'):
#         Count+=1
# print(Count)

#Remove Duplicates
Provided_List=[11,22,33,44,22,33,22,22,11,22]
# print(list(set(Provided_List)))
count=0;


#Count Duplicates
# for i in range(len(Provided_List)) :
#     for j in range(i+1,len(Provided_List)):
#         if Provided_List[i]==Provided_List[j]:
#             count+=1
#             break
# print(count)
# print(len(Provided_List)-len(set(Provided_List)))

#Find Duplicates
# Without_Duplicate=list(set(Provided_List))
# seen=set()
# for i in Provided_List:
#     if i in seen :
#         print("duplicate is " ,i)
#     else :
#         seen.add(i)
# print(seen)

#Find second largest no.
# Provided_List.sort()
# print(Provided_List[-2])

#Maximum and minimum
# print(max(Provided_List))
# print(min(Provided_List))

#Merge List
Second_List=[20,5,85,96,23,11,22]
# New_List=Provided_List+Second_List
# print(New_List)

#Common Element
# Provided_set=set(Provided_List)
# Second_set=set(Second_List)
# print(Provided_set & Second_set)

#Frequency of Character
Given="Banana"
# new_word="".join(set(Given))
new_Dict={}
# for i in range(0,len(new_word)) :
#     count=0
#     for j in range(0,len(Given)) :
#         if new_word[i]==Given[j] :
#             count+=1;
#     new_Dict.update({new_word[i]:count})
# # print(new_Dict)

# def frequencyCheck(words):
#     Frequency={}
#     for char in words :
#         if char in Frequency :
#             Frequency[char]+=1
#         else :
#             Frequency[char]=1
#     return Frequency

#Anagram
# new_word="anaban"
# print("Anagram" if frequencyCheck(Given.lower())== frequencyCheck(new_word.lower()) else "not Anagram")


#Armstrong Number
# IsArmstrong=371
# Original=IsArmstrong
# new=0
# length=len(str(IsArmstrong))
# while IsArmstrong>0 :
#     new+=(IsArmstrong%10)**length
#     IsArmstrong=IsArmstrong//10
# print("Armstrong" if Original==new else "Not an Armstrong Number")

#missing number
Givemlist=[0,1,2,3,4,5,7,9,6]
# maxi=max(list)
# mini=min(list)
# sum=0
# total=0
# for i in range (mini,maxi+1):
#     sum+=i
# for num in Givemlist:
#     total+=num
# print(sum-total)
# targetSet=set()
# target=8
# for i in Givemlist :
#     if target-i in targetSet:
#         print(i,target-i)
#         # break
#     else :
#         targetSet.add(i)



