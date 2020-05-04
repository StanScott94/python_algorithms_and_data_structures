import time

def recursive_countdown_timer(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        return recursive_countdown_timer(n - 1)

def iteration_countdown_timer(n):
    while n >= 0:
        print(n)
        time.sleep(1)
        n -= 1

time_to_count_down = 10
print(f"Counting down from {time_to_count_down}")
#iteration_countdown_timer(time_to_count_down)
print(recursive_countdown_timer(time_to_count_down))
