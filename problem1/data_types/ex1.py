if __name__ == '__main__':
    # get it out of the way the first line
    n = int(input())
    # read the second line and split by whitespace
    line = input().split()
    # save the line into a list of integers
    integer_list = map(int, line)
    # convert the list to a tuple of ints, which is hashable
    tp = tuple(integer_list)
    # print the hash
    print(hash(tp))