from json import load, dump, dumps

def add_score(i, j, point, time):
  score = load_score()
  score[i - 3][j - 3]["tries"] = score[i - 3][j - 3]["tries"] + 1
  if point:
    score[i - 3][j - 3]["points"] = score[i - 3][j - 3]["points"] + 1
    score[i - 3][j - 3]["times"].append(time)
  dump_score(score)

def load_score():
  return load(open("score.json", "r"))

def dump_score(data):
  dump(data, open("score.json", "w"), indent=4)

def reset_score():
  empty = load(open("empty_score.json", "r"))
  dump(empty, open("score.json", "w"), indent=4)

def print_json(data, i=4):
  print(dumps(data, indent = i))
