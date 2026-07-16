def get_value(row, names):

    for name in names:

        if name in row:

            return row[name]

    return 0



def analyze_keywords(
    df,
    target_acos=0.35
):


    result = {

        "waste": [],

        "winner": [],

        "potential": []

    }



    for _, row in df.iterrows():


        keyword = get_value(
            row,
            [
                "Keyword",
                "Search Term",
                "关键词",
                "搜索词"
            ]
        )


        clicks = int(
            get_value(
                row,
                [
                    "Clicks",
                    "点击"
                ]
            )
            or 0
        )


        orders = int(
            get_value(
                row,
                [
                    "Orders",
                    "7 Day Total Orders (#)",
                    "订单"
                ]
            )
            or 0
        )


        spend = float(
            get_value(
                row,
                [
                    "Spend",
                    "花费"
                ]
            )
            or 0
        )


        sales = float(
            get_value(
                row,
                [
                    "Sales",
                    "7 Day Total Sales",
                    "销售额"
                ]
            )
            or 0
        )



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


            "keyword": keyword,


            "clicks": clicks,


            "orders": orders,


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



        # 浪费关键词

        if (

            clicks >= 20

            and orders == 0

        ) or (

            acos > target_acos * 2

        ):


            item["suggestion"] = (

                "降低Bid，暂停关键词，添加Negative Keyword"

            )


            result["waste"].append(
                item
            )



        # 优质关键词

        elif (

            clicks >= 10

            and orders > 0

            and acos < target_acos

        ):


            item["suggestion"] = (

                "提高Bid，增加预算，建立Exact广告"

            )


            result["winner"].append(
                item
            )



        # 潜力关键词

        elif (

            clicks >= 5

            and orders > 0

            and cvr > 0.15

        ):


            item["suggestion"] = (

                "增加曝光，提高竞价测试"

            )


            result["potential"].append(
                item
            )



    return result
