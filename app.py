import streamlit as st
import pandas as pd

from analyzer import full_analysis
from ai_report import generate_ai_report


st.set_page_config(
    page_title="Amazon Ads Intelligence System",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Amazon Ads Intelligence System")

st.write(
    "上传 Amazon 广告报表，AI自动分析广告表现并生成优化建议"
)


file = st.file_uploader(
    "上传 Amazon Ads Excel/CSV 文件",
    type=["xlsx","csv"]
)



if file:


    if file.name.endswith(".xlsx"):

        df = pd.read_excel(file)

    else:

        df = pd.read_csv(file)



    st.success("文件上传成功")


    st.subheader("数据预览")

    st.dataframe(
        df.head(10)
    )


    if st.button(
        "🚀 开始AI分析"
    ):


        with st.spinner(
            "正在分析广告数据..."
        ):


            result = full_analysis(df)


            report = generate_ai_report(
                result
            )


        st.divider()


        st.header(
            "📈 广告核心指标"
        )


        basic=result["basic"]


        c1,c2,c3,c4=st.columns(4)


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


        st.header(
            "🤖 AI优化报告"
        )


        st.markdown(
            report
        )
