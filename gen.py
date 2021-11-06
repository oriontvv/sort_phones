from argparse import ArgumentParser


def gen(path):
    # +79XXXXXXXXX
    print(f"Writing to {path}")
    with open(path, "w") as f:
        # simulate "random-like"
        for phone in range(10 ** 9 - 1, -1, -1):
            f.write(f"+79{phone:09}\n")


def main():
    parser = ArgumentParser()
    parser.add_argument("--path", required=True, help="path to file")
    args = parser.parse_args()

    gen(args.path)


main()
