from concurrent import futures
import threading

words = ['hello', 'world']
result = []


def letter_by_letter(my_word):
    for letter in my_word:
        # proof that we are using 2 threads
        print(threading.current_thread().getName())
        result.append(letter)


# thanks to `with`, script will wait until all threads in executor stops
with futures.ThreadPoolExecutor(max_workers=2) as executor:
    [executor.submit(letter_by_letter, word) for word in words]


print(''.join(result))
