

def solution(msg):
    answer = []
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    nums = list(range(1, 27))

    dic = dict(zip(chars, nums))

    while msg:
        w = ''

        for length in range(len(msg), 0, -1):
            if msg[:length] in dic:
                w = msg[:length]
                break

        answer.append(dic[w])

        if len(w) < len(msg):
            c = msg[len(w)]
            dic[w + c] = len(dic) + 1

        msg = msg[len(w):]

    return answer

    

