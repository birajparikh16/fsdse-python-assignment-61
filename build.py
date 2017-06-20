def solution(list_of_nums):
    dic = {"ODD":0,"EVEN":0}
    for x in list_of_nums:
        if x%2==0:
            dic["EVEN"]+=1
        else:
            dic["ODD"]+=1
    return dic
