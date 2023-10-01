import yaml

def read_yaml_file(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)
    
def write_yaml_file(path, data):
    with open(path, "w") as file:
        yaml.safe_dump(data, file)

def append_yaml_file(path, data):
    with open(path, "a") as file:
        yaml.safe_dump(data, file)