import random
# change the code to use functions
number_to_guess = random.randint(0, 100)
counter = input("Hard or easy ? Type 'h' or 'e': ")
print(f'Guess what number between 0 and 100 I found')
print(number_to_guess)

if counter == 'h':
    count = 5
else:
    count = 10
while count > 0:
    user_guess = int(input("Your guess is: "))
    if user_guess == number_to_guess:
         print(f"Yes the number is {user_guess}")
         count = 0
    elif user_guess < number_to_guess:
        print("The number you have chosen is lower than the generated number ")
        count -= 1
    elif user_guess > number_to_guess:
        print("The number you have chosen is higher than the generated number ")
        count -= 1
