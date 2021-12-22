def field(dictlist, *keys):
    assert len(keys) > 0
    if len(keys) == 1:
        for d in dictlist:
            yield d[keys[0]]
        return
    result = []
    for d in dictlist:
        rd = {}
        for key in keys:
            if key in d.keys():
                rd[key] = d[key]
        if len(rd) > 0:
            result.append(rd)
        yield rd

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

if __name__ == "__main__":
    for item in field(goods, 'title'):
        print(item)
    print(list(field(goods, 'title', 'price')))
