def print_sorts(items):
    result = [t[1] for t in sorted([(abs(item), item) for item in items], reverse=True)]
    print("no lambda:", result)

    result_with_lambda = sorted(items, reverse=True, key=lambda x: abs(x))
    print("with lambda:", result_with_lambda)

if __name__ == '__main__':
    data = [-12, 1, -1, 2, 3, -14, 12, 14]
    print_sorts(data)
    