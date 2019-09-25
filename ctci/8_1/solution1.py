MEMO = {}

def ways_to_jump_up_n_stairs(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    elif n in MEMO:
        return MEMO[n]
    else:
        num_ways = ways_to_jump_up_n_stairs(n-1) + ways_to_jump_up_n_stairs(n-2) + ways_to_jump_up_n_stairs(n-3)
        MEMO[n] = num_ways
        return num_ways

if __name__ == "__main__":
    print(ways_to_jump_up_n_stairs(1))
    print(ways_to_jump_up_n_stairs(10))
    print(ways_to_jump_up_n_stairs(100))
    print(ways_to_jump_up_n_stairs(1000))
