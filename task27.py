import re
sequence = "She sells, sells! How much\n money!!! What?!    what."
list = [i.strip(",.!?\n") .lower()for i in sequence.split(" ")]
result = set(list)
result.discard('')
print(result)
print(len(result))
