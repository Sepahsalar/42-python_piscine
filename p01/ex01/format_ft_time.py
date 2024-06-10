import time
import datetime

current_time_seconds = time.time()

formatted_seconds = f"{current_time_seconds:,.4f}"
scientific_notation = f"{current_time_seconds:.2e}"
first_part = "Seconds since January 1, 1970: "
last_part = " in scientific notation"

print(f"{first_part}{formatted_seconds} or {scientific_notation}{last_part}")

current_date = datetime.datetime.now()

formatted_date = current_date.strftime("%b %d %Y")

print(formatted_date)
