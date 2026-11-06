import dotenv
import os

WARN = "\033[1;31m[WARNING]\033[0m"
SECRET_KEYS = ("API_KEY", "DATABASE_URL", "LOG_LEVEL", "ZION_ENDPOINT")


def security_check(before: dict[str, str]) -> None:
    here = os.path.dirname(os.path.abspath(__file__))

    with open(__file__) as f:
        source: str = f.read()
    secrets: list[str] = [os.environ[k]
                          for k in SECRET_KEYS if os.environ.get(k)]
    hardcoded: bool = any(value in source for value in secrets)

    try:
        with open(os.path.join(here, ".gitignore")) as f:
            lines = [line.strip() for line in f]
        ignored: bool = ".env" in lines
    except OSError:
        ignored = False

    from_env = [k for k in SECRET_KEYS if k in before]

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected" if not hardcoded
          else f"{WARN} A secret value appears in the source code!")
    print("[OK] .env file properly ignored by git" if ignored
          else f"{WARN} .env is not listed in .gitignore!")
    print("[OK] Production overrides available" +
          (f" (from environment: {', '.join(from_env)})" if from_env else ""))


def oracle() -> None:
    print("ORACLE STATUS: Consulting the configuration...\n")
    if not dotenv.load_dotenv():
        print(f"{WARN} No .env file or it doesnt containt values.\n")

    matrix_mode = os.getenv("MATRIX_MODE") or "development"
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL") or "INFO"
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print(f"Mode: {matrix_mode}")
    print(f"Database: "
          f"{'Connected to local instance' if db_url else "default_db_url"}")
    print(f"API Access: {'Authenticated' if api_key else "default_api_key"}")
    if matrix_mode == "development":
        print(f"Log Level: {log_level}")
    print(f"Remote Network: "
          f"{'Connected' if zion_endpoint else "default_endpoint"}")
    if all(os.getenv(key) for key in SECRET_KEYS):
        print("\nThe Oracle sees all configurations.")
    else:
        print(f"\n{WARN} Missing some keys")


def main() -> None:
    before = dict(os.environ)
    dotenv.load_dotenv()
    oracle()
    security_check(before)


if __name__ == "__main__":
    main()
