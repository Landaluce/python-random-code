import random
import threading
import psutil
import gc


counter = 0


def track_memory():
    memory_usage = psutil.Process().memory_info().rss / 1024 / 1024
    print(f"Current memory usage: {memory_usage:.2f} MB")


def increment():
    global counter
    counter = 0
    counter = sum([counter + 1 for _ in range(100000)])


def create_objects():
    for _ in range(1000):
        data = [random.random() for _ in range(10000)]


def main():
    threads = []

    for _ in range(4):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")  # Might not be 400000 due to GIL
    track_memory()
    create_objects()
    track_memory()
    gc.collect()
    track_memory()
    gc.collect()
    track_memory()


if __name__ == "__main__":
    main()
