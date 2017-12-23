import logging
import argparse
import json
from xpinyin import Pinyin

logFormat = '%(asctime)s %(filename)s [%(lineno)d][%(levelname)s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logFormat)

pinyin = Pinyin()


def translate_item(item):
    '''
    {'name': '泽库', 'value': '632323', 'parent': '632300'}
    '''
    name = item['name']
    name = pinyin.get_pinyin(name, '')
    item['name'] = name.title()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="source file", type=str)
    parser.add_argument("dest", help="dest file", type=str)
    args = parser.parse_args()

    with open(args.src, encoding='utf8') as file:
        data = file.read()

    items = json.loads(data)

    for item in items:
        logging.debug(item)
        translate_item(item)
        logging.debug(item)

    with open(args.dest, 'w', encoding='utf8') as file:
        json.dump(items, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
