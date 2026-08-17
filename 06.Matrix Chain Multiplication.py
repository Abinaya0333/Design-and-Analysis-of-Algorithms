def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming

    dims: list of dimensions
    Matrix i has dimensions dims[i-1] x dims[i]

    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """

    n = len(dims) - 1

    # m[i][j] = minimum number of scalar multiplications
    # required to multiply matrices i through j
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # s[i][j] = position at which the optimal split occurs
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # l is the chain length
    for l in range(2, n + 1):

        # i is the starting matrix
        for i in range(1, n - l + 2):

            # j is the ending matrix
            j = i + l - 1

            # Initially set cost to infinity
            m[i][j] = float('inf')

            # Try every possible split position
            for k in range(i, j):

                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + dims[i - 1] * dims[k] * dims[j]
                )

                # If this split gives minimum cost
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):

    # If there is only one matrix
    if i == j:
        return f"A{i}"

    # Get the optimal split position
    k = s[i][j]

    # Find optimal parenthesization of left part
    left = print_optimal_parens(s, i, k)

    # Find optimal parenthesization of right part
    right = print_optimal_parens(s, k + 1, j)

    return f"({left} x {right})"


def print_dp_table(m, n):

    print("\nDP Cost Table m[i][j]:")

    # Print column headings
    print(f'{"":>6}', end='')

    for j in range(1, n + 1):
        print(f"A{j:>8}", end='')

    print()

    # Print table values
    for i in range(1, n + 1):

        print(f"A{i:<5}", end='')

        for j in range(1, n + 1):

            if j < i:
                print(f'{"---":>9}', end='')
            else:
                print(f"{m[i][j]:>9}", end='')

        print()


# -------------------------------------------------
# Main Program
# -------------------------------------------------

# Matrix dimensions:
# A1 = 10 x 30
# A2 = 30 x 5
# A3 = 5 x 60
# A4 = 60 x 10

dims = [10, 30, 5, 60, 10]

n = len(dims) - 1


# Display matrix dimensions
print("Matrix Dimensions:")

for i in range(n):
    print(f" A{i + 1}: {dims[i]} x {dims[i + 1]}")


# Calculate optimal matrix chain order
m, s = matrix_chain_order(dims)


# Display minimum cost
print(f"\nMinimum scalar multiplications: {m[1][n]}")


# Display optimal parenthesization
print(
    f"Optimal parenthesization: "
    f"{print_optimal_parens(s, 1, n)}"
)


# Display DP table
print_dp_table(m, n)
