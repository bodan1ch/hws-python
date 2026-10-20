import time


def horizontal_line(symbol):
    print(symbol * 20)


def vertical_line(symbol):
    for _ in range(10):
        print(symbol)


def show_line(symbol, function_to_call):
    function_to_call(symbol)


def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Время выполнения функции: {elapsed:.6f} секунд")
        return result

    return wrapper


@measure_time
def calculate_sum(n):
    return sum(range(1, n + 1))


print("Выберите тип линии:")
print("1 — горизонтальная")
print("2 — вертикальная")
choice = input("Ваш выбор (1-2): ")
symbol = input("Введите символ для линии: ")

if choice == "1":
    show_line(symbol, horizontal_line)
elif choice == "2":
    show_line(symbol, vertical_line)
else:
    print("Нет линии с таким номером.")

result = calculate_sum(1_000_000)
print(f"Сумма чисел: {result}")
