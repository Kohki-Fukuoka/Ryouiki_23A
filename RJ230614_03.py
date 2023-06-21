
def read_files():

    file_path_before = "sample/kitamura_"
    file_path_after = "_kgu.txt"

    sum = 0

    for i in range(1, 1000, 2):
        file_path = f"{file_path_before}{i:05}{file_path_after}"
        with open(file_path, "r") as f:
            line_sum = calc_file(f)
            sum += line_sum
    
    return sum


def calc_file(f):
    contents = f.read()
    lines = contents.split("\n")

    sum = 0

    for line in lines:
        try:
            val = int(line)
            sum += val
        except:
            pass
    
    return sum

def main():
    print(read_files())

if __name__ == "__main__":
    main()
