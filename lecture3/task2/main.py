from time import sleep


def controlled_execution(call_count, start_sleep_time, factor, border_sleep_time):
    def controlled_function(func):
        def wrapper(*args, **kwargs):
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            t = start_sleep_time
            for count in range(1, call_count + 1):
                func_result = func(*args, **kwargs)
                output = f'Запуск номер {count}. Ожидание: {t} секунд. Результат декорируемой функций = {func_result}.'
                print(output)
                sleep(t)
                t *= (2 ** factor)
                if t >= border_sleep_time:
                    t = border_sleep_time
            print('Конец работы')

        return wrapper

    return controlled_function
