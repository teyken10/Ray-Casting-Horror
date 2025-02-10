import time

# Считываем текущее время в секундах с начала эпохи (1 января 1970)
current_time = time.time()
print(f"Текущее время: {current_time} секунд с начала эпохи.")

# Засекаем время выполнения какого-либо кода
start_time = time.time()
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд.")
