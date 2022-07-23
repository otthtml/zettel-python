def solution(S):
    maxi = -1
    for i in range(len(S) - 1):
        digram = S[i] + S[i+1]
        furthest = S.rfind(digram)
        if i != furthest:
            if furthest - i > maxi:
                maxi = furthest - i

    return maxi