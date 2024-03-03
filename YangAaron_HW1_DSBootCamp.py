#1 Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word 
def count_vowels(word):
    count=0
    vowels = "aeiouAEIOU"
    for letters in word:
        if letters in vowels:  
            count+=1
    print("Number of Vowels:", count)

#2. Iterate through the following list of animals and print each one in all caps.
def cap_words(lst):
    for word in lst:
        all_cap_list=[word.upper() for word in lst]
    print(all_cap_list)
    
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

#3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
def return_parity(num):
    count=1
    while count <= num: 
        if count%2==0:
            print(count,"is even")
        else:
            print(count,"is odd")
        count+=1

#4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
def sum_of_integers(a,b):
    print("The sum of",a,"and",b,"is",a+b)


count_vowels("Aaron Yang")   #Q1
cap_words(animals)           #Q2
return_parity(20)            #Q3
sum_of_integers(1,3)         #Q4



