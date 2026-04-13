# 3)Create a tuple with mixed data types and:
# a)Access elements using indexing
# b)Explain why tuples are immutable
# c)Convert a tuple into a list, modify an element, and convert it back into a tuple.

t = (29, "Deepika", 10.0, True)

# a) Access elements
print(t[0])
print(t[1])

# b) Why immutable?
# Tuple cannot be changed after creation (no add/remove/update)

# c) Convert → modify → back
temp = list(t)
temp[1] = "Pavan"
t = tuple(temp)

print(t)