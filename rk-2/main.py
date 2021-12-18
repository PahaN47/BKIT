from computer import computer
from microprocessor import microprocessor
from cmlink import cmlink




# задание 1: вывести список всех компьютеров, название которых начинается с 'A',
# и список всех микропроцессоров в них
def task1(computers, microprocessors):
    dict_base = {
        comp : [mp for mp in microprocessors if mp.comp_id == comp.getid()]
        for comp in computers 
    }
    result = {}
    for comp in dict_base.keys():
        if (comp.name.lower()[0] == 'a'):
            result[comp.name] = [mp.name for mp in dict_base[comp]]
    return result

# задание 2: вывести список компьютеров и максимальную стоимость микропроцессора
# в каждом компьютере, отсортированный по убыванию стоимости
def task2(computers, microprocessors):
    dict_base = {
        comp : [mp for mp in microprocessors if mp.comp_id == comp.getid()]
        for comp in computers 
    }
    result = {
        comp.name : max([mp.price for mp in dict_base[comp]])
        for comp in dict_base.keys()
    }
    result = sorted(result.items(), key= lambda x : x[1], reverse= True)
    return result

# задание 3: вывести список всех связанных пар компьютеров и микропроцессоров,
# отсортированный по компьютерам
def task3(computers, microprocessors, cmlinks):
    pairlist = [
        (computers[cmlink.comp_id].name, microprocessors[cmlink.mp_id].name)
        for cmlink in cmlinks
        ]
    return pairlist
