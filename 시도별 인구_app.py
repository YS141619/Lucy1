import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv("시_도별 인구.csv")
    df.columns = [col.replace('Explained by: ', '').replace(' ', '_').lower() for col in df.columns]
    df = df.rename(columns={'country_name': 'Country', 'ladder_score': 'Happiness_Score'})
    return df

df = load_data()

# 제목
st.title("시도별인구 Dashboard")
st.markdown("📊 **시도별인구 데이터를 다양한 방식으로 시각화한 대시보드입니다.**")

# 탭 구성
tab1, tab2 = st.tabs(["🌐 시도별 인구 시각화", "🏆 상위 인구 그래프"])

# 🌐 탭1: 시도별 인구 지도
with tab1:
    st.subheader("시도별 인구 지도")
    fig_map = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Happiness_Score",
        hover_name="Country",
        color_continuous_scale="YlGnBu",
        title="시도별 인구"
    )
    st.plotly_chart(fig_map, use_container_width=True)

# 🏆 탭2: 시도별 인구 상위 10위 그래프
with tab2:
    st.subheader("시도별 인구 10위")
    top10 = df.sort_values("Happiness_Score", ascending=False).head(10)
    fig_bar = px.bar(
        top10,
        x="Happiness_Score",
        y="Country",
        orientation="h",
        color="Happiness_Score",
        color_continuous_scale="Blues",
        title="시도별 인구 10위"
    )
    st.plotly_chart(fig_bar, use_container_width=True)


     st.markdown("📌 선형 추세선을 통해 변수 간 관계를 시각적으로 파악할 수 있습니다.")
