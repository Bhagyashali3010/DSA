from collections import defaultdict

def count_valid_quadruples(x):
    n = len(x)
    count = 0

    # map to keep count of (char_a, char_b) pairs before position c
    pair_count = defaultdict(int)
    # 
#wverealjagsegi
    for c in range(1, n):
        for d in range(c + 1, n):
            # x[a] == x[c] and x[b] == x[d]
            char_c = x[c]
            char_d = x[d]
            count += pair_count[(char_c, char_d)]

        # Update pair_count with all (a, b) pairs where b == c
        for a in range(c):
            pair_count[(x[a], x[c])] += 1

    return count

