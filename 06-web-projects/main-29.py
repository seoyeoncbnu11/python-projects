import streamlit as st
import datetime
import pyupbit

d = st.date_input("날짜를 선택하세요", datetime.date.today())

st.write("비트코인 1일 차트")

ticker = "KRW-BTC"
interval = "minute60"
to = str(d + datetime.timedelta(days=1))  # 선택 날짜의 다음 날까지 포함되도록 설정
count = 24
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

if price_now is not None and not price_now.empty:
    # st.dataframe(price_now)
    st.line_chart(price_now["close"])  # 종가 시각화
else:
    st.error(
        "OHLCV 데이터를 가져오지 못했습니다. 날짜를 다시 선택하거나 나중에 시도해보세요."
    )
