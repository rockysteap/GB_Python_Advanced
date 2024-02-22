# PS C:\Users\PycharmProjects> python -m doctest .\prime.py
# PS C:\Users\PycharmProjects> python -m doctest .\prime.py -v
# PS C:\Users\PycharmProjects> python -m doctest .\prime.md
# PS C:\Users\PycharmProjects> python -m doctest .\prime.md -v
# -m -> use module
# -v -> visual

if __name__ == '__main__':
    import doctest

    doctest.testfile('prime.md', verbose=True)
