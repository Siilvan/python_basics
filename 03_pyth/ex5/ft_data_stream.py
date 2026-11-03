import random
import typing

PLAYERS = ["bob", "alice", "dylan", "charlie"]
ACTIONS = ["swim", "run", "move", 'climb', 'use', 'release', 'grab']


def gen_event() -> typing.Generator[tuple[str, str]]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
        list: list[tuple[str, str]]) -> typing.Generator[tuple[str, str]]:
    while len(list) > 0:
        yield (list.pop(random.randrange(len(list))))


def ft_data_stream() -> None:
    print('=== Game Data Stream Processor ===')
    event_generator = gen_event()
    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_list = [next(event_generator) for i in range(10)]
    print(f"Built list of 10 event: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()
