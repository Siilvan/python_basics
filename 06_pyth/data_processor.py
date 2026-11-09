from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.store: list[Any] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        result: tuple[int, str] = (self.rank, self.store.pop(0))
        self.rank += 1
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        data_list = data if isinstance(data, list) else [data]
        for item in data_list:
            if not isinstance(item, (int | float)) or isinstance(item, bool):
                return False
        return True

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        data_list = data if isinstance(data, list) else [data]
        for item in data_list:
            self.store.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        data_list = data if isinstance(data, list) else [data]
        for item in data_list:
            if not isinstance(item, str):
                return False
        return True

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper string data")
        data_list = data if isinstance(data, list) else [data]
        for item in data_list:
            self.store.append(str(item))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not data:
            return False
        data_list = data if isinstance(data, list) else [data]
        for item in data_list:
            if not isinstance(item, dict):
                return False
            if set(item) != {"log_level", "log_message"}:
                return False
            if not all(isinstance(value, str) for value in item.values()):
                return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        data_list = data if isinstance(data, list) else [data]
        for item in data_list:
            self.store.append(": ".join(
                [item["log_level"], item["log_message"]]))


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    nbr_proc = NumericProcessor()
    print(f" Trying to validate input '42': {nbr_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {nbr_proc.validate('Hello')}")
    try:
        print(" Test invalid ingestion of string 'foo' with validation:")
        nbr_proc.ingest('foo')
    except Exception as e:
        print(f" Caught exception: {e}")
    print(" Processing data: [1, 2, 3, 4, 5]")
    nbr_proc.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for i in range(3):
        nbr_item = nbr_proc.output()
        print(f" Numeric value {nbr_item[0]}: {nbr_item[1]}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()
    print(f" Trying to validate input '42': {txt_proc.validate(42)}")
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    txt_proc.ingest(['Hello', 'Nexus', 'World'])
    print(" Extracting 1 value...")
    txt_item = txt_proc.output()
    print(f" Text value {txt_item[0]}: {txt_item[1]}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {data}")
    log_proc.ingest(data)
    print(" Extracting 2 values...")
    for i in range(2):
        log_item = log_proc.output()
        print(f" Log entry {log_item[0]}: {log_item[1]}")


if __name__ == "__main__":
    main()
