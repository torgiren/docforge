def init():
    import pymongo
    db = pymongo.Connection('localhost')['docforge']
    typy = [
        {'nazwa': 'Tekst', 'widget': 'text'},
        {'nazwa': 'Liczba', 'widget': 'number'},
        {'nazwa': 'Data', 'widget': 'date'}]
    db['typy'].insert(typy)
if __name__ == '__main__':
    init()
