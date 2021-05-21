from scipy.io import mmread


def main():
    a = mmread('test.mtx')
    print(a)


if __name__ == '__main__':
    main()
