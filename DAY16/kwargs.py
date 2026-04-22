# **kwargs --> keyword args

def details(**kwar):
    return kwar

print(details(name="Deepika", id = 101, age = 23, sal = 20000, role = "Software developer"))

#{'name': 'Deepika', 'id': 101, 'age': 23, 'sal': 20000, 'role': 'Software developer'}