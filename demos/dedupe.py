def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            # print("item is:" ,item)
            seen.add(val)

def dedupeSingle(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ == "__main__":
    print("main")
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    aa = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
    print(aa)

    b = [1, 5, 2, 1, 9, 1, 5, 10]
    bb = list(dedupeSingle(b))
    print(bb)