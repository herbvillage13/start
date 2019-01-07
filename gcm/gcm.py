import time

def gcm0(a, b):
    start_time = time.time()
    count = 0

    while a != b:
        count += 1
        if b < a:
            a = a - b
        else:
            b = b - a

    print("gcm0: gcm = {}, gcm_count = {}".format(a, count))
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))

def gcm1(a, b):
    start_time = time.time()

    count = 0
    while a != b:
        count += 1
        while b < a:
            a = a - b
        a, b = b, a

    print("gcm1: gcm = {}, gcm_count = {}".format(a, count))
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))

# gcm1 -> 나머지를 mod 계산으로 구하도록 수정
def gcm2(a, b):
    start_time = time.time()

    count = 0
    while a != b:
        count += 1
        a = a % b
        a, b = b, a
        if b == 0:
            break

    print("gcm2: gcm = {}, gcm_count = {}".format(a, count))
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))

def main():
    a = 30246823540
    b = 430

    gcm0(a, b)
    gcm1(a, b)
    # 사실상 gcd 
    gcm2(a, b)

if __name__ == "__main__":
    # start_time = time.time()
    main()
    # end_time = time.time()
    # print("\n--- %s seconds ---" % (end_time - start_time))