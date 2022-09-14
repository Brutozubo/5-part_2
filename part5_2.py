
import json

class Model():
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

obj = Model(1, 2, 3)


fltrd_lst = [a for a in dir(obj) if not a.startswith('__')]


json_string = json.dumps(obj.__dict__)
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)

print(json_string)
