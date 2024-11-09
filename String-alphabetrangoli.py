def print_rangoli(size):
    # The width of the largest line in the rangoli
    width = 4 * size - 3
    lines = []
    
    # Create the top half of the rangoli, including the middle line
    for i in range(size):
        # Generate the descending part of the line (from outermost letter to 'a')
        left_part = [chr(ord('a') + size - j - 1) for j in range(i + 1)]
        full_line = '-'.join(left_part + left_part[-2::-1])
        lines.append(full_line.center(width, '-'))
    print("\n".join(lines + lines[-2::-1]))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
