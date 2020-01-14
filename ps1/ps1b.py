# 年薪
annual_salary = float(input('The starting annual salary: '))
# 每个月投资比例
portion_saved = float(input('The portion of salary to be saved: '))
# 总房款
total_cost = float(input('The cost of your dream home: '))
# 半年涨薪比例
semi_annual_raise = float(input('The semi­annual salary raise: '))
# 月薪
monthly_salary = annual_salary / 12
# 首付比例
portion_down_payment = 0.25
# 当前存款
current_savings = 0.0
# 投资利率
r = 0.04

# 首付总额
down_payment = total_cost * portion_down_payment

# 每个月投资金额
monthly_money = monthly_salary * portion_saved

# 月数
month = 1

while (True):
    current_savings += current_savings * (r / 12)
    # 加上每个月新投资的钱
    current_savings += monthly_money

    # 每6个月后涨薪
    if (month % 6 == 0):
        annual_salary *= (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        monthly_money = monthly_salary * portion_saved

    if (current_savings >= down_payment):
        break

    month += 1

print('Number of months:', month)
