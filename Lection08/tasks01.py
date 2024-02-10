import json

a = 'Hello world!'
print(*enumerate(a))
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))

print(c)
