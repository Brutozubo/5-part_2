import json

class Model():
    def __init__(self, title, text, author):
        self.title = 1
        self.text = 2
        self.author = 3
data = {"Title": 1, "Text": 2, "Author": 3}
obj = Model(1, 2, 3)


fltrd_lst = [a for a in dir(obj) if not a.startswith('__')]
print(fltrd_lst)

print(obj.title)
print(obj.text)
print(obj.author)

json_string = json.dumps(data)
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)
