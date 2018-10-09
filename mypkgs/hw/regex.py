import re

t = '''(this is inside)
this is not'''
p = re.compile(r'\(?.+\)?')
m = re.findall(p,t)
print(m)

s = '''
My number is (+420) 725 858 538 4444444444 
+333 458 333 258 (454)545 454 544
42072585538 7777777444477444477 
'''

r = r'\s*\(?[+]{0,1}\d{3}\)?\s*\d{3}\s*\d{3}\s*\d{3} '
p = re.compile(r)
#p = re.compile(r'\(?[+]*?\d{3}\)?\s*\d{3}\*\d{3}\s*\d{3}')
#m=p.search(s)
#print(m)
m = re.findall(p, s)
print(m)

# reverse name, not startingt with...
s='Dick Dick'
s = re.sub('([a-zA-z]+) ([a-zA-z]+)', r'\2 \1', s)
print(s)



def camel_to_snake(text):
    import re
    str1 = re.sub('((?<=[a-z0-9])[A-Z]|(?<!^)[A-Z](?=[a-z]))', r'_\1', text)
    #str1 = re.sub('(?<!^)([A-Z]+)', r'_\1', text)
    #return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
    return str1.lower()
print(camel_to_snake('Python3ExercisesForHTTP'))
print(camel_to_snake('python3ExercisesForHTTP'))