from functools import reduce
from typing import Any, Protocol

import pyphen

type Processable = str | list[str]

class Processor(Protocol):
    def positions(self, *args, **kwargs) -> Any:
        ...

    def inserted(self, *args, **kwargs) -> Any:
        ...


def process_text(text: Processable, processor: Processor) -> list[tuple[int, str]]:

    def process_line(line: Processable) -> tuple[int, str]:

        def process_word(word: Processable) -> tuple[int, str]:
            return len(processor.positions(word)) + 1, processor.inserted(word)

        word_results = list(map(process_word, line.split()))
        return (
            reduce(lambda acc, x: acc + x[0], word_results, 0),
            ' '.join(list(map(lambda x: x[1], word_results)))
        )

    return list(map(process_line, text.splitlines()))


if __name__ == '__main__':
    print(process_text(
        """И вновь нет сна, не спится мне
                На сей раз есть причина.""",
        pyphen.Pyphen(lang='ru')))