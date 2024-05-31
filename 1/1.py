def print_complement(string):
    string = string.lower()

    string = string.replace("a", "C")
    string = string.replace("c", "A")
    string = string.replace("g", "T")
    string = string.replace("t", "G")

    print(string)


if __name__ == '__main__':
    print_complement("CAGT")
