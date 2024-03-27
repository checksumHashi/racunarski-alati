# У једном сеоцету у срцу Шумадије живела је шармантна девојчица по имену Спасенија...

def plazma() -> int:
    n, t = [int(x) for x in input().split()]

    dicti = {}

    for x in range(0, n):
        a, b = [int(x) for x in input().split()]
        dicti.update({a: b})

    # dan na koji je prvi put kupljena coko plazma
    first_buy_at = min(dicti.keys())

    # broj coko plazme koja je kupljena prvi put
    current_sum = dicti[first_buy_at]

    # brojac dana tokom kojih je Spasenija jela plazmu
    successfull_days = 0

    # trenutan dan
    current_day = 1

    for x in range(1, t):
        
        try:
            addon = dicti[current_day]
            current_sum += addon
        except:
            continue
        current_day += 1

#print(current_sum)
#print(dicti)