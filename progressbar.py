import math
import colorama


def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")


# Example Usage

numbers = [x * 5 for x in range(2000, 2500)]
results = []

# Initialize progess to zero
progress_bar(0, len(numbers))

for i, m in enumerate(numbers):
    results.append(math.factorial(m))
    # Increment progress bar
    progress_bar(i + 1, len(numbers))

print(colorama.Fore.RESET)
