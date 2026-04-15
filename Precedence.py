# 10.Explain operator precedence in Python and write a program showing how precedence affects the result.
# () → ** → * / // % → + -
# 2 * 5 happens first → 10 + 10 = 20
# (10 + 2) first → 12 * 5 = 60

res1 = 15 + 2 * 6
res2 = (15 + 2) * 6

print("Without brackets:", res1)   
print("With brackets:", res2)  