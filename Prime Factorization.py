# Version 1
#
# q1 = int(input("Number to prime factorize: "))
# for i in range(2, q1 + 1):
#   count = 0
#   while q1 % i == 0:
#     q1 /= i
#     count += 1
#     if q1 % i != 0:
#       if count > 1:
#         print(f'{i}^{count}', end='')
#         if q1 != 1:
#           print('*', end='')
#       else:
#         print(f'{i}', end='')
#         if q1 != 1:
#           print('*', end='')
# print()


# Optimised Version
import math # to use sqrt()

def prime_factors(n):
  """
  Returns a list of factors.
  Example: 24 yields [2,2,2,3]
  """
  factors = []  # for storing the list of factors
  i = 2
  n_sqrt = math.sqrt(n)
  while i <= n_sqrt:  # only need to go until n^(1/2)
    if n % i != 0:  # i is not a factor of n
      i += 1  # move to the next 'i'
    else:
      factors.append(i)
      n //= i
  if n > 1:
    factors.append(n)
  return factors


def print_factors(factors):
  """Takes in a list of factors and formats it."""
  unique_factors = sorted(list(set(factors)))
  string = ""
  for factor in unique_factors:
    string += str(factor)
    factor_count = factors.count(factor)
    if factor_count > 1:
      string += f"^{factor_count}"
    string += "*"
  return string[:-1] # get rid of one trailing "*"


num = int(input("Number to prime factorize: "))
print(print_factors(prime_factors(num)))
