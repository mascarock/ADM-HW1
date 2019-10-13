if __name__ == '__main__':
    n = int(input())
    # create the array for the scores
    scores = list(map(int, input().split()))
    # get the max
    m = max(scores)
    # store the temporary min (algo for min)
    minScore = min(scores)
    for x in scores:
        if(x>minScore and x<m):
            minScore = x
    print(minScore)