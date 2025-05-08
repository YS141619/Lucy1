import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv("시_도별 인구.csv")
    
    # 컬럼 이름 정리
    df.columns = [col.strip().replace(' ', '_') for col in df.columns]
    
    # 컬럼 이름 변경 (데이터에 맞게 수정 필요)
    if '지역명' in df.columns:
        df = df.rename(columns={'지역명': 'Region'})
    if '인구수' in df.columns:
        df = df.rename(columns={'인구수': 'Population'})
    
    return df

df = load_data()

# 제목
st.title("시도별 인구 Dashboard")
st.markdown("📊 **시도별 인구 데이터를 다양한 방식으로 시각화한 대시보드입니다.**")

# 탭 구성
tab1, tab2 = st.tabs(["🌐 시도별 인구 시각화", "🏆 상위 인구 그래프"])

# 🌐 탭1: 시도별 인구 지도
with tab1:
    st.subheader("시도별 인구 지도")
    
    # 지도 시각화 (대한민국 행정구역에 맞게 수정 필요)
    fig_map = px.choropleth(
        df,
        locations="Region",  # 시도별 지역명 사용
        locationmode="ISO-3",  # 필요에 따라 적절한 locationmode 설정
        color="Population",
        hover_name="Region",
        color_continuous_scale="YlGnBu",
        title="시도별 인구"
    )
    st.plotly_chart(fig_map, use_container_width=True)

# 🏆 탭2: 시도별 인구 상위 10위 그래프
with tab2:
    st.subheader("시도별 인구 10위")
    
    # 인구 수 기준 상위 10개 지역 선택
    top10 = df.sort_values("Population", ascending=False).head(10)
    
    fig_bar = px.bar(
        top10,
        x="Population",
        y="Region",
        orientation="h",
        color="Population",
        color_continuous_scale="Blues",
        title="시도별 인구 10위"
    )
    st.plotly_chart(fig_bar, use_container_width=True)
