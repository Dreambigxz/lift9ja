def percentage_calculator(percent, amount):

    return percent*amount/100

target_amount = 780000
remaining = 780000

# a = (percentage_calculator(2, remaining))
daily_percent = 30
count = 0
days = 0
#
# while count < target_amount:
#
#     print('new amount', remaining, 'percent', daily_percent)
#
#     percent = percentage_calculator(daily_percent, remaining)
#
#     print('percent', percent)
#
#     count += percent
#     remaining -= percent
#
#     days += 1
#
#     if count > target_amount:
#         #reap completed
#         count = target_amount
#         print('hy')
#
#     print('reap',remaining, 'count', count,'days:',days)
#
#     # break
#
# else:
#     print(False)

print(percentage_calculator(5, 400))

