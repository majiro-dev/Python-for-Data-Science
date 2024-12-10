import time

current_time = time.time()
formatted_time = time.strftime("%b %d %Y", time.gmtime(current_time))

print(f"Seconds since January 1, 1970: {current_time:.4f}",
        f"or {current_time:.2e} in scientific notation")

print(formatted_time)