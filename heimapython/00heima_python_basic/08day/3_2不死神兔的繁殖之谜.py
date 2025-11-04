def get_rabbit(a):
    if a ==1 or a==2:
        return 1
    else:
        return get_rabbit(a-1) + get_rabbit(a-2)

if __name__ == '__main__':
    print(get_rabbit(1))
    print(get_rabbit(2))
    print(get_rabbit(23))