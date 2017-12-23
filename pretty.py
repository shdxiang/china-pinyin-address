import logging
import argparse
import json
import locale
from xpinyin import Pinyin

logFormat = '%(asctime)s %(filename)s [%(lineno)d][%(levelname)s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logFormat)

pinyin = Pinyin()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file", type=str)
    parser.add_argument("key", help="sort key", type=str)
    args = parser.parse_args()

    with open(args.file, encoding='utf8') as file:
        data = file.read()

    items = json.loads(data)

    items_sorted = sorted(
        items, key=lambda k: pinyin.get_pinyin(k[args.key], ''))
    with open(args.file, 'w', encoding='utf8') as file:
        json.dump(items_sorted, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
