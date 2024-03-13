if len(nums) == k:
            return sum(nums) / k
        cutoff_from = 0
        cut_until = k
        solution_sum = sum(nums[cutoff_from:k])
        while cut_until < len(nums):
            temp_sum = (solution_sum - nums[cutoff_from]) + nums[cut_until]
            print(nums[cutoff_from])
            print(nums[cut_until])
            print(temp_sum)
            print(cutoff_from)
            print(cut_until)
            if temp_sum > solution_sum:
                solution_sum = temp_sum
            cutoff_from += 1
            cut_until += 1
        return solution_sum / k
