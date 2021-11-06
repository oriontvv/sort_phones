import io
import logging
from pathlib import Path
from argparse import ArgumentParser


import ext_sort

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)-8s] %(asctime)-15s (%(name)s): %(message)s",
)


class PhoneSerializer(ext_sort.Serializer):
    def __init__(self, writer):
        super().__init__(io.TextIOWrapper(writer, write_through=True))

    def write(self, item):
        self._writer.write(item)


class PhoneDeserializer(ext_sort.Deserializer):
    def __init__(self, reader):
        super().__init__(io.TextIOWrapper(reader))

    def read(self):
        return next(self._reader)


def main():

    parser = ArgumentParser()
    parser.add_argument("--path", required=True, help="path to dir with files")
    parser.add_argument("--chunk_size", default=10_000_000, type=int, help="chunk size")
    args = parser.parse_args()

    path = Path(args.path)
    phones_path = path / "phones.txt"
    sorted_path = path / "sorted.txt"

    with open(phones_path, "rb") as unsorted_file:
        with open(sorted_path, "wb") as sorted_file:
            ext_sort.sort(
                reader=unsorted_file,
                writer=sorted_file,
                chunk_size=args.chunk_size,
                Serializer=PhoneSerializer,
                Deserializer=PhoneDeserializer,
                tmp_dir=path,
            )


if __name__ == "__main__":
    main()
