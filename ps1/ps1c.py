# 初始年薪
annual_salary = float(input('The starting annual salary: '))
# 每个月投资比例
# portion_saved = 0.4411
# 总房款
total_cost = 1000000
# 半年涨薪比例
semi_annual_raise = 0.07
# 首付比例
portion_down_payment = 0.25

# 投资利率
r = 0.04
# 首付总额
down_payment = total_cost * portion_down_payment

min_rate = 0
max_rate = 10000

steps = 0

found_rate = False

while (not found_rate):
    portion_saved = (min_rate + max_rate) / 2 / 10000
    temp_annual_salary = annual_salary
    # 月薪
    monthly_salary = temp_annual_salary / 12
    # 每个月投资金额
    monthly_money = monthly_salary * portion_saved
    # 月数
    month = 1
    # 当前存款
    current_savings = 0.0
    steps += 1
    while (month <= 36):

        current_savings += current_savings * (r / 12)
        # 加上每个月新投资的钱
        current_savings += monthly_money

        # 每6个月后涨薪
        if (month % 6 == 0):
            temp_annual_salary *= (1 + semi_annual_raise)
            monthly_salary = temp_annual_salary / 12
            monthly_money = monthly_salary * portion_saved

        if (current_savings >= down_payment):
            break

        month += 1

    # print('Number of months:', month)
    # print('current_savings:', current_savings)

    if (abs(current_savings - down_payment) <= 100):
        print('YES!', portion_saved, steps)
        print('Best savings rate:', int(portion_saved * 10000) / 10000)
        print('Steps in bisection search:', steps)
        break
        found_rate = True
    else:
        if (portion_saved == 1.0):
            print('It is not possible to pay the down payment in three years.')
            break
        if (current_savings > down_payment):
            max_rate = portion_saved * 10000
        else:
            min_rate = portion_saved * 10000
