def main():
    sumsq = sum([i**2 for i in range(1, 101)])
    sqsum = sum(list(range(1, 101)))**2
    # print(sumsq,sqsum,sqsum - sumsq)
    print(sqsum - sumsq)


if __name__ == '__main__':
    main()
