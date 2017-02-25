# -*- coding: utf-8

import string
from character import *
from bounty import *
from character import *


def msg_line(text, cols_total):
  text_len = len(text.translate(None, string.punctuation + ' '))
  half_of_columns = ' ' * ( (cols_total - ( text_len / 2) - 2) // 2 )

  if text_len == 3 :
    li_half_of_columns = list(half_of_columns)
    li_half_of_columns.pop()
    half_of_columns_minus_one = ''.join(li_half_of_columns)
    message = half_of_columns + text  + half_of_columns_minus_one

  else :
    message = half_of_columns + text  +  half_of_columns

  return message


class Matrix():

  halt = False

  def __init__(self, rows, columns, default_character = ' '):

    self.rows = rows
    self.columns = columns

    self.grid = [ [default_character] * columns for l in xrange( rows ) ]


  def print_matrix(self):

    for row in self.grid:
      print '|', ''.join(row) , '|'


  def update_character_in_matrix(self, column_number, row_number , new_character):

    if 0 <= row_number < self.rows and 0 <= column_number < self.columns:

      if self.grid[row_number][column_number] == '∆':
        MainSymbol.score += Food.food_score
        Food.food_items -= 1

      self.grid[row_number][column_number] = new_character

      if Food.food_items == 0:
        Matrix.halt = True

        game_over_msg = [
          msg_line('ПОБЕДА !', self.columns) ,
          msg_line('  ', self.columns) ,
          msg_line('набрано очков:', self.columns) ,
          msg_line(' ' + str(MainSymbol.score) + ' ' if MainSymbol.score >= 10 else ' ' + str(MainSymbol.score).rjust(2, '0') + ' ', self.columns)
        ]

        i = 0
        for game_message in game_over_msg:
          self.grid[(self.rows // 2) + i] = str(game_message)
          i += 1

      return

    else:
      Matrix.halt = True

      game_over_msg = [
        msg_line('ИГРА ОКОНЧЕНА!', self.columns) ,
        msg_line('  ', self.columns) ,
        msg_line('набрано очков:', self.columns) ,
        msg_line(' ' + str(MainSymbol.score) + ' ' if MainSymbol.score >= 10 else ' ' + str(MainSymbol.score).rjust(2, '0') + ' ', self.columns)
      ]

      i = 0
      for game_message in game_over_msg:
        self.grid[(self.rows // 2) + i] = str(game_message)
        i += 1

      return


  def update_food_in_matrix(self, column_number, row_number , food_character):
    self.grid[row_number][column_number] = food_character
    return


