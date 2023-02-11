Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# # Scoring

# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# # Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# # Constraints



# # Sample Input

# BANANA

# # Sample Output

# Stuart 12

Sol:-
  
  def minion_game(string):
    s = len(string)
    vowel = 0
    consonant = 0
    
    
    for i in range(s):
        if string[i] in "AIEUO":
            vowel += (s - i)
            
        else:
            consonant += (s - i)
            
    if vowel < consonant:
        print("Stuart " +str(consonant))
        
    elif vowel > consonant:
        print("Kevin " +str(vowel))
        
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    
#    Explanation:-
    
#     1) storing the length of the string
#     2) declare two variables vowel and consonant and initialize them to 0
#     3) In the for loop, if character at index i of string is a vowel then increment vowel by (s-i), else if string at index i is not a vowel then we increment consonant by (s-i).
#    4)   After the execution of the lop, if vowel is less than consonant we print Stuart along with value of consonant and else if vowel is greater than consonant we print Kevin along with the value of vowel, and if both are equal we print ‘Draw’.
