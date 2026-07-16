import streamlit as st
import pandas as pd
import plotly.express as px
from analyzer import full_analysis
from ai_report import generate_ai_report


st.set_page_config(
    page_title="Amazon Ads智能分析系统",
    page_icon="📊",
    layout="wide"
)


# =========================
# 标题
# =========================

st.title(
    "📊 Amazon Ads Intelligence System"
)

st.caption(
    "亚马逊广告智能分析与优化系统"
)


# =========================
# 菜单
# =========================

menu = st.sidebar.selectbox(

    "功能导航",

    [
        "🏠 数据看板",
        "📤 上传广告数据",
        "🔍 关键词分析",
        "📢 广告活动分析",
        "🤖 AI优化报告"
    ]

)



# 保存分析结果

if "analysis" not in st.session_state:

    st.session_state.analysis = None



# =========================
# 上传页面
# =========================

if menu == "📤 上传广告数据":


    st.header(
        "📤 上传Amazon广告报表"
    )


    st.info(
        """
支持：

- Sponsored Products
- Sponsored Brands
- Sponsored Display

格式：

Excel (.xlsx)
CSV

建议上传最近30天数据
"""
    )



    file = st.file_uploader(

        "选择广告报表",

        type=[
            "xlsx",
            "csv"
        ]

    )



    if file:


        if file.name.endswith(".xlsx"):

            df = pd.read_excel(file)

        else:

            df = pd.read_csv(file)



        st.success(
            "广告数据上传成功"
        )


        st.write(
            "数据预览："
        )


        st.dataframe(
            df.head(10)
        )



        if st.button(
            "🚀 开始智能分析"
        ):


            result = full_analysis(df)


            st.session_state.analysis = result


            st.success(
                "分析完成，请查看各模块"
            )



# =========================
# Dashboard
# =========================

elif menu == "🏠 数据看板":


    st.header(
        "📈 今日广告表现"
    )


    if st.session_state.analysis:


        data = (
            st.session_state.analysis
            ["basic"]
        )


        c1,c2,c3,c4 = st.columns(4)



        c1.metric(
            "广告花费",
            f"€{data['spend']:.2f}"
        )


        c2.metric(
            "广告销售额",
            f"€{data['sales']:.2f}"
        )


        c3.metric(
            "ACOS",
            f"{data['acos']:.2%}"
        )


        c4.metric(
            "ROAS",
            f"{data['roas']:.2f}"
        )



        st.divider()
        # =====================
        # 数据可视化
        # =====================


        st.subheader(
            "📊 广告数据可视化"
        )


        chart_data = pd.DataFrame({

            "指标":[
                "广告花费",
                "广告销售额"
            ],


            "金额":[

                data["spend"],

                data["sales"]

            ]

        })


        fig = px.bar(

            chart_data,

            x="指标",

            y="金额",

            title="广告投入与销售"

        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.subheader(
            "💚 广告健康评分"
        )


        score = 100



        if data["acos"] > 0.5:

            score -= 30


        if data["cpc"] > 1:

            score -= 15



        if len(waste) > 5:

            score -= 20



        score=max(
            score,
            0
        )



        if score >=80:

            level="优秀"


        elif score>=60:

            level="正常"


        else:

            level="需要优化"



        st.metric(

            "广告健康分",

            f"{score}/100"

        )


        st.info(

            f"当前等级：{level}"

        )
        st.subheader(
            "🚨 智能优化提醒"
        )



        waste = (

            st.session_state.analysis
            ["keywords"]
            ["waste"]

        )


        if waste:


            st.warning(

                f"""
发现 {len(waste)} 个浪费关键词。


建议：

降低竞价 Bid

添加否定关键词

检查搜索词匹配


"""

            )

        else:


            st.success(
                "暂无明显广告浪费"
            )


    else:


        st.info(
            "请先上传广告数据"
        )



# =========================
# Keyword
# =========================

elif menu == "🔍 关键词分析":


    st.header(
        "🔍 广告关键词分析"
    )


    if st.session_state.analysis:


        keywords = (

            st.session_state.analysis
            ["keywords"]

        )


        st.subheader(
            "🔴 浪费关键词"
        )


        st.dataframe(

            pd.DataFrame(
                keywords["waste"]
            )

        )



        st.subheader(
            "🟢 优质关键词"
        )


        st.dataframe(

            pd.DataFrame(
                keywords["winner"]
            )

        )



        st.subheader(
            "🟡 潜力关键词"
        )


        st.dataframe(

            pd.DataFrame(
                keywords["potential"]
            )

        )


    else:


        st.info(
            "请先上传广告数据"
        )



# =========================
# Campaign
# =========================

elif menu == "📢 广告活动分析":


    st.header(
        "📢 Campaign广告活动分析"
    )



    if st.session_state.analysis:


        campaigns = (

            st.session_state.analysis
            ["campaigns"]

        )


        st.dataframe(

            pd.DataFrame(
                campaigns
            )

        )


    else:


        st.info(
            "请先上传广告数据"
        )



# =========================
# AI报告
# =========================

elif menu == "🤖 AI优化报告":


    st.header(
        "🤖 AI广告优化日报"
    )


    if st.session_state.analysis:


        report = generate_ai_report(

            st.session_state.analysis

        )


        st.markdown(
            report
        )


    else:


        st.info(
            "请先上传广告数据"
        )
