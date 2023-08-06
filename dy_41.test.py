# Instructions
# You are going to write a virtual coin toss program. # It will randomly tell the user "Heads" or "Tails".
# the first letter should be capitalised  and spelt exactly like in the example e.g. Heads, not heads. 
# you should generate a random number, either 0 or 1.Then use that number to print out Heads or Tails. 
# e.g. 1 means Heads, 0 means Tails 
import random
test_seed = int(input("Enter the seed number of your choice: "))
random.seed(test_seed)
coin_choice = random.randint(0,1)
print(coin_choice)
coin_toss = ['heads','tails']
coin_toss_H = coin_toss[0].capitalize()
coin_toss_T = coin_toss[1].capitalize()
if coin_choice == 1:
    print(f'The coin is {coin_toss_H}')
else:
    print(f'The coin is {coin_toss_T}')

# Alternative
# if coin_choice ==1:
#   print("Heads")
# else:
#        print("Tails")