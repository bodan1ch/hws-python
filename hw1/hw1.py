def odd_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number


def multiples_of_five(start, end):
    for number in range(start, end + 1):
        if number % 5 == 0:
            yield number


def palindromes(start, end):
    for number in range(start, end + 1):
        if str(number) == str(number)[::-1]:
            yield number


print("Выберите задание:")
print("1 — нечётные числа в диапазоне")
print("2 — числа, кратные пяти, в диапазоне")
print("3 — палиндромы в диапазоне")

choice = input("Введите номер задания (1-3): ")
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if choice == "1":
    result = odd_numbers(start, end)
elif choice == "2":
    result = multiples_of_five(start, end)
elif choice == "3":
    result = palindromes(start, end)
else:
    print("Нет задания с таким номером.")
    result = None

if result is not None:
    print("Результат:", list(result))
