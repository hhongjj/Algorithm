# G5 17214 다항 함수의 적분
# https://www.acmicpc.net/problem/17214
# 수학, 문자열, 피싱, 미적분학
# x인경우 해결 못함.

poly = input().split('x')


# poly = input()
# if '+' in poly:
#     poly = poly.split('+')
# elif '-' in poly:
#     if poly[0] == '-':
#         poly = poly.split('-')
#         if len(poly) == 3:
#             poly[0] = '-' + poly[1]
#             poly[1] = '-' + poly[2]
#             poly.pop()
#         else:
#             poly[0] = '-' + poly[1]
#             poly.pop()
#     else:
#         poly = poly.split('-')
#         poly[1] = '-' + poly[1]
# else:
#     temp = poly
#     poly = list()
#     poly.append(temp)
#
# result = ''
# for p in range(len(poly)):
#     if poly[p] == 'x':
#         if len(result):
#             result += '+'
#         result += '1/2xx'
#     elif poly[p] == '-x':
#         if len(result):
#             result += '+'
#         result += '-1/2xx'
#     elif poly[p][-1] == 'x':
#         num = ''
#         if poly[p][0] == '-':
#             result += '-'
#             for i in range(1, len(poly[p])-1):
#                 num += poly[p][i]
#             num = int(num) // 2
#             result += str(num) + 'xx'
#         else:
#             if len(result):
#                 result += '+'
#             for i in range(len(poly[p])-1):
#                 num += poly[p][i]
#             num = int(num) // 2
#             result += str(num) + 'xx'
#
#     else:
#         if poly[p][0] == '-':
#             result += poly[p] + 'x'
#         else:
#             if len(result):
#                 result += '+'
#             result += poly[p] + 'x'
#
#
# result += '+W'
# print(result)