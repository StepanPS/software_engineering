from datetime import datetime as dt
import time

start_time = dt.now()

for X in range(int(5)):
    current_time = dt.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    print(f"Текущее время: {formatted_time}")
    time.sleep(1)
