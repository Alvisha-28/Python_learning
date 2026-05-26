#statistical calculator
def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def mode(numbers):
    frequency = {}
    for n in numbers:
        frequency[n] = frequency.get(n, 0) + 1
    max_frequency = max(frequency.values())
    return [k for k, v in frequency.items() if v == max_frequency]

# Example usage:
data = [1, 2, 2, 3, 4, 4, 4, 5]
print("Mean:", mean(data))
print("Median:", median(data))
print("Mode:", mode(data))