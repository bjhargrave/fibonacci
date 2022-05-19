class Fibonacci:
    called = 0
    looped = 0

    def f(self, i: int) -> int:
        print(f'computing f({i})')
        self.called += 1
        prev, accumulator = 1, 0
        for j in range(i):
            prev, accumulator = accumulator, prev + accumulator
            self.looped += + 1
        return accumulator


for n in range(20):
    fib = Fibonacci()
    print(f'f({n}) = {fib.f(n)}: called {fib.called} looped: {fib.looped}')
