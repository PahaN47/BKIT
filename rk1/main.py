from computer import computer
from microprocessor import microprocessor
from cmlink import cmlink

computers = [
    computer("Computer Sergey"),
    computer("Amazing Computer 3000"),
    computer("The Box")
]

microprocessors = [
    microprocessor("intel core i3", 10000, computers[0].getid()),
    microprocessor("intel core i5", 15000, computers[1].getid()),
    microprocessor("intel core i7", 30000, computers[2].getid()),
    microprocessor("intel xeon", 600000, computers[2].getid())
]


# список для третьего задания. связи в первых двух заданиях отличаются
# и никак не связаны с третьим заданием. 
# в третьем задании поле id микропроцессора игнорируется
cmlinks = [
    cmlink(computers[0].getid(), microprocessors[0].getid()),
    cmlink(computers[1].getid(), microprocessors[0].getid()),
    cmlink(computers[1].getid(), microprocessors[1].getid()),
    cmlink(computers[2].getid(), microprocessors[0].getid()),
    cmlink(computers[2].getid(), microprocessors[1].getid()),
    cmlink(computers[2].getid(), microprocessors[2].getid()),
    cmlink(computers[2].getid(), microprocessors[3].getid())
]

def main():
    dict12_base = {
        comp : [mp for mp in microprocessors if mp.comp_id == comp.getid()]
        for comp in computers 
    }
# задание 1: вывести список всех компьютеров, название которых начинается с 'A',
# и список всех микропроцессоров в них
    print("TASK 1:")
    for comp in dict12_base.keys():
        if (comp.name.lower()[0] == 'a'):
            print(comp.name, ':', [mp.name for mp in dict12_base[comp]])
# задание 2: вывести список компьютеров и максимальную стоимость микропроцессора
# в каждом компьютере, отсортированный по убыванию стоимости
    print("\nTASK 2:")
    dict2 = {
        comp : max([mp.price for mp in dict12_base[comp]])
        for comp in dict12_base.keys()
    }
    dict2 = sorted(dict2.items(), key= lambda x : x[1], reverse= True)
    for item in dict2:
        print(item[0].name, " : ", item[1])
# задание 3: вывести список всех связанных пар компьютеров и микропроцессоров,
# отсортированный по компьютерам
    print("\nTASK 3:")
    list3 = [
        (computers[cmlink.comp_id].name, microprocessors[cmlink.mp_id].name)
        for cmlink in cmlinks
        ]
    for names in list3:
        print(names[0], " : ", names[1])

if __name__ == "__main__":
    main()
    
