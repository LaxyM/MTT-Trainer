
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
input_string = "AA,KK,QQ,JJ,TT,99,88,77,66,55,44,33:0.0675,AK,AQ,AJ,AT,A9,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJ,KT,K9s,K8s,K7s,K6s,K5s:0.962,QJs,QJo:0.602,QTs,QTo:0.4537,Q9s,Q8s,JTs,JTo:0.623,J9s,J8s,T9s,T8s,T7s:0.5725,98s,97s,87s,86s:0.4472,76s,65s,54s:0.2252"

# Форматирование весов в нужный формат
formatted_weights = format_weights(input_string)
print(formatted_weights)


