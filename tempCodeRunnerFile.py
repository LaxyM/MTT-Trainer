
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

# # Пример данных
# input_string = "AA,KK,QQ,JJ,TT,99,88,77,66,55,44:0.5203,33:0.001,AK,AQ,AJ,AT,A9s,A9o:0.2877,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJs,KJo:0.8854,KTs,KTo:0.6262,K9s,K8s,K7s:0.498,K6s:0.9996,QJs,QJo:0.1013,QTs,QTo:0.2549,Q9s,JTs,JTo:0.2065,J9s,J8s:0.6406,T9s,T8s,98s,97s:0.4166,87s,76s:0.9983,65s:0.7493"

# # Форматирование весов в нужный формат
# formatted_weights = format_weights(input_string)
# print(formatted_weights)