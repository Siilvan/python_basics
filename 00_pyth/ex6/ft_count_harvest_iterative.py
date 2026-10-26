def ft_count_harvest_iterative():
    count = range(1, int(input("Days until harvest: ")) + 1)
    for i in count:
        print("Day", i)
    print("Harvest time!")
