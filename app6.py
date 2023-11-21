import streamlit as st
import pandas as pd

# 숫자 또는 문자 입력 UI

def main():
    # text input
    input_name = st.text_input('Typing your name')    

    st.subheader('My name is ' + input_name)

    st.text_input('Input Name', max_chars=5, placeholder='James ')

    message = st.text_area('Typing some message', height=20)
    
    st.text(message)

    # number input
    birth = st.number_input('Typing your year of birth', 1900, 2023)

    st.text('My year of birth is '+str(birth))

    st.number_input('Input real number', -2.0, 100.0, step = 0.5)

    # Input date
    my_date = st.date_input('Input Meeting date')
    
    st.text(my_date)

    print(type(my_date))

    # year - month - day week on web screen
    st.text(my_date.strftime('Its %Y. %m. %d. %a'))

    # Input time
    my_time = st.time_input('Input what time is now')

    st.text(my_time.strftime('I have some meeting at %H:%M'))

    # Input password
    st.text_input('Input yout password',type='password')

    # Input color
    my_color = st.color_picker('Seclect prefer color')

    st.text(my_color)


if __name__ == '__main__':
    main()