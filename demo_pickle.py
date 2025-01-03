import pickle

SAVEFILE = "demo.pk1"
DATA = {
    "Foo": 0,
    "Baz": "Test",
    "Bar": (6, 32, 85, "Apple"),
     100: {'A':1, 2:'b', 3:'d', 4:'H'},
     True: False,
     (1, 2, 3): " Any valid python dict key is ok"
}

def load(file):
    data = None
    with open(file, "rb") as pickle_file:
        try:
            data = pickle.load(pickle_file)
        except Exception as e:
            print(e)
    return data

def save(data, file):
    with open(file, "wb") as pickle_file:
        pickle.dump(data, pickle_file)

if __name__ == '__main__':
    while True:
        action = input("Load, Save, or Quit:  ").upper()[0]
        if action == "L":
            try:
                output = load(SAVEFILE)
            except FileNotFoundError:
                print(f"The data file {SAVEFILE} does not yet exist.  Try the `Save` action")
            else:
                print("File contents: ")
                print(output)
        elif action == "S":
            save(DATA, SAVEFILE)
            print(f"Test data saved to {SAVEFILE}")
        elif action == "Q":
            break
