def solution(data, n):
    from collections import Counter

    occurrences = Counter()
    
    for id in data:
        occurrences[id] += 1

    return list(filter(lambda id: occurrences[id] <= n, data))

if __name__ == '__main__':
    print(solution([5, 10, 15, 10, 7], 1))
    print(solution([1, 2, 3], 0))
    print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
