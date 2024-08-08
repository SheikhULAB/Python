def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1] + [prev_row[j] + prev_row[j+1] for j in range(i - 1)] + [1]
        triangle.append(curr_row)
    return triangle

rows = 5
print("Pascal's Triangle: ")
for row in generate_pascals_triangle(rows):
    print(row)    