def length_of_railway(sounds):
    start = False
    an = '呜呜'
    fahrt = "哐当"
    distance = 0
    i = 0
    while i < len(sounds):
        check = sounds[i:i+2]
        if check == fahrt and start == True:
            distance += 20
            i+=2
        elif check == fahrt and start == False:
            distance += 10
            i+=2
        elif check == an:
            start = not start
            i+=3
        else:
            i+=1
    return distance


#print(length_of_railway('呜呜呜哐当哐当面包饮料矿泉水了啊，哐当桶面火腿肠茶叶蛋了啊哐当哐当呜呜呜哐当哐当哐当北京站到了，下车的旅客请带好您的行李，准备下车哐当哐当'))
#print(length_of_railway('哐当哐当哐当哐当哐当哐当'))
print(length_of_railway('哐当哐当哐当哐当服哐当哐当'))
#print(length_of_railway('呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当'))
#print(length_of_railway('呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当'))
