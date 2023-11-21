import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main():
    st.title('Draw chart')

    df = pd.read_csv('./data/iris.csv')

    st.dataframe(df)

    # Relation of petal_length and petal_width 

    # matplotlib or seaborn 
    
    fig1 = plt.figure()
    plt.scatter (data= df, x= 'petal_length', y = 'petal_width')
    plt.title('Petal length vs width')
    plt.xlabel('Length')
    plt.ylabel('Width')
    st.pyplot(fig1)

    fig2 = plt.figure()
    sb.regplot(data =df, x='petal_length', y= 'petal_width')
    st.pyplot(fig2)

    # Draw histogram with petal_length
    fig3 = plt.figure()
    plt.hist(data = df, x='petal_length', rwidth = 0.8, bins = 20)
    st.pyplot(fig3)

    # One char area, draw two charts
    fig4 = plt.figure(figsize = (10,4))

    plt.subplot (1,2,1)
    plt.hist(data = df, x ='petal_length', rwidth =0.8, bins = 10)

    plt.subplot (1,2,2)
    plt.hist(data = df, x ='petal_length', rwidth =0.8, bins = 20)
    st.pyplot(fig4)

    # Use pandas chart
    fig6 = plt.figure()
    df['petal_length'].hist()
    st.pyplot(fig6)

    fig7 = plt.figure()
    df['species'].value_counts.plot(kind='bar')
    st.pyplot(fig7)

    fig8 = plt.figure()
    sb.countplt(data = df, x='species')
    st.pyplot(fig8)

    # pltm seaborn, pandas chart are
    # save chart area with plt.figure in variable
    # draw with st.pyplot 

if __name__ == '__main__':
    main()