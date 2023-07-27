def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle

if __name__ == "__main__":
    n = 5
    print_triangle(pascal_triangle(n))
