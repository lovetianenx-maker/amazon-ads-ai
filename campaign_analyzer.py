def analyze_campaigns(df):


    result = []


    # 如果没有Campaign字段

    if "Campaign Name" not in df.columns:


        return result



    grouped = df.groupby(
        "Campaign Name"
    )



    for name, data in grouped:


        spend = data["Spend"].sum() \
            if "Spend" in data.columns else 0


        sales = data["Sales"].sum() \
            if "Sales" in data.columns else 0


        clicks = data["Clicks"].sum() \
            if "Clicks" in data.columns else 0


        orders = data["Orders"].sum() \
            if "Orders" in data.columns else 0



        acos = (

            spend / sales

            if sales > 0

            else 999

        )



        cvr = (

            orders / clicks

            if clicks > 0

            else 0

        )



        item = {


            "campaign": name,


            "spend": round(
                spend,
                2
            ),


            "sales": round(
                sales,
                2
            ),


            "acos": round(
                acos,
                2
            ),


            "cvr": round(
                cvr,
                2
            )

        }



        # 高风险Campaign

        if acos > 0.5:


            item["level"] = "高风险"


            item["suggestion"] = (

                "降低预算，检查高花费低转化关键词"

            )


        # 优秀Campaign

        elif acos < 0.25:


            item["level"] = "优秀"


            item["suggestion"] = (

                "增加预算，扩大关键词覆盖"

            )


        else:


            item["level"] = "正常"


            item["suggestion"] = (

                "持续观察优化"

            )



        result.append(
            item
        )



    return result
