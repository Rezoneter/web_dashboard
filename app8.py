import streamlit as st
import pandas as pd
from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main():
    st.title('File separate app')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('Menu select', menu )

    if choice == menu[0]:
        run_home_app()

    elif choice == menu[1]:
        run_eda_app()


    elif choice == menu[2]:
        run_ml_app()



if __name__ == '__main__':
    main()