# Дат Вам је низ која садржи само бројеве 0,1 и 2. 
# Ви на сте на позицији 1, а Ваши непријатељи су на позицијама 2. 
# Потребно је израчунати растојање до Вашег најближег непријатеља како бисте дошли до њега. 
# Можете ићи лево и десно. Такође, уколико се налазите на ивици низа, 
# и уколико се померите у правцу те ивице, појавићете се на пољу на супротној страни тог низа.
# Низ садржи произвољан број 0 и 2, али је само једна 1 у њему, 
# такође и не мора садржати број 2, тада би требало вратити 0.

# resenje uzima 103 (maksimum) poena

# isto kao i "def func(s):", pogledaj "python type checking" za objasnjenje
def func(length:int, cords: list) -> int:
    if length == 1: return 0
    
    left = right = cords.index(1)
    count = 1
    while True:
        left -= 1
        right += 1
        if left < 0: left = length - 1
        if right > length - 1: right = 0
        if cords[left] == 2:
            return count
        if cords[right] == 2:
            return count
        count += 1
    return


# ulaz
length = int(input())
cords = [int(digit) for digit in input()]
print(func(length, cords))


# test slucajevi

#print("one: ", func(5, [2,0,0,1,0]))
#print("two: ", func(3, [1,0,2]))
#print("three: ", func(10, [0,2,0,0,2,0,0,1,0,0]))