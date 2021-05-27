from scipy.io import mmread


def main():
    a = mmread('rec-amazon.mtx')
    print(a)


if __name__ == '__main__':
    main()
