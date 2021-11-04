import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Analysis by Asaoka')
st.write('ver. 2021.11.4 ')


uploaded_file=st.file_uploader('↓ここにCSVデータをアップロード！')

expander=st.expander('CSVの書式')
expander.write('① CSV形式のみ対応')
expander.write('② インデックス無し，1行目がカラムになります．')
expander.write('③ 右下のダウンロードボタンでテンプレをダウンロードできます．')

df=pd.DataFrame({'x1':[0,1,2,3],'x2':[5,8,8,9],'x3':[2,4,6,8]})

left_column,right_column=st.columns(2)

csv=open('data2.csv')
left_column.write('サンプルデータ')
right_column.download_button('Download:サンプルデータ',csv,file_name='テンプレート.csv',mime='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write('現在のデータ')

st.dataframe(df)
    
graph_list=['折れ線グラフ(Streamlit)',
            '棒グラフ(Streamlit)',
            'ヒストグラム(pyplot)']
option=st.selectbox('グラフの種類',graph_list)

if option == graph_list[0]:
    st.line_chart(df)
elif option==graph_list[1]:
    st.bar_chart(df)
elif option==graph_list[2]:
    fig,ax=plt.subplots()
    ax.hist(df)
    st.pyplot(fig)


#st.write('option',option)

#left_column,right_column=st.columns(2)
#button1=left_column.button('left')
#if button1:
#    right_column.write('yes')

#expander=st.expander('問い合わせ')
#expander.write('come on!')


#text=st.text_input('Your hobby')
#condition=st.slider('Your condition',0,100,50)
#'You love',text,'!'

#'Your condition:',condition
