def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
     return phrase.lower().count(letter.lower())

#in order to check the working of the function add the following lines to the code:

first_str = input("Enter the first string:")  #prompts user to enter first string

second_str = input("Enter the second string (one character long):")
#prompts user to enter second string which should be one character long

occurrence = count_occurrences(first_str,second_str)  #calls count_occurrences method by passing both strings to it

print(second_str,"occurs",occurrence,"times in",first_str) #prints how many times the second_str occurs in the first_str on output screen
