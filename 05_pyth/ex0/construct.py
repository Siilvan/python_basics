import os
import sys
import site


def construct() -> None:
    venv_flag: bool = sys.prefix != sys.base_prefix
    print("\nLABORATORY STATUS:",
          "The laboratory is sealed" if venv_flag
          else "You are working in the open")
    print(f"\nCurrent Python: {sys.executable}")
    env: str = (os.path.basename(path)
                if (path := os.environ.get("VIRTUAL_ENV"))
                else "None detected")
    print(f"Virtual Environment: {env}")
    if venv_flag:
        print(f"Environment Path: {path}")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecing the global system.")
        print(f"\nReagant installation path:\n{site.getsitepackages()[0]}")
    else:
        print("\nWARNING: You are in the global environment!")
        print("Every reagant you install here leaks into the whole system.")
        print("\nTo seal the laboratory, run:\npython3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    construct()
