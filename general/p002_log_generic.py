# Given a file, print the last N lines in reverse order (without loading unnecessary data).

with open("line_numbrs.txt", 'w') as file:
    for i in range(1, 11):
        file.write("This is line {}\n".format(i))


def reverse_last_n_lines(filename, n):
    with open(filename) as f:
        lines = f.readlines()
    # Take last n lines and reverse using slicing

    for line in lines[-n:][::-1]:
        print(line.strip())

reverse_last_n_lines('line_numbrs.txt', 3)

#Remove first k and last k lines and write remaining content to a new file.

