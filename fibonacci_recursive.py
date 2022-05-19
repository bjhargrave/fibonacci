class Fibonacci:
    called = 0

    def f(self, i: int) -> int:
        # print(f'computing f({i})')
        self.called += 1
        if i == 0:
            return 0
        if i == 1:
            return 1
        return self.f(i-1) + self.f(i-2)


for n in range(20):
    fib = Fibonacci()
    print(f'f({n}) = {fib.f(n)}: called {fib.called}')
