def round_to_nearest_five(num):
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

#     # Форматирование весов в нужный формат
#     formatted_weights = format_weights(input_string)
#     print(formatted_weights)
