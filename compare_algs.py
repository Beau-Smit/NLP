# package imports
import pandas as pd
import numpy as np
import jellyfish
import textdistance
import Levenshtein

# SPEED: Levenshtein, jellyfish, textdistance

# print(jellyfish.soundex('Beau'))
# print(jellyfish.soundex('Smit'))
# print(jellyfish.levenshtein_distance('Beau', 'Smit'))
# print(jellyfish.levenshtein_distance('hi', 'hello'))

myseries = pd.Series(['plumbob', 'plumbus', 'plumbing'] * 50000)

@profile
def jelly_lev(str1, str2):
   distance = jellyfish.levenshtein_distance(str1, str2)
   return distance

myseries.apply(jelly_lev, str2='plumber')

@profile
def textd_lev(str1, str2):
   distance = textdistance.levenshtein.distance(str1, str2)
   return distance

myseries.apply(textd_lev, str2='plumber')

@profile
def Leven_lev(str1, str2):
   distance = Levenshtein.distance(str1, str2)
   return distance

myseries.apply(Leven_lev, str2='plumber')

