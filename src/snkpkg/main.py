import argparse

from snkpkg.hello import hello


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple greeting CLI")

    # 引数の定義
    parser.add_argument("name", type=str, help="名前を指定してください")

    args = parser.parse_args()
    hello(args.name)


if __name__ == "__main__":
    main()
