# javascript object notation
import json
with open('data.json', 'r') as f:
    py_obj = json.load(f)
    #data = f.read()

#print(type(data))
#py_obj = json.loads(data)
#print(type(py_obj))

# json_str = json.dumps(py_obj)
# print(type(json_str))

with open("new_data.json", 'w') as f:
    json.dump(py_obj, f, indent=4)