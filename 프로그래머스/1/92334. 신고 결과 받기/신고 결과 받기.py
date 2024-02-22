def solution(id_list, report, k):

    
    user_list = {id:{"report":set(),"mail":0} for id in id_list}
    
    for r in report:
        r = r.split(" ")
        user_list[r[1]]["report"].add(r[0])
        
    for key in user_list:
        if(len(user_list[key]["report"])>=k):
            for user in user_list[key]["report"]:
                user_list[user]["mail"] +=1
                
    mail_num = [value["mail"] for value in user_list.values()]
    
    return mail_num