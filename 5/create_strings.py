import random

def get_random_sequence(length):
    result = ""
    for i in range(length):
        result += random.choice(['A', 'C', 'G', 'T'])

    return result

def init_test_file(file_name, test_count):
    with open(file_name, "w") as f:
        for i in range(test_count):
            f.write(">str" + str(i) + "\n")
            f.write(get_random_sequence(random.randint(1, 2000)) + "\n")