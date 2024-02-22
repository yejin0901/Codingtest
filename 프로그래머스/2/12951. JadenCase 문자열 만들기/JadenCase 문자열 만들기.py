def solution(s):
    answer = []
    s_list = s.split(" ")
    for i in s_list:
        if i != "":
            answer.append(i[0].upper() + i[1:].lower())
        else:
            answer.append("")
    return " ".join(answer)