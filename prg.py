def spiral_traversal(matrix, start_dir="right"):
    if not matrix or not matrix[0]:
        return []

    directions = ["right", "down", "left", "up"]
    dir_idx = directions.index(start_dir)

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    result = []

    while top <= bottom and left <= right:
        if directions[dir_idx] == "right":
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        elif directions[dir_idx] == "down":
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        elif directions[dir_idx] == "left":
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        elif directions[dir_idx] == "up":
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        dir_idx = (dir_idx + 1) % 4  # Move to next direction

    return result


# 🔹 Example usage:
if __name__ == "__main__":
    matrix = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13,14,15,16]
    ]
    direction = input("Enter starting direction (right/down/left/up): ").strip().lower()

    print("Spiral Traversal starting", direction, "→")
    print(spiral_traversal(matrix, direction))
