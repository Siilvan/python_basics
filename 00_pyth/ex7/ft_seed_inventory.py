def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    res: str = f"{seed_type.capitalize()} seeds: "
    if unit == "packets":
        res += f"{quantity} packets available"
    elif unit == "grams":
        res += f"{quantity} grams total"
    elif unit == "area":
        res += f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(res)
