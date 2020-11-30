import os

def get_one_line(filepath, indices_you_want):
        to_store = []
        for i, row in enumerate(open(filepath)):
            if i in indices_you_want:
                to_store.append(row)
        return to_store

def path():
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    return path

def altair_json_output(json_file):
    fl = open(json_file, "r")
    json = fl.read()
    fl.close()
    return json