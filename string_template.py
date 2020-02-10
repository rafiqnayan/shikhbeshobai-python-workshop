from string import Template


t = Template('Hey, $name! Welcome to $country')

s = t.substitute(name='Bob', country='Bangladesh')
print(s)

s = t.substitute(name='Alice', country='Bangladesh')
print(s)

s = t.substitute(name='Bob', country='England')
print(s)