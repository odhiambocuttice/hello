import jason


with open("states.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
