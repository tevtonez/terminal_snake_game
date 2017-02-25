
# -*- coding: utf-8

from random import randint

from matrix import *
from character import *
from bounty import *

rows, columns  = 20 , 40
field_symbol =  ' '

game_matrix = Matrix(rows, columns, field_symbol)
main_symbol = MainSymbol('o')

li_food_items = []

for i in xrange(Food.food_items):
  foodx = randint(1, 38)

  if foodx % 2 != 0:
    foodx += 1

  foody = randint(1, 18)
  food_item_name = 'food_item' + str(i)

  li_food_items.append([food_item_name, '∆', foodx, foody])


for food_item in li_food_items:
  food_name = food_item[0]
  food_name = Food(food_item[1], food_item[2], food_item[3])
  game_matrix.update_food_in_matrix(food_name.foodx, food_name.foody, food_name.food_symbol)



game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

while True:

  score_board = '\nОЧКИ:' + str(MainSymbol.score) + '                     ОСТАЛОСЬ:' + str(Food.food_items)
  line = ' -' + '-' * game_matrix.columns + '- '

  print score_board
  print line
  game_matrix.print_matrix()
  print line

  direction = raw_input("Используй WASD и Enter для движения:")

  if direction == 'q': break
  if direction in (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST):

    game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.trace)
    main_symbol.move(direction)
    game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

    if Matrix.halt:
      print score_board
      print line
      game_matrix.print_matrix()
      print line

      break
