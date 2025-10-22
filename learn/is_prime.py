nums = range(1, 1000)
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, n): # Check divisibility from 2 to n-1
        if n % i == 0: # If n is divisible by any number other than 1 and itself, it's not prime
            return False
    return True

primes = list(filter(is_prime,nums)) #[num for num in nums if is_prime(num)]
print(f"Primes in range {nums.start} to {nums.stop - 1}: {primes}")