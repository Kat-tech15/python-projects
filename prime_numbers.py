def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return  True

prime_numbers = [str(num) for num in range (1, 251) if is_prime(num)]
with open("results.txt", "w") as file:
    file.write("Prime numbers between 1 and 250:\n")
    file.write(", ".join(prime_numbers))
user_input = int(input("Enter a number to check if it's prime: "))
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

print("Prime numbers have been saved to results.txt.")
