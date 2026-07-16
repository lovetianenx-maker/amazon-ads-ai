def generate_ai_report(data):


    basic = data["basic"]


    report = ""


    report += "# Amazon Ads Intelligence Report\n\n"



    report += "## 1. 广告整体表现\n\n"


    report += f"""
广告花费：

€{basic['spend']:.2f}


广告销售：

€{basic['sales']:.2f}


ACOS：

{basic['acos']:.2%}


ROAS：

{basic['roas']:.2f}


点击：

{basic['clicks']}


订单：

{basic['orders']}


"""


    report += "\n---\n"



    report += "## 2. 关键词分析\n\n"



    waste = data["keywords"]["waste"]


    winner = data["keywords"]["winner"]


    potential = data["keywords"]["potential"]



    report += f"""

发现：

🔴 浪费关键词：

{len(waste)} 个



🟢 优质关键词：

{len(winner)} 个



🟡 潜力关键词：

{len(potential)} 个



"""



    if len(waste) > 0:


        report += """

### 浪费关键词建议


建议：

- 降低Bid

- 暂停无转化关键词

- 添加Negative Keyword


"""



    if len(winner) > 0:


        report += """

### 优质关键词建议


建议：

- 提高Bid 15%-25%

- 增加预算

- 创建Exact Match广告


"""



    report += "\n---\n"


    report += "## 3. Campaign分析\n\n"



    for campaign in data["campaigns"][:5]:


        report += f"""

Campaign:

{campaign['campaign']}


状态:

{campaign['level']}


ACOS:

{campaign['acos']:.2%}


建议:

{campaign['suggestion']}



"""



    report += "\n---\n"



    report += """

## 4. 今日执行清单


☐ 检查高花费无订单关键词


☐ 优化高ACOS Campaign


☐ 扩大低ACOS关键词流量


☐ 添加Negative Keyword



"""


    return report
