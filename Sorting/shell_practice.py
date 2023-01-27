def shell_sort(list):
    n = len(list)

    interval = n//2
    while interval>0:
        for i in range(interval,n):
            temp = list[i]
            j = i
            while j >= interval and list[j-interval]>temp:
                list[j] = list[j-interval]
                j-=interval
            list[j] = temp

        interval //=2
