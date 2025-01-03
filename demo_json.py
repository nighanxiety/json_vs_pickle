import json

SAVEFILE = "demo.json"
DATA = {
    "Foo": 0,
    "Baz": "Test",
    "Bar": (6, 32, 85, "Apple"),
     100: {'A':1, 2:'b', 3:'d', 4:'H'},
     True: False,
     "(1, 2, 3)": "Complex Key must be made a string in advance"
}

def load(file):
    data = {}
    with open(file, "r") as json_file:
        try:
            data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            print("JSON file is malformed or empty")
    return data

def save(data, file):
    with open(file, "w") as json_file:
        json.dump(data, json_file)

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
