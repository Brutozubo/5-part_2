class Model:
    def Save(self):
        import json
        dict = {'title': 'Какой-то заголовок',
                'text': 'Какой-то текст',
                'author': 'Какой-то автор'}
        json = json.dumps(dict)
        f = open('dict.json', 'w')
        f.write(json)
        f.close()

class C1():
    title = '1'
    text = '2'
    author = '3'


print (list(filter(lambda x: not x.startwith('_'), dir(C1))))