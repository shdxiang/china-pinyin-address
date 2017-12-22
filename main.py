import logging
import argparse
import json
from xpinyin import Pinyin

logFormat = '%(asctime)s %(filename)s [%(lineno)d][%(levelname)s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logFormat)

pinyin = Pinyin()


trantab = str.maketrans('', '', u'省市区县乡區縣鄉')


def translate_item(item):
    '''
    {'name': '泽库县', 'value': '632323', 'parent': '632300'}
    '''
    name = item['name'].translate(trantab)
    name = pinyin.get_pinyin(name, '')
    item['name'] = name.title()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="source file", type=str)
    parser.add_argument("dest", help="dest file", type=str)
    args = parser.parse_args()

    with open(args.src) as file:
        data = file.read()

    js = json.loads(data)

    for item in js:
        logging.debug(item)
        translate_item(item)
        logging.debug(item)

    data = json.dumps(js)
    with open(args.dest, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    main()
