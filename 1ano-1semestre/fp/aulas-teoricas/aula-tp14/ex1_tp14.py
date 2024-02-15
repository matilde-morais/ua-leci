# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. The first place on the board, a1, is black. The next
# is white, alternating across a row. Odd rows start with black, even rows start with white.

# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Black" or
# "White" indicating if the square is black or white.

inputStr = 'a1' 

column = inputStr[0]
row = int(inputStr[1])
   
if row in [1, 3, 5, 7]:
   if column in ['a', 'c', 'e', 'g']:
      print('Black')
   elif column in ['b', 'd', 'f', 'h']:
      print('White')
elif row in [2, 4, 6, 8]:
   if column in ['a', 'c', 'e', 'g']:
      print('White')
   elif column in ['b', 'd', 'f', 'h']:
      print('Black')