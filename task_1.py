#Напишите программу, удаляющую из текста все слова содержащие "абв". 
#Используйте знания с последней лекции. Выполните ее в виде функции. 


def deletABW(text:str):
    bufList = text.split()
    fragment = 'абв'
    newList = [bufList[i] for i in range(len(bufList)) if fragment not in bufList[i]]
    return newList




textU = 'абв оплджу вып влп ыпабв алвдыабвпвл лжпппж'
new = deletABW(textU)
print(new)