import streamlit as st


st.set_page_config(page_title="Home",layout="wide",page_icon='./images/home.png')
st.title("YOLO V5 Detection App")
st.caption('Demonstrate Object Detection')

#content
st.markdown("""
### This app detexts objects from images
- イメージから自動で20のオブジェクトを検出する
- [こちらから](/YOLO_for_image/)

次の物体を検出します

1.人
2.車
3.椅子
4.ボトル
5.ソファ
6.自転車
7.馬
8.ボート
9.バイク
10.猫
11.TV
12.牛
13.羊
14.飛行機
15.電車
16.ダイニングテーブル
17.バス
18.植物
19.鳥
20.犬
""")