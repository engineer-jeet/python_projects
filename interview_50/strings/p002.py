# Given a file, print the last N lines in reverse order (without loading unnecessary data).

with open("line_numbers.txt", 'w') as f:
    for i in range(1, 101):
        f.write(f"This is line number {i}\n")


def reverse_last_n_lines(filename, n):
    with open(filename) as f:
        lines = f.readlines()
    # Take last n lines and reverse using slicing

    for line in lines[-n:][::-1]:
        print(line.strip())

        



reverse_last_n_lines('line_numbers.txt', 3)
