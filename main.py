from base_class import score
from io_manager import read_input, write_output
from strategy import method


for char in "abcde":
    cls = read_input(char)
    result = method(cls)
    score = get_score(cls, result)
    print(f"Case {char}: {score} score \n")
    write_output(result, char)
