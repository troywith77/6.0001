# 年薪
annual_salary = float(input('The starting annual salary: '))
# 每个月投资比例
portion_saved = float(input('The portion of salary to be saved: '))
# 总房款
total_cost = float(input('The cost of your dream home: '))
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
month = 0

while (current_savings < down_payment):
    current_savings += current_savings * (r / 12)
    # 加上每个月新投资的钱
    current_savings += monthly_money
    month += 1

print('Number of months:', month)
