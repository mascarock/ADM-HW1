List = []
result = []
N = int(input())
for i in range(N):
    List = input().split()
    if List[0] == "insert" :
        position = int(List[1])
        integer = int(List[2])
        result.insert(position,integer)
    if List[0] == "remove" :
        rem_int = int(List[1])
        result.remove(rem_int)
    if List[0] == "append" :
        append_int = int(List[1])
        result.append(append_int)
    if List[0] == "sort" :
        result.sort()
    if List[0] == "pop" :
        result.pop()
    if List[0] == "reverse" :
        result.reverse()
    if List[0] == "print" :
        print(result)