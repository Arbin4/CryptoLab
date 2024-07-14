def exhaust_memory():
    a = []
    try:
        while True:
            a.append(' ' * 10 ** 6)  # Allocate 1 MB repeatedly
    except MemoryError:
        print("Memory exhausted!")


if __name__ == "__main__":
    exhaust_memory()
