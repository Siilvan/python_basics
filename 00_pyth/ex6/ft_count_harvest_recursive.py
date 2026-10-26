def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))
    print_recursive(1, count)
    print("Harvest time!")


def print_recursive(day, max):
    if day <= max:
        print("Day", day)
        day += 1
        print_recursive(day, max)
