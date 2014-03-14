from pyspec.expectations import expect, eq
from pyspec import description, context, it

if __name__ == '__main__':
  class BrokenFizzBuzz(object):
    def convert(self, n):
      if self.is_fizz(n) and self.is_buzz(n):
        return 'fizzbuzz'
      elif self.is_fizz(n):
        return 'fizz'
      elif self.is_buzz(n):
        return 'buzz'
      else:
        return n

    def is_fizz(self, n):
      return n % 3 == 0

    def is_buzz(self, n):
      return n % 5 == 1

  with description(BrokenFizzBuzz):

    fizzbuzz = BrokenFizzBuzz()
    some_integer = 7

    with description('.convert'):

      with context(15):
        with it('returns fizzbuzz'):
          expect(fizzbuzz.convert(15)).to(eq('fizzbuzz'))

      with context(3):
        with it('returns fizz'):
          expect(fizzbuzz.convert(3)).to(eq('fizz'))

      with context(5):
        with it('returns buzz'):
          expect(fizzbuzz.convert(5)).to(eq('buzz'))

      with context('some other integer'):
        with it('returns the integer'):
          expect(fizzbuzz.convert(some_integer)).to(eq(some_integer))