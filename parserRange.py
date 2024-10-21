
#! PIOSOLVER
def round_to_nearest_five(num):
    # Округляем до ближайшего 0.05
    return round(num * 20) / 20

def format_weights(input_string):
    # Разделяем входные данные по запятой
    hand_entries = input_string.split(',')
    result = []

    for entry in hand_entries:
        # Если есть двоеточие, значит, это запись с весом
        if ':' in entry:
            hands, weight = entry.split(':')
            weight_value = float(weight)

            if weight_value > 0.95:
                # Если вес больше 0.95, добавляем руку без веса
                result.append(hands)
            else:
                # Округляем вес и формируем строку
                rounded_weight = round_to_nearest_five(weight_value)
                result.append(f'{hands}:{rounded_weight:.2f}')
        else:
            # Если записи без веса, просто добавляем их
            result.append(entry)

    # Объединяем результаты в одну строку без пробелов
    return ','.join(result)

# Пример данных
input_string = "AA,KK,QQ,JJ:0.624972,TT:0.332176,99:0.0842844,88:0.0597551,AKs,AKo:0.877067,AQo:0.361647,AJo:0.127448,ATo:0.526105,A5o:0.26852,A4o:0.268013,KJs:0.00775974,KJo:0.587195,KTs:0.42508,KTo:0.10798,K9s:0.125902,K9o:0.00935129,K6s:0.358119,QJs:0.237162,QJo:0.0753459,JTs:0.328224,J9s:0.207775,J8s:0.0414203,T9s:0.0287582,T9o:0.0192664,87s:0.144214,76s:0.232018,65s:0.353789,64s:0.055604,54s:0.213869"

# Форматирование весов в нужный формат
formatted_weights = format_weights(input_string)
print(formatted_weights)




