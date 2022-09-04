class Model:

    title = '1'
    text = '2'
    author = '3'

    def save(self):
        model_a = Model()
        model_a.save()
        list = filter(lambda x: not x.startswith('_'), dir(model_a)))
        print(list)
        
        import json
        json = json.dumps(dict)
        f = open('dict.json', 'w')
        f.write(json)
        f.close()
