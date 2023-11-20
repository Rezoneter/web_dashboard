import streamlit as st
import pandas as pd

# 판다스의 데이터프레임을 웹화면으로 보여주는 방법

def main():
    st.title('Iris Flower Data')

    df  = pd.read_csv('./data/iris.csv')
    
    st.dataframe(df)

    number_of_species = df['species'].nunique()

    st.text('Count of Iris Species: '+ str(number_of_species))



if __name__ == '__main__':
    main()