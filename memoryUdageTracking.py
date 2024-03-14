import psutil


def track_memory():
    memory_usage = psutil.Process().memory_info().rss / 1024 / 1024
    print(f"Current memory usage: {memory_usage:.2f} MB")


def main():
    # Track memory before and after an operation
    track_memory()
    # Perform some memory-intensive operation
    track_memory()


if __name__ == "__main__":
    main()
