import sys


def create_inv() -> dict[str, int]:
    inv: dict[str, int] = {}
    args = sys.argv[1:]
    for arg in args:
        try:
            key_and_val = arg.split(":")
            if len(key_and_val) != 2:
                raise Exception(f"Error - invalid parameter '{arg}'")
            if key_and_val[0] in inv.keys():
                raise Exception(f"redundant item '{key_and_val[0]}'"
                                " - discarding")
            item = {key_and_val[0]: int(key_and_val[1])}
            inv.update(item)
        except ValueError as e:
            print(f"quantity error for '{arg.split(":")[0]}': {e}")
        except Exception as e:
            print(e)
    return (inv)


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===\n")
    inv = create_inv()
    print(f"Got inventory: {inv}")
    print(f"Item list: {[key for key in inv.keys()]}")
    print(f"Total quantity of the {len(inv)} items : {sum(inv.values())}")
    highest, highest_val = "highest", float('-inf')
    lowest, lowest_val = "lowest", float('inf')
    for key in inv.keys():
        print(f"Item {key} represents "
              f"{(inv[key] / sum(inv.values())) * 100:.1f}%")
        if inv[key] > highest_val:
            highest, highest_val = key, inv[key]
        if inv[key] < lowest_val:
            lowest, lowest_val = key, inv[key]
    print(f"Item most abundant: {highest} with quantity {highest_val}")
    print(f"Item least abundant: {lowest} with quantity {lowest_val}")
    inv.update({'magic_item': 1})
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    ft_inventory_system()
