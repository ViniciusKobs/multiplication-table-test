from math import floor
from score import load_score

def main():
  scores = load_score()

  for i in range(7):
    for j in range(7 - i):
      print("\n---------- " + str(i+3) + " X " + str(j+3 + i) + " ----------")
      print("total times: " + str(scores[i][j + i]["tries"] + scores[j + i][i]["tries"]))
      print("total hits: " + str(scores[i][j + i]["points"] + scores[j + i][i]["points"]))
      print("hits percentage: " + str(floor((scores[i][j + i]["points"] + scores[j + i][i]["points"]) / (scores[i][j + i]["tries"] + scores[j + i][i]["tries"]) * 100)) + "%")

      best_t = 1000
      average_t = 0
      worst_t = 0
      for t in scores[i][j + i]["times"]:
        if t < best_t:
          best_t = t
        if t > worst_t:
          worst_t = t
        average_t += t
      for t in scores[j + i][i]["times"]:
        if t < best_t:
          best_t = t
        if t > worst_t:
          worst_t = t
        average_t += t
      average_t /= len(scores[i][j + i]["times"]) + len(scores[j + i][i]["times"])

      print("best time: " + ("%.3f" % best_t))
      print("average time: " + ("%.3f" % average_t))
      print("worst time: " + ("%.3f" % worst_t))

if __name__ == "__main__":
  main()