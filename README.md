# china-pinyin-address

Translate Chinese address to Pinyin, extract countries and regions form a single file.

## Translate

Input:

```json
{"name": "墨脱", "value": "540423", "parent": "540400"}
```

Out:

```json
{"name": "Motuo", "value": "540423", "parent": "540400"}
```

### Usage

```bash
python translate.py china_address_cn.json china_address_en.json
```

[china_address_cn.json](./china_address_cn.json) is translated to [china_address_en.json](./china_address_en.json)

## Extract

Input:

```json
{"code": "CN", "en": "China", "cn": "中国"}
```

Output:

```json
{"name": "China", "value": "CN"}
```

```json
{"name": "中国", "value": "CN"}
```

### Usage

```bash
python extract.py countries_regions.json countries_regions_en.json countries_regions_cn.json
```

Extract [countries_regions_en.json](./countries_regions_en.json) and [countries_regions_cn.json](./countries_regions_en.json) from [countries_regions.json](./countries_regions.json)

## Pretty

Indent and sort JSON file by `key`.

```bash
python pretty.py china_address_cn.json name
python pretty.py china_address_en.json name
python pretty.py countries_regions.json code
python pretty.py countries_regions_cn.json key
python pretty.py countries_regions_en.json key
```
