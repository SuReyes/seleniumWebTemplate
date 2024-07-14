def read_file_lines(filename):
    with open(filename, 'r') as f:
        return [line.replace('\n', '') for line in f.readlines()]