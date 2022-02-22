from base_class import BaseClass

def read_input(character):
    baseclasses = []
    with open(f"data/{character}.in.txt") as f:
        for i, line in enumerate(f):
            continue
    return

def write_output(result, character):
    with open(f"output/{character}.out.txt", "w") as f:
        f.write(" ".join(line))

