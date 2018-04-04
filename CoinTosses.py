# Assignment: Coin Tosses
# Objectives:
# Practice writing functions and loops
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

import random

def CoinTosses():
    headCount = 0
    tailCount = 0
    totalCount = 0
    for x in range(0,10):
        random_num = random.randint(1,2)
        if random_num == 1:
            headCount += 1
            totalCount += 1
            print("Attempt #", totalCount, ": Tossing coin... It's a head! You have", headCount,"head(s) and",tailCount,"tail(s) so far") 
        else:
            tailCount += 1
            totalCount += 1
            print("Attempt #", totalCount, ": Tossing coin... It's a tail! You have", headCount,"head(s) and",tailCount,"tail(s) so far")
        
CoinTosses()
