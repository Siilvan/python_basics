import math


def get_player_pos() -> tuple[float, float, float]:
    args = input("Enter new coordinates as "
                 "floats in format 'x,y,z': ").split(",", 2)
    try:
        coords = [float(arg) for arg in args]
    except Exception:
        print("Invalid syntax")
        return (get_player_pos())
    if len(coords) != 3:
        print("Invalid syntax")
        return (get_player_pos())
    return (coords[0], coords[1], coords[2])


def calc_distance(set1: tuple[float, float, float],
                  set2: tuple[float, float, float]) -> float:
    distance: float
    distance = math.sqrt(
        ((set2[0] - set1[0]) ** 2) +
        ((set2[1] - set1[1]) ** 2) +
        ((set2[2] - set1[2]) ** 2)
    )
    return distance


def ft_coordinate_system() -> None:
    set1 = get_player_pos()
    print(f"Got a first tuple: {set1}")
    print(f"It includes: X={set1[0]}, Y={set1[1]}, Z={set1[2]}")
    print(f"Distance to center: {calc_distance(set1, (0.0, 0.0, 0.0)):.4f}")
    print("\nGet a second set of coordinates")
    set2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{calc_distance(set1, set2):.4f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    ft_coordinate_system()
