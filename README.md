Solution
===================
For this problem, I read user input and store it into the stack data structure after it is cleaned/formatted. The input is then iterated through; numbers are added to the stack, while operators call the operator function and operate on the top 2 numbers on the stack. This process is repeated until the end of the input and the process is killed.

The basic arithmetic operations are defined into it's own class to keep the operations modular and to also easily support the addition of other operations. The arithmetic operations are stored in a dictionary where the key-value pair are operator:operation function so that when operators are read, the respective operation function is called

Time complexity is O(n) where n is the total number of characters the user enters. Space complexity is O(n) for storing input in the stack plus O(m) dict for storing operations, overall O(n)
