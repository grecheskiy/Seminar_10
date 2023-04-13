for at in ['attribute', 'класс', 'функция', 'type']:
    try:
        print(at, type(at), at.encode('ascii'), ' - encoding to bytes successful ')
    except:
        print(at, type(at), ' - not valid input for bytes string')
