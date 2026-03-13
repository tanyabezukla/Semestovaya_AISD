from strintmap import StrIntMap

def main():
    m = StrIntMap()

    print("put")
    m.put("cat", 10)
    m.put("dog", 7)
    m.put("mouse", 11)
    print('put("cat", 10), put("dog", 7), put("mouse", 11)')

    print("\nget")
    print(f'get("mouse") == {m.get("mouse")}')
    print(f'get("squirrel") == {m.get("squirrel")}')

    print("\ncontains")
    print(f'contains("dog") == {m.contains("dog")}')
    print(f'contains("fish") == {m.contains("fish")}')

    print("\nsize")
    print(f'size() == {m.size()}')

    print("\nkeys")
    print(f'keys() == {m.keys()}')

    print("\nremove")
    m.remove("dog")
    print('remove("dog")')
    print(f'contains("dog") == {m.contains("dog")}')
    print(f'size() == {m.size()}')
    m.remove("fish")
    print('remove("fish") — ключа нет, ничего не изменилось')

    print("\nrehash")
    print(f'capacity до: {m.capacity}')
    m.rehash()
    print(f'capacity после: {m.capacity}')
    print(f'size после rehash: {m.size()}')


if __name__ == "__main__":
    main()
