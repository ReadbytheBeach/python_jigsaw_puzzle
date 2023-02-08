# 购买三明治， 选择一系列的搭配方式
"""
1.输入选择：
    # 面包类型： opt_bread: 'wheet','white','sourdough'
    # 蛋白质要求: opt_type:  'chicken','turkey','ham','beef','tofu'
    # 要加cheese吗: yes/no
    # 如果要cheese, 选择类型opt_cheese: 'cheddar', 'Swiss','ozzarella'
    # 要加sauces吗: yes/no 
    # 如果要加saucesopt_sauces: 'mayo', 'mustard'
    # 要加蔬菜吗： yes/no:
    # 如果要加vegetable: opt_vegetable: 'lettuce', 'tomato'
    # 要几个三明治: sandw_number, (隐含最少选1个, 限量最多买5个)
    隐含：以上每种选择都必须选择其一
    隐含：以上每种选择都只能选一个
    隐含：不成功需要重新输入选择，直到做出正确选择
    隐含: 推出方式可以是时间, 等待10S
    隐含: pyip.Menu() 自动提示--'Please select one of the following:'
    隐含：但你做出选择后，打印出你所作的选择
    隐含: 当直接回车没有输入时, 自动提示--'Blank values are ot allowed'

    # ToDo:
    额外选择可以加钱嘛。。。

2.所需费用：
    # 列出每项价格
    # 显示总价

"""

import pyinputplus as pyip
import time

global_price = 0

while True:
    opt_bread = ['wheet','white','sourdough']
    opt_protein = ['chicken','turkey','ham','beef','tofu']
    opt_cheese = ['cheddar', 'swiss','ozzarella']
    opt_sauce = ['mayo', 'mustard']
    opt_vegetable = ['lettuce', 'tomato']

    price_bread = 0
    price_protein = 0
    price_cheese = 0
    price_sauce = 0.1
    price_vegetable = 0
    sandwich_price = 0

    chse_bread = pyip.inputMenu(opt_bread, timeout= 100)
    print('you choosed: ', chse_bread)
    time.sleep(0.5)  # 每次输出结果停顿0.5秒
    if chse_bread == 'white':
        price_bread = 1
        sandwich_price += price_bread
    # ToDo: 添加选择其他选项的价格

    chse_protein = pyip.inputMenu(opt_protein, timeout= 100)
    print('you choosed: ', chse_protein)
    time.sleep(0.8)
    if chse_protein == 'ham':
        price_protein = 2
        sandwich_price += price_protein
    # ToDo: 添加选择其他选项的价格

    cheeseYesNo_prompt = 'you want cheese? --yes/no: '
    yes_cheese = pyip.inputYesNo(prompt=cheeseYesNo_prompt)
    if yes_cheese == 'yes':
        chse_cheese = pyip.inputMenu(opt_cheese, timeout= 100)
        print('you choosed: ', opt_cheese)
        time.sleep(0.5)
        if chse_cheese == 'cheddar':
                price_cheese == 1
                sandwich_price += price_cheese
        # ToDo: 添加选择其他选项的价格
    else:
        print('You don\'t want cheese')
        # 没选不加钱

    sauceYesNo_prompt = 'you want sauce? --yes/no: '
    yes_sauce = pyip.inputYesNo(prompt=sauceYesNo_prompt)
    if yes_sauce == 'yes':
        chse_sauce = pyip.inputMenu(opt_sauce, timeout= 100)
        print('you choosed: ', chse_sauce)
        time.sleep(0.5)
        if chse_sauce == 'mustard':
                price_sauce == 0.5
                sandwich_price += price_sauce
        # ToDo: 添加选择其他选项的价格
    else:
        print('You don\'t want sauce')
        # 没选不加钱

    vegetableYesNo_prompt = 'you want vegetable? --yes/no: '
    yes_vegetable = pyip.inputYesNo(prompt=vegetableYesNo_prompt)
    if yes_vegetable== 'yes':
        chse_vegetable = pyip.inputMenu(opt_vegetable, timeout= 100)
        print('you choosed: ', opt_vegetable)
        time.sleep(0.5)
        if chse_vegetable == 'tomato':
            price_vegetable == 2
            sandwich_price += price_vegetable
        # ToDo: 添加选择其他选项的价格
    else:
        print('You don\'t want any vegetables')
        # 没选不加钱

    # 同类型的三明治要买几个
    sandwich_prompt = 'How many sandwich you want: ' # 假设每次选择同样类型的三明治
    num_sandwich = pyip.inputInt(sandwich_prompt, timeout= 100, min=1, max =5)
    print('you ordered '+ str(num_sandwich) + ' sandwiches.')

    # 同类型三明治的价格组成
    print('bread price: ', price_bread * num_sandwich)
    print('protein price: ', price_protein * num_sandwich)
    print('cheese price: ', price_cheese * num_sandwich)
    print('sauce price: ', price_sauce * num_sandwich)
    print('vegetable price: ', price_vegetable * num_sandwich)
    print('同类型三明治总价： %s' %((price_bread + price_protein + price_cheese + price_sauce + price_vegetable) * num_sandwich))
    global_price += (price_bread + price_protein + price_cheese + price_sauce + price_vegetable) * num_sandwich

    # 如果想买其他搭配的三明治--continue
    # 直到选择了所有想买的类型三明治，就结总账
    opt_other_sandwich = 'Do you want to buy other types: '
    want_other_sandwich = pyip.inputYesNo(prompt=opt_other_sandwich, timeout=100) 

    if want_other_sandwich == 'yes':
        continue # 回到循环的开头
    else:
        break

print('请付款： ', global_price)