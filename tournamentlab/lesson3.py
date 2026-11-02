from itertools import combinations

teams = ["A", "B", "C", "D"]


def generate_fixtures(teams):
    fixtures = []

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            fixtures.append((teams[i], teams[j]))

    return fixtures


# Method 1: Nested loops
fixtures = generate_fixtures(teams)

print("Nested loops:")
for fixture in fixtures:
    print(f"{fixture[0]} vs {fixture[1]}")

print(f"\nTotal fixtures: {len(fixtures)}")


# Method 2: itertools.combinations
print("\nitertools.combinations:")

other_fixtures = list(combinations(teams, 2))

for fixture in other_fixtures:
    print(f"{fixture[0]} vs {fixture[1]}")

print(f"\nTotal fixtures: {len(other_fixtures)}")

# Verify that both methods produce the same result.
assert fixtures == other_fixtures

print("\nBoth methods produce the same fixtures!")