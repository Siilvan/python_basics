import alchemy.grimoire.dark_spellbook as dark


def main() -> None:
    print("== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    spell: str = "dark_Fantasy"
    ingredient: str = "Bat, eye-ball, arsenic"
    print("Testing record dark spell: "
          f"{dark.dark_spell_record(spell, ingredient)}")


if __name__ == "__main__":
    main()
