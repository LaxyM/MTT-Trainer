
# #! PIOSOLVER
# def round_to_nearest_five(num):
#     # Округляем до ближайшего 0.05
#     return round(num * 20) / 20

# def format_weights(input_string):
#     # Разделяем входные данные по запятой
#     hand_entries = input_string.split(',')
#     result = []

#     for entry in hand_entries:
#         # Если есть двоеточие, значит, это запись с весом
#         if ':' in entry:
#             hands, weight = entry.split(':')
#             weight_value = float(weight)

#             if weight_value > 0.95:
#                 # Если вес больше 0.95, добавляем руку без веса
#                 result.append(hands)
#             else:
#                 # Округляем вес и формируем строку
#                 rounded_weight = round_to_nearest_five(weight_value)
#                 result.append(f'{hands}:{rounded_weight:.2f}')
#         else:
#             # Если записи без веса, просто добавляем их
#             result.append(entry)

#     # Объединяем результаты в одну строку без пробелов
#     return ','.join(result)




# def format_weights(input_string):
#     # Разделяем входную строку на отдельные записи
#     entries = input_string.split(', ')

#     # Создаём словарь для хранения весов
#     weights = {}

#     # Обрабатываем каждую запись
#     for entry in entries:
#         # Если запись содержит вес, то извлекаем его
#         if '[' in entry and ']' in entry:
#             weight = float(entry[entry.index('[') + 1:entry.index(']')])
#             hands = entry[entry.index(']') + 1:].strip()
#             weights[hands] = weight
#         else:
#             # Если запись не содержит вес, то добавляем её в словарь с весом 0
#             weights[entry] = 0

#     # Форматируем веса
#     formatted_weights = []
#     for hands, weight in weights.items():
#         if weight > 0.95:
#             formatted_weights.append(hands)
#         else:
#             rounded_weight = round(weight * 20) / 20
#             formatted_weights.append(f'{hands}:{rounded_weight:.2f}')

#     # Объединяем результаты в одну строку
#     return ', '.join(formatted_weights)


# # Пример данных
# input_string = "AA,KK,QQ,JJ,TT,99,88,77,66,55,44:0.5203,33:0.001,AK,AQ,AJ,AT,A9s,A9o:0.2877,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJs,KJo:0.8854,KTs,KTo:0.6262,K9s,K8s,K7s:0.498,K6s:0.9996,QJs,QJo:0.1013,QTs,QTo:0.2549,Q9s,JTs,JTo:0.2065,J9s,J8s:0.6406,T9s,T8s,98s,97s:0.4166,87s,76s:0.9983,65s:0.7493"

# # Форматирование весов в нужный формат
# formatted_weights = format_weights(input_string)
# print(formatted_weights)


def format_weights(input_string):
    # Split the input string into individual entries
    entries = input_string.split(', ')

    # Create a dictionary to store the weights
    weights = {}

    # Process each entry
    for entry in entries:
        # Check if the entry contains a weight
        if '[' in entry and ']' in entry:
            start_index = entry.index('[') + 1
            end_index = entry.index(']')
            weight_str = entry[start_index:end_index].strip()
            if weight_str:
                weight = float(weight_str.replace('/', ''))
                hands = entry[end_index+1:].strip()
                weights[hands] = weight
        else:
            # If the entry doesn't contain a weight, add it to the dictionary with a weight of 0
            weights[entry] = 0

    # Format the weights
    formatted_weights = []
    for hands, weight in weights.items():
        if weight > 0.95:
            formatted_weights.append(hands)
        else:
            rounded_weight = round(weight * 20) / 20
            formatted_weights.append(f'{hands}:{rounded_weight:.2f}')

    # Combine the results into a single string
    return ', '.join(formatted_weights)


input_string = '[0.34]6d6h, 6s6h, 6c6h, 6s6d, 6c6d, 6c6s[/0.34], [4.44]Jh9h, Jd9d, Js9s, Jc9c[/4.44], [7.90]Jh8h, Jd8d, Js8s, Jc8c[/7.90], [8.31]QhTh, QdTd, QsTs, QcTc[/8.31], [8.60]KdQh, KsQh, KcQh, KhQd, KsQd, KcQd, KhQs, KdQs, KcQs, KhQc, KdQc, KsQc[/8.60], [9.45]Ah3h, Ad3d, As3s, Ac3c[/9.45], [9.73]Ah2h, Ad2d, As2s, Ac2c[/9.73], [11.36]QhJh, QdJd, QsJs, QcJc[/11.36], [11.38]QdTh, QsTh, QcTh, QhTd, QsTd, QcTd, QhTs, QdTs, QcTs, QhTc, QdTc, QsTc[/11.38], [11.82]6h5h, 6d5d, 6s5s, 6c5c[/11.82], [12.04]9h8h, 9d8d, 9s8s, 9c8c[/12.04], [12.21]Ad9h, As9h, Ac9h, Ah9d, As9d, Ac9d, Ah9s, Ad9s, Ac9s, Ah9c, Ad9c, As9c[/12.21], [12.53]Ah4h, Ad4d, As4s, Ac4c[/12.53], [12.74]7d7h, 7s7h, 7c7h, 7s7d, 7c7d, 7c7s[/12.74], [13.73]Kh8h, Kd8d, Ks8s, Kc8c[/13.73], [13.78]8h7h, 8d7d, 8s7s, 8c7c[/13.78], [15.56]Ah6h, Ad6d, As6s, Ac6c[/15.56], [15.78]AhJh, AdJd, AsJs, AcJc[/15.78], [17.92]7h6h, 7d6d, 7s6s, 7c6c[/17.92], [18.44]Qh9h, Qd9d, Qs9s, Qc9c[/18.44], [20.05]Ah5h, Ad5d, As5s, Ac5c[/20.05], [22.60]Th8h, Td8d, Ts8s, Tc8c, TdTh, TsTh, TcTh, TsTd, TcTd, TcTs[/22.60], [23.67]KhTh, KdTd, KsTs, KcTc[/23.67], [23.71]Ah7h, Ad7d, As7s, Ac7c[/23.71], [25.13]AdJh, AsJh, AcJh, AhJd, AsJd, AcJd, AhJs, AdJs, AcJs, AhJc, AdJc, AsJc[/25.13], [27.84]KdTh, KsTh, KcTh, KhTd, KsTd, KcTd, KhTs, KdTs, KcTs, KhTc, KdTc, KsTc[/27.84], [28.78]Th9h, Td9d, Ts9s, Tc9c[/28.78], [29.31]KdJh, KsJh, KcJh, KhJd, KsJd, KcJd, KhJs, KdJs, KcJs, KhJc, KdJc, KsJc[/29.31], [29.60]8d8h, 8s8h, 8c8h, 8s8d, 8c8d, 8c8s[/29.60], [31.16]JhTh, JdTd, JsTs, JcTc[/31.16], [37.38]5h4h, 5d4d, 5s4s, 5c4c[/37.38], [38.66]JdJh, JsJh, JcJh, JsJd, JcJd, JcJs[/38.66], [39.44]KhJh, KdJd, KsJs, KcJc[/39.44], [40.27]Ah9h, Ad9d, As9s, Ac9c[/40.27], [40.98]9d9h, 9s9h, 9c9h, 9s9d, 9c9d, 9c9s[/40.98], [43.26]AdTh, AsTh, AcTh, AhTd, AsTd, AcTd, AhTs, AdTs, AcTs, AhTc, AdTc, AsTc[/43.26], [52.18]Kh9h, Kd9d, Ks9s, Kc9c[/52.18], [53.69]AdQh, AsQh, AcQh, AhQd, AsQd, AcQd, AhQs, AdQs, AcQs, AhQc, AdQc, AsQc[/53.69], [61.97]AdKh, AsKh, AcKh, AhKd, AsKd, AcKd, AhKs, AdKs, AcKs, AhKc, AdKc, AsKc[/61.97], [62.83]Ah8h, Ad8d, As8s, Ac8c[/62.83], [84.46]QdQh, QsQh, QcQh, QsQd, QcQd, QcQs[/84.46], KdKh, KsKh, KcKh, AhKh, KsKd, KcKd, AdKd, KcKs, AsKs, AcKc, AdAh, AsAh, AcAh, AsAd, AcAd, AcAs'

formatted_weights = format_weights(input_string)
print(formatted_weights)