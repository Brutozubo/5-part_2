class Model:

    title = '1'
    text = '2'
    author = '3'


    def save(self):
        print("Сохраняем атрибуты")

    С1 = Model()

    list = filter(lambda x: not x.startswith('_'), dir (C1))
    print(list)

    import json
    json = json.dumps(dict)
        f = open('dict.json', 'w')
        f.write(json)
        f.close()
