from pyknp import Juman
text=input()
juman=Juman()
result=juman.analysis(text)
result=[mrph.midasi for mrph in result.mrph_list()]
print(text)
print(result)