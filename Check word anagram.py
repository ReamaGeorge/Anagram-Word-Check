from itertools import permutations
import enchant

d = enchant.Dict("en_GB")
    
    
any_word = input("Enter a word \n")
inp = any_word
lettr = [x.lower() for x in inp]

  
for y in permutations(lettr):
    z = "".join(y)
    if d.check(z) and z != inp:
        print(True)
        break
    
else:
    print(False)


