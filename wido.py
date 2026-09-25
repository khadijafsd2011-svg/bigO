n = 10

guess = input("double Loop at n = 10 checks n x n pairs.  How many? ")

input("Formula: one calculation, done. Press Enter to run ")
steps = 1
print("  steps =", steps, " -> 0(1) constant time -> steps never change")
#best case scenario

input("Loop: one step per item.  Press Enter to run")
steps = 0
for i in range(n):
    steps +=1
    print("  steps =",steps,"-> O(n) linear time -> steps grow with n")
    #average case scenario

input(" Double Loop: checks every pair.  Press Enter to run ")
steps = 0
for i in range(n):
    for j in range(n):
        steps +=1
print(" steps =", steps, " your guess:", guess,"-> O(n^2) quadratic time")
#worst case scenario

input("Two more natations.  Press Enter ")
print(" Big Omega  -> best case lower bound")
print(" Big Theta  -> exact bound (worst = best)")