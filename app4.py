import streamlit as st
import pandas as pd

def main():
    pass
    st.title('Ready')

    df = pd.read_csv('./data/iris.csv')

    if st.button('Show DataFrame'):
        st.dataframe(df)

    name = 'Mike'
    
    st.text(name)
    # 버튼 생성
    if st.button('Big_Word'):
        st.subheader(name.upper())

    if st.button('Small_Word'):
        st.subheader( name.lower())
    
    # 라디오 버튼 생성
    selected = st.radio('Select Sort',['Ascending','Descending'])
    
    # df 의 petal_length 컬럼을 정렬
    if selected == 'Ascending' :
            st.dataframe(df.sort_values('petal_length', ascending=True))
    
    elif selected == 'Descending':
            st.dataframe(df.sort_values('petal_length', ascending=False))

    # 체크박스 생성
    if st.checkbox('Show DataFrame'):
         st.dataframe(df)
    else:
         st.write('')
    
    # 셀렉트 박스 생성
    language = ['Pyton', 'Java', 'C', 'PHP', 'GO' ]

    my_choice = st.selectbox('Select prefer language', language)

    st.subheader('I like {} language'.format(my_choice))

    if my_choice == language[0] or my_choice == language[3] or my_choice == language[4]:
         st.text('Easy to learn')
    elif my_choice == language[1] or my_choice == language[2]:
         st.text('Hard to learn')
    
    # 멀티 셀렉트 생성
    colums_list = df.columns
    selected_list = st.multiselect('Can select many options', colums_list)
    if len(selected_list) != 0:
         st.dataframe(df[selected_list])
    else:
         pass
    
    # 슬라이더 생성
    set_age = st.slider('Age',0,100)

    st.subheader('My age is {}'.format(set_age))

    st.slider('Data', 50, 200, step = 10)

    st.slider('Age', 0, 100, value = 33)

    st.slider('data', -0.5, 2.7, step = 0.1)

    with st.expander('More Info'):
         st.text('Detail Information')


if __name__ == '__main__' :
    main()