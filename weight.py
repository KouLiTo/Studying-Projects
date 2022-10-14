print("""РАССЧЕТ ИДЕАЛЬНОГО ВЕСА
         ДЛЯ ЗАВЕРШЕНИЯ ПРОГРАММЫ ВВЕДИТЕ "OFF" ВМЕСТО ИМЕНИ """)


def type_number():
    num = input("ВВЕДИТЕ ЗДЕСЬ: ")
    if num == "off":
        return num
    elif not num.isdigit():
        print("Ви маєте ввести тільки числове значення")
        return type_number()
    else:
        num = float(num)
        return num

def sex():
    s = input("ВВЕДИТЕ ВАШ ПОЛ В ФОРМАТЕ М/Ж: ").upper()
    if (s == "М") or (s == "Ж"):
        return s
    else:
        print("ПОВТОРИТЕ ПОПЫТКУ! ВВЕДИТЕ ТОЛЬКО ОДНУ БУКВУ - М или Ж")
        return sex()

def weight_index(name, sex, height, weight):
    match sex:
        case "М":
            ideal_weight = round(((height / 100) ** 2) * 21.745 + 2.2, 3)
            print(f"{name}, ВАШ ИДЕАЛЬНЫЙ ВЕС ДОЛЖЕН БЫТЬ {ideal_weight} КГ")
            if weight == ideal_weight:
                print("У ВАС ИДЕАЛЬНЫЙ ВЕС")
            elif weight < ideal_weight:
                print(f"ВАШ ВЕС МЕНЬШЕ ИДЕАЛЬНОГО ДЛЯ ВАС ВЕСА НА {round(ideal_weight - weight, 3)} КГ")
            else:
                print(f"ВАШ ВЕС БОЛЬШЕ ИДЕАЛЬНОГО ДЛЯ ВАС ВЕСА НА {round(weight - ideal_weight, 3)} КГ")
        case _:
            ideal_weight = round(((height / 100) ** 2) * 21.745 - 2.2, 3)
            print(f"{name}, ВАШ ИДЕАЛЬНЫЙ ВЕС ДОЛЖЕН БЫТЬ {ideal_weight} КГ")
            if weight == ideal_weight:
                print("У ВАС ИДЕАЛЬНЫЙ ВЕС")
            elif weight < ideal_weight:
                print(f"ВАШ ВЕС МЕНЬШЕ ИДЕАЛЬНОГО ДЛЯ ВАС ВЕСА НА {round(ideal_weight - weight, 3)} КГ")
            else:
                print(f"ВАШ ВЕС БОЛЬШЕ ИДЕАЛЬНОГО ДЛЯ ВАС ВЕСА НА {round(weight - ideal_weight, 3)} КГ")

res_ = True
while res_:
    print("""ДЛЯ ЗАВЕРШЕНИЯ ВВЕДИТЕ "OFF" ВМЕСТО ИМЕНИ""")
    name = input("ВВЕДИТЕ ВАШЕ ИМЯ: ").upper()
    if name == "OFF":
        print("ПРОГРАММА ЗАВЕРШЕНА")
        res_ = False
    else:
        sex = sex()
        print(f"{name}, НИЖЕ ВВЕДИТЕ ВАШ РОСТ В СМ:")
        height = type_number()
        print(f"{name}, НИЖЕ ВВЕДИТЕ ВАШ ВЕС В КГ")
        weight = type_number()
        weight_index(name, sex, height, weight)


