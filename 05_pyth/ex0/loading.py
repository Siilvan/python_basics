import importlib


def load() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("\nChecking dependencies:")
    count: int = 0
    packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        }
    for name, desc in packages.items():
        try:
            mod = importlib.import_module(name)
            print(f"\033[32m[OK]\033[0m {name} ({mod.__version__}) - {desc}")
            count += 1
        except ImportError as e:
            print(f"\033[31m[ERR]\033[0m Error while importing '{name}': {e}")

    print("pip vs Poetry:\n"
          "requirements.txt declares what to install;"
          " pip resolves it at install time.\n"
          "pyproject.toml declares the same constraints,"
          " and Poetry pins the resolved "
          "versions in poetry.lock so every install is identical.")
    if count != len(packages):
        print("\nNot every required package is installed."
              "\nTo install run:"
              "\npip install -r requirements.txt  # To install with pip"
              "\npoetry install  # To install with poetry")
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    load()
