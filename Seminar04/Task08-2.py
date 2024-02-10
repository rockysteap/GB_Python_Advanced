java, python, rust, javas, pythons, s = range(6)


def fn():
    for k, v in globals().items():
        if len(k) > 1 and k.endswith("s"):
            globals()[k] = None
            globals()[k[:-1]] = v


if __name__ == '__main__':
    print(java, python, rust, javas, pythons, s)
    fn()
    print(java, python, rust, javas, pythons, s)
