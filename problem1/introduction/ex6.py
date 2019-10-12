def is_leap(year):
    leap = False

    # Verbose version
    # if year %400 == 0: leap = True
    # else:
    #     if ( year%4==0 and not year %100 == 0): leap = True
    #     else: leap = False
    
    # Short version
    if year %400 == 0 or ( year % 4 == 0 and not (year %100 == 0)): leap = True
    return leap

year = int(input())
print (is_leap(year))