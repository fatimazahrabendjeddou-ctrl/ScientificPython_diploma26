import time

class Exercises:

    def ex1(self):
        # quadratic equation
        def solve_quadratic_eqt(a, b, c):
            if a == 0:
                print("This is not a quadratic equation (a = 0).")
                return
            delta = b**2 - 4*a*c
            if delta < 0:
                print("No real solutions because delta < 0")
            elif delta == 0:
                x = -b / (2*a)
                print("One real solution:", x)
            else:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)
                print("Solutions:", x1, "and", x2)

        solve_quadratic_eqt(1, -3, 2)


    def ex2(self):
        # Recamán sequence
        def recaman(N):
            seq = [0]
            seen = {0}
            for n in range(1, N):
                c = seq[-1] - n
                if c > 0 and c not in seen:
                    seq.append(c)
                    seen.add(c)
                else:
                    new_num = seq[-1] + n
                    seq.append(new_num)
                    seen.add(new_num)
            return seq

        print(recaman(48))


    def ex3(self):
        mylist = [1, -99, 89, 0, 234, 77, -748, 11]
        print(sorted(mylist, reverse=True))
        print(mylist)


    def ex4(self):
        l = [1, 2, 3, 4, 5, 6]
        m = [3, 5, 7, 9, 10]
        print(set(l).intersection(set(m)))


    def ex5(self):
        def pairs(n):
            p = []
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    p.append((i, n // i))
            return p

        print(pairs(12))


    def ex6(self):
        REPEAT = 10000

        start = time.time()
        for _ in range(REPEAT):
            lst = []
            for i in range(1000):
                if i % 3 == 0:
                    lst.append(i)
        print("Naive time:", time.time() - start)

        start = time.time()
        for _ in range(REPEAT):
            lst = [i for i in range(1000) if i % 3 == 0]
        print("List comprehension time:", time.time() - start)

        start = time.time()
        for _ in range(REPEAT):
            lst = list(range(1000))[::3]
        print("Slicing time:", time.time() - start)

        start = time.time()
        for _ in range(REPEAT):
            lst = list(range(0, 1000, 3))
        print("Range time:", time.time() - start)


    def ex7(self):
        def is_palindrome(s):
            s = s.lower()
            return s == s[::-1]

        print(is_palindrome("mom"))


    def ex8(self):
        def max_occurrence(s):
            s = s.replace(" ", "")
            return max((c, s.count(c)) for c in s)

        print(max_occurrence("babababaaaa"))


    def ex9(self):
        def first_n_primes(N):
            if N < 1:
                return []
            size = max(15, N * 10)
            while True:
                sieve = [True] * size
                sieve[0] = sieve[1] = False
                for i in range(2, int(size**0.5) + 1):
                    if sieve[i]:
                        for j in range(i*i, size, i):
                            sieve[j] = False
                primes = [i for i, is_prime in enumerate(sieve) if is_prime]
                if len(primes) >= N:
                    return primes[:N]

        print(first_n_primes(10))
