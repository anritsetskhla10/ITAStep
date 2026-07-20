# დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და შეამოწმებს ეს რიცხვი არის თუ არა მარტივი

# შემდეგ ნაკადების გამოყენებით გაუშვით ეს ფუნქცია პარალელურად რომ შეამოწმოს შემდეგ ლისტში
# num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51] ყველა რიცხვი და დააბრუნოს პასუხი

import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_in_list(num_list):

    results = {}
    threads = []

    def worker(index, num):
        result = is_prime(num)
        print(f"Number: {num}, Is Prime: {result}")
        results[index] = result
        print(f"Thread {index} finished processing number: {num}")

    for i, num in enumerate(num_list):
        thread = threading.Thread(target=worker, args=(i, num))
        print(f"Starting thread {i} for number: {num}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_results = []
    for i in range(len(num_list)):
        final_results.append(results[i])
    return final_results


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]
print(check_prime_in_list(num_list))