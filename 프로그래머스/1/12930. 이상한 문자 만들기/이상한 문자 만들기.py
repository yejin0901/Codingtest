def solution(s):
    result = []
    word = s.split(" ")

    for i in word:
        new_word=""
        for idx, alp in enumerate(i):
            if idx % 2==0:
                new_word+=alp.upper()
            else:
                new_word += alp.lower()


        result.append(new_word)
    return " ".join(result)