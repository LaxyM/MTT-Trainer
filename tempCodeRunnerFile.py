#! PIOSOLVER
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
# input_string = "QQ:0.107863,JJ:0.353081,TT:0.501532,99:0.656747,88:0.695092,77:0.740659,66:0.292116,55:0.302414,44:0.106144,AKo:0.271471,AQs,AQo:0.0751733,AJs:0.922095,ATs:0.521194,A9s:0.440367,A8s:0.0296234,A5s:0.368309,A4s:0.190291,KQs:0.959782,KJs:0.152245,KTs:0.300547,QJs:0.471156,QTs:0.534402,JTs:0.698996,T9s:0.154463,65s:0.0925641,54s:0.0341512"

# # Форматирование весов в нужный формат
# formatted_weights = format_weights(input_string)
# print(formatted_weights)