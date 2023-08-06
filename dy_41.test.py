 
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
