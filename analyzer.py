import pandas as pd

from keyword_analyzer import analyze_keywords
from campaign_analyzer import analyze_campaigns



def get_column_value(row, names):

    for name in names:

        if name in row:

            return row[name]

    return 0



def basic_analysis(df):


    spend = 0
    sales = 0
    clicks = 0
    orders = 0
    impressions = 0



    for _, row in df.iterrows():


        spend += float(
            get_column_value(
                row,
                [
                    "Spend",
                    "Spend (USD)",
                    "花费"
                ]
            )
            or 0
        )


        sales += float(
            get_column_value(
                row,
                [
                    "Sales",
                    "7 Day Total Sales",
                    "销售额"
                ]
            )
            or 0
        )


        clicks += int(
            get_column_value(
                row,
                [
                    "Clicks",
                    "点击"
                ]
            )
            or 0
        )


        orders += int(
            get_column_value(
                row,
                [
                    "Orders",
                    "7 Day Total Orders (#)",
                    "订单"
                ]
            )
            or 0
        )


        impressions += int(
            get_column_value(
                row,
                [
                    "Impressions",
                    "展示量"
                ]
            )
            or 0
        )



    acos = (

        spend / sales

        if sales > 0

        else 0

    )


    roas = (

        sales / spend

        if spend > 0

        else 0

    )


    cpc = (

        spend / clicks

        if clicks > 0

        else 0

    )


    cvr = (

        orders / clicks

        if clicks > 0

        else 0

    )



    return {


        "spend": spend,

        "sales": sales,

        "clicks": clicks,

        "orders": orders,

        "impressions": impressions,

        "acos": acos,

        "roas": roas,

        "cpc": cpc,

        "cvr": cvr

    }




def full_analysis(df):


    basic = basic_analysis(df)


    keywords = analyze_keywords(df)


    campaigns = analyze_campaigns(df)



    return {


        "basic": basic,


        "keywords": keywords,


        "campaigns": campaigns

    }
