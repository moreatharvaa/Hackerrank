## Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. ( N is an odd natural number, and M  is 3 times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.


Input Format

A single line containing the space separated values of  N and M.

-- Sample Input

9 27

-- Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------


a,b = input().split()
a = int(a)
b = int(b)
#printing first half
for i in range(a//2):
    c = int((2*i)+1)
    print(('.|.'*c).center(b, '-'))
#printing middle line
print('WELCOME'.center(b,'-'))
#printing last half
for i in reversed(range(a//2)):
    c = int((2*i)+1)
    print(('.|.'*c).center(b, '-'))
