import streamlit as st
import pandas as pd

from analyzer import full_analysis
from ai_report import generate_ai_report


st.set_page_config(
    page_title="Amazon Ads Intelligence System",
    page_icon="📊",
    layout="wide"
)


# =====================
# 页面标题
# =====================

st.title(
    "📊 Amazon Ads Intelligence System"
)

st.caption(
    "AI-powered Amazon PPC Analysis Platform"
)


# =====================
# 左侧菜单
# =====================

menu = st.sidebar.selectbox(

    "Navigation",

    [
        "🏠 Dashboard",
        "📤 Upload Data",
        "🔍 Keyword Analysis",
        "📢 Campaign Analysis",
        "🤖 AI Report"
    ]

)


# =====================
# Session保存数据
# =====================

if "analysis" not in st.session_state:

    st.session_state.analysis = None



# =====================
# 上传页面
# =====================

if menu == "📤 Upload Data":


    st.header(
        "📤 Upload Amazon Ads Report"
    )


    file = st.file_uploader(

        "Upload Excel / CSV",

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
            "File uploaded successfully"
        )


        if st.button(
            "🚀 Start Analysis"
        ):


            result = full_analysis(df)


            st.session_state.analysis = result


            st.success(
                "Analysis completed!"
            )



# =====================
# Dashboard
# =====================

elif menu == "🏠 Dashboard":


    st.header(
        "Today's Advertising Performance"
    )


    if st.session_state.analysis:


        basic = st.session_state.analysis["basic"]


        c1,c2,c3,c4 = st.columns(4)



        c1.metric(

            "Spend",

            f"€{basic['spend']:.2f}"

        )


        c2.metric(

            "Sales",

            f"€{basic['sales']:.2f}"

        )


        c3.metric(

            "ACOS",

            f"{basic['acos']:.2%}"

        )


        c4.metric(

            "ROAS",

            f"{basic['roas']:.2f}"

        )


        st.divider()



        st.subheader(
            "🚨 Smart Alerts"
        )


        waste = (
            st.session_state.analysis
            ["keywords"]
            ["waste"]
        )


        if len(waste)>0:


            st.warning(

                f"""
发现 {len(waste)} 个浪费关键词。

建议：
降低Bid或添加Negative Keyword。
"""

            )

        else:

            st.success(
                "暂无明显浪费关键词"
            )



    else:


        st.info(

            "请先上传广告数据"

        )



# =====================
# Keyword页面
# =====================

elif menu == "🔍 Keyword Analysis":


    st.header(
        "Keyword Performance"
    )


    if st.session_state.analysis:


        keywords = (
            st.session_state.analysis
            ["keywords"]
        )


        st.subheader(
            "🔴 Waste Keywords"
        )


        st.dataframe(

            pd.DataFrame(
                keywords["waste"]
            )

        )



        st.subheader(
            "🟢 Winner Keywords"
        )


        st.dataframe(

            pd.DataFrame(
                keywords["winner"]
            )

        )


    else:

        st.info(
            "请先上传数据"
        )



# =====================
# Campaign页面
# =====================

elif menu == "📢 Campaign Analysis":


    st.header(
        "Campaign Performance"
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
            "请先上传数据"
        )



# =====================
# AI报告
# =====================

elif menu == "🤖 AI Report":


    st.header(
        "AI Advertising Report"
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
            "请先上传数据"
        )
