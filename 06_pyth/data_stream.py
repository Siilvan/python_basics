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


class DataStream():
    def __init__(self) -> None:
        self.proc_list: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        if proc in self.proc_list:
            print("\033[1;31m[ERROR]\033[0m: processor already registered")
        else:
            self.proc_list[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = 0
            for proc in self.proc_list.keys():
                if proc.validate(element):
                    old_size = len(proc.store)
                    proc.ingest(element)
                    self.proc_list[proc] += len(proc.store) - old_size
                    processed = 1
                    continue
            if processed == 0:
                print("\033[31mDataStream error\033[0m - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self.proc_list:
            print("No processor found, no data")
            return
        for proc in self.proc_list:
            print(f"{type(proc).__name__}: "
                  f"total {self.proc_list[proc]} items processed, "
                  f"remaining {len(proc.store)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream\n\n Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("Registering Numeric Processor")
    nbr_proc = NumericProcessor()
    stream.register_processor(nbr_proc)
    data_batch = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO',
          'log_message': 'User wil isconnected'}],
        42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data_batch}")
    stream.process_stream(data_batch)
    stream.print_processors_stats()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)
    print("Registering other data processors\nSend the same batch again")
    stream.process_stream(data_batch)
    stream.print_processors_stats()
    print("Consume some elements from the processors: number 3, text 2, log 1")
    txt_proc.output()
    txt_proc.output()
    nbr_proc.output()
    nbr_proc.output()
    nbr_proc.output()
    log_proc.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
