# Generate all Pythagorean Triplets with side length less than or equal to 30
def find_triplets(limit):
    triplets = []
    for a in range(1, limit+1):
        for b in range(a, limit+1): # starting from a to avoid duplicates
            for c in range(b, limit+1):
                if a**2 + b**2 == c**2:
                    triplets.append((a, b, c))
    return triplets

limit = 30
triplets = find_triplets(limit)

print("Pythagorean triplets from 1 to 30:")
for triplet in triplets:
    print(triplets)