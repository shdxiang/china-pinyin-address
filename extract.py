import logging
import argparse
import json

logFormat = '%(asctime)s %(filename)s [%(lineno)d][%(levelname)s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logFormat)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="source file", type=str)
    parser.add_argument("dest_en", help="dest en file", type=str)
    parser.add_argument("dest_cn", help="dest cn file", type=str)
    args = parser.parse_args()

    with open(args.src, encoding='utf8') as file:
        data = file.read()

    items = json.loads(data)

    items_en = []
    items_cn = []

    for item in items:
        logging.debug(item)
        item_en = {
            'key': item['code'],
            'value': item['en']
        }
        items_en.append(item_en)
        item_cn = {
            'key': item['code'],
            'value': item['cn']
        }
        items_cn.append(item_cn)

    with open(args.dest_en, 'w', encoding='utf8') as file:
        json.dump(items_en, file, ensure_ascii=False)

    with open(args.dest_cn, 'w', encoding='utf8') as file:
        json.dump(items_cn, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
