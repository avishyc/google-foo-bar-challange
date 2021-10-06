def solution(l):
    from itertools import permutations
    from functools import reduce

    for length in range(len(l), 0, -1):
        nums = [reduce(lambda x, y: 10 * x + y, p) for p in permutations(l, length)]
        nums.sort(reverse=True)
        for num in nums:
            if num % 3 == 0:
                return num

    return 0


if __name__ == '__main__':
    print(solution([3,1,4,1]))
    print(solution([3,1,4,1,5,9]))