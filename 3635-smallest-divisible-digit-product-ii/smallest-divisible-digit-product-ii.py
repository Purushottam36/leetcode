class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # 1. Count the required prime factors of t
        target = {2: 0, 3: 0, 5: 0, 7: 0}
        temp = t
        primes = [2, 3, 5, 7]
        
        for p in primes:
            while temp % p == 0:
                target[p] += 1
                temp //= p
        
        # If t contains any prime factors other than 2, 3, 5, or 7, it's impossible
        if temp > 1:
            return "-1"

        # Map each digit from 1-9 to its prime factor contributions
        digit_factors = {
            1: {2: 0, 3: 0, 5: 0, 7: 0},
            2: {2: 1, 3: 0, 5: 0, 7: 0},
            3: {2: 0, 3: 1, 5: 0, 7: 0},
            4: {2: 2, 3: 0, 5: 0, 7: 0},
            5: {2: 0, 3: 0, 5: 1, 7: 0},
            6: {2: 1, 3: 1, 5: 0, 7: 0},
            7: {2: 0, 3: 0, 5: 0, 7: 1},
            8: {2: 3, 3: 0, 5: 0, 7: 0},
            9: {2: 0, 3: 2, 5: 0, 7: 0}
        }

        def get_min_suffix_needed(req_2, req_3, req_5, req_7) -> str:
            """Greedily constructs the minimal sorted string of digits needed 
            to satisfy the remaining prime factor requirements."""
            n2, n3, n5, n7 = max(0, req_2), max(0, req_3), max(0, req_5), max(0, req_7)
            suffix = []

            # 7 and 5 can only be satisfied by digits 7 and 5
            suffix.extend(['7'] * n7)
            suffix.extend(['5'] * n5)

            # Combine 3s into 9s and 2s into 8s
            suffix.extend(['9'] * (n3 // 2))
            n3 %= 2
            suffix.extend(['8'] * (n2 // 3))
            n2 %= 3

            # Handle remaining combinations of 2s and 3s
            if n3 == 1 and n2 == 1:
                suffix.append('6')
            elif n3 == 1 and n2 == 2:
                suffix.extend(['6', '2'])
            elif n3 == 1:
                suffix.append('3')
            elif n2 == 2:
                suffix.append('4')
            elif n2 == 1:
                suffix.append('2')

            suffix.sort()
            return "".join(suffix)

        n = len(num)
        
        # 2. Build prefix factor counts
        # pref[i] stores the accumulated prime factors for num[0...i-1]
        pref = [{2: 0, 3: 0, 5: 0, 7: 0} for _ in range(n + 1)]
        first_zero_idx = -1

        for i in range(n):
            pref[i + 1] = pref[i].copy()
            if num[i] == '0':
                if first_zero_idx == -1:
                    first_zero_idx = i
            else:
                f = digit_factors[int(num[i])]
                for p in primes:
                    pref[i + 1][p] += f[p]

        # Case 1: Check if num itself is valid (contains no 0s and fulfills t)
        if first_zero_idx == -1 and all(pref[n][p] >= target[p] for p in primes):
            return num

        # Case 2: Greedy backtracking
        # If there's a 0, we cannot keep any prefix that contains or goes past that 0
        start_idx = first_zero_idx if first_zero_idx != -1 else n - 1

        for i in range(start_idx, -1, -1):
            curr_digit = int(num[i])
            # Try to increment the current digit
            for d in range(curr_digit + 1, 10):
                current_f = pref[i]
                d_f = digit_factors[d]

                # Remaining factors needed from the suffix
                req_2 = target[2] - current_f[2] - d_f[2]
                req_3 = target[3] - current_f[3] - d_f[3]
                req_5 = target[5] - current_f[5] - d_f[5]
                req_7 = target[7] - current_f[7] - d_f[7]

                min_suffix = get_min_suffix_needed(req_2, req_3, req_5, req_7)
                rem_len = n - 1 - i

                # If the required digits fit in the remaining space
                if len(min_suffix) <= rem_len:
                    pad_ones = rem_len - len(min_suffix)
                    return num[:i] + str(d) + ('1' * pad_ones) + min_suffix

        # Case 3: If no number of the same length works, expand the length
        min_suffix = get_min_suffix_needed(target[2], target[3], target[5], target[7])
        target_len = max(n + 1, len(min_suffix))
        pad_ones = target_len - len(min_suffix)
        return ('1' * pad_ones) + min_suffix