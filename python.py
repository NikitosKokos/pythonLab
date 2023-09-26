import random


totalMoney = 1000

name = input('Your name>>>')
print(f'Hey {name}! You have {totalMoney}$, wanna play a bit?')
# number = None
# while not isinstance(number, int):
#     try:
#         number = int(input('Enter your number:'))
#     except:
#         print('Try again')


def shakeDice():
   global totalMoney

   bet = None
   while not isinstance(bet, int):
      try:
         bet = int(input('Enter your bet>>>'))
      except:
         print('Not valid')
   # bet = int(input('Enter your bet>>>'))
   if(bet > totalMoney):
      bet = totalMoney

   totalMoney = totalMoney - bet
   randomShake = random.randint(2, 12)
   print(f'Shake: {randomShake}')
   if(randomShake > 6):
      print(f'You win {bet * 2}!')
      totalMoney = totalMoney + bet * 2
   elif(randomShake < 6):
      print(f'You lost {bet} :(')
   else:
       print('Nothing changed, but at least you saved your money')
       totalMoney = totalMoney + bet


def game():
   if(totalMoney == 0):
      return totalMoney
   
   shakeDice()

   if(totalMoney == 0):
      return totalMoney
   else:
      print(f'Balance: {totalMoney}')

   def keepPlaying():
      isKeepPlaying = input('Keep playing?(Enter - Yes/no - Escape)>>>')

      if isKeepPlaying == '':
         return game()
      elif isKeepPlaying == 'no':
         return totalMoney
      else:
         keepPlaying()
      
   
   keepPlaying()
   


game()

'''
  ________
 /       /|
/______ / |
| *  * |  |
| *  * |  /
| *  * | /
|______|/

'''

print(f'Okay, {name}. Your total win is {totalMoney}')



# def factorial(x):
#    """This is a recursive function
#    to find the factorial of an integer"""

#    if x == 0:
#       return 0
#    elif x == 1:
#        return 1
#    elif x < 0:
#        return 'Isn\'t working with the negative numbers'
#    else:
#       return (x * factorial(x-1))
# print(factorial(number))