def solution(keymap, targets):
    result = []  # 결과를 저장할 리스트

    alp_key = dict()  # 각 문자에 대한 키 정보를 저장할 딕셔너리

    # keymap을 순회하면서 각 문자가 어떤 키에서 어떤 순서로 나오는지 기록
    for row in keymap:
        for idx, alp in enumerate(row):
            
            # 이미 해당 문자가 기록되어 있고, 현재 키보다 나중에 나오는 경우 스킵
            if (alp in alp_key) and (idx+1) > alp_key[alp]:
                continue

            # 문자와 해당 키의 순서를 딕셔너리에 저장
            alp_key[alp] = idx + 1

    # targets를 순회하면서 각 문자열을 만들기 위해 필요한 키 누름 횟수 계산
    for row in targets:
        total_index = 0  # 문자열을 만들기 위한 총 키 누름 횟수

        for alp in row:
            
            # 문자가 딕셔너리에 있으면 해당 키의 순서를 더함
            if alp in alp_key:
                total_index += alp_key[alp]
                
            # 문자가 딕셔너리에 없으면 해당 문자열을 만들 수 없으므로 -1로 설정하고 루프 종료
            else:
                total_index = -1
                break

        # 결과 리스트에 각 문자열을 만들기 위한 키 누름 횟수 추가
        result.append(total_index)

    return result  # 결과 반환