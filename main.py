from time import time
from random import random
from math import floor
from score import add_score

def main():
  min_n = 3
  max_n = 10

  inp_n = 0
  num_i = 0
  num_j = 0
  start_t = 0
  end_t = 0

  print("press any key to start")
  input()
  while True:
    num_i = floor(rand(min_n, max_n)) 
    num_j = floor(rand(min_n, max_n)) 

    start_t = time()
    print(str(num_i) + " X " + str(num_j) + " = ")
    inp_n = input()
    ent_t = time()

    print("%.3f" % (ent_t - start_t))
    if str(num_i * num_j) == inp_n:
      print("correct")
    else:
      print("wrong, the correct answer is: " + str(num_i * num_j))
    
    add_score(num_i, num_j, str(num_i * num_j) == inp_n, ent_t - start_t)

    print("press enter to continue or type q to quit")
    quit = input()
    if quit == "q":
      break

def rand(min_n = 0, max_n = 1):
  return (random() * (max_n - min_n)) + min_n

if __name__ == "__main__":
  main()