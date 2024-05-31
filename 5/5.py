from create_strings import init_test_file
from functools import reduce

def read_strings(file_name):
    strings = {}
    with open(file_name, "r") as f:
        key = ""
        for line in f.readlines():
            line = line.strip()
            if line.startswith(">"):
                key = line[1:]
            else:
                strings[key] = line
                key = ""

    return strings


def inter_of_two(s1, s2):
    result = ""
    min_str = s1 if len(s1) < len(s2) else s2
    for i in range(len(min_str)):
        for j in range(i + 1, len(min_str) + 1):
            if min_str[i:j] in list({s1, s2} - {min_str})[0]:
                if len(result) < len(min_str[i:j]):
                    result = min_str[i:j]
    return result

def max_substr(string_list):
    return reduce(lambda inter, next: inter_of_two(inter, next), string_list)


def main():
    print(max_substr(read_strings("strings.txt").values()))


if __name__ == "__main__":
    #init_test_file("strings.txt", 10)
    main()