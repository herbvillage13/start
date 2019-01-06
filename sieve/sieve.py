import time
import csv

def mark_sieve(first, last, factor, prime_list):
    prime_list[first] = 0
    while(last - first > factor):
        first += factor
        prime_list[first] = 0

def main():
    number = input("1 부터 x이하의 자연수 중 소수를 찾습니다: ")
    number = int((int(number) - 3) / 2)
    number += 1

    index = range(0, number)
    prime_list = [1 for _ in index]

    i = 0
    index_square = 3
    while(index_square < number):
        if prime_list[i] == 1:
            mark_sieve(index_square, number, 2*i + 3, prime_list)
        i += 1
        index_square = 2*i*(i + 3) + 3

    value = [3]
    for i in range(1, number):
        value.append(2*i+3)

    result1 = [a*b for a,b in zip(prime_list, value)]
    prime = [2]
    for i in result1:
        if i != 0:
            prime.append(i)

    print(prime)
    with open('prime.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(prime)

    print("소수 개수: {}" .format(len(prime)))

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("\n--- %s seconds ---" % (end_time - start_time))