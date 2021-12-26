def sqString(givStr):
    lenOfsides = round(len(givStr) / 4)
    topStr = givStr[:lenOfsides]
    botStr = givStr[lenOfsides*3:]

    midstring1 = givStr[lenOfsides:lenOfsides * 2]
    midstring2 = givStr[lenOfsides * 2:lenOfsides * 3]
    newMS1 = ''
    newTop = ''
    newBot = ''
    for i in midstring1:
        newMS1 += i + ' '
    for j in topStr:
        newTop += j + ' '
    for k in botStr:
        newBot += k + ' '

    print(newTop)
    for i in range(len(midstring1)):
        print(str(midstring1[i]) + ' ' * (len(newMS1) - 3) + str(midstring2[i]))
    print(newBot)


sqString('thiscodewillprintoutasquarewiththisgivenstringofletters.')

