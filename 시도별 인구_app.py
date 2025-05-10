import streamlit as st
import pandas as pd
import plotly.express as px
import json

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv("시_도별 인구.csv")
    df.columns = [col.strip().replace(' ', '_') for col in df.columns]
    df = df.rename(columns={'지역명': 'Region', '인구수': 'Population'})
    return df

@st.cache_data
def load_geojson():
    with open("skorea-provinces-geo.json", encoding="utf-8") as f:
        geojson = json.load(f)
    return geojson

df = load_data()
geojson = load_geojson()

st.title("시도별 인구 Dashboard")
st.markdown("📊 **시도별 인구 데이터를 다양한 방식으로 시각화한 대시보드입니다.**")

tab1, tab2 = st.tabs(["🌐 시도별 인구 시각화", "🏆 상위 인구 그래프"])

with tab1:
    st.subheader("시도별 인구 지도")
    fig_map = px.choropleth(
        df,
        geojson=geojson,
        locations='Region',
        featureidkey="properties.name",
        color="Population",
        color_continuous_scale="YlGnBu",
        hover_name="Region",
        title="시도별 인구 지도"
    )
    fig_map.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig_map, use_container_width=True)

with tab2:
    st.subheader("시도별 인구 10위")
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
