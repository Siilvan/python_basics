import alchemy.grimoire as light


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell: str = "Fantasy"
    ingredient: str = "Earth, wind and fire"
    print("Testing record light spell: "
          f"{light.light_spell_record(spell, ingredient)}")


if __name__ == "__main__":
    main()
