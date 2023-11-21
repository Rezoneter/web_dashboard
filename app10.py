import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd


def main():
    df = pd.read_csv('./data/lang_data.csv')
    st.dataframe(df)

    # Make multi select
    # show programming language column
    # show only selected language 

    column_menu = df.columns[1:]

    choice_list = st.multiselect('Select Language', column_menu)

    print(choice_list)
    if len(choice_list) != 0:
        # Draw chart of User selected language

        # First, get selected dataframe columns
        df_selcted = df[choice_list]

        # streamlit chart, line chart
        st.line_chart(data = df_selcted)

        # streamlit chart, area chart
        st.area_chart(data = df_selcted)

        # streamlit chart, bar chart
        st.bar_chart(data = df_selcted)

        # Data from 2017.04 ~ 2018.03 
        # Draw bar chart
        
        my_filter = (df['Week'] >= '2017-04') & (df['Week'] <= '2018-03')

        df_2017_2018 = df.loc[my_filter,]

        df3 = df_2017_2018[choice_list]

        st.bar_chart(data = df3)

        df_iris = pd.read_csv('./data/iris.csv')

        # Relation of two columns 
        # Show species info too

        chart = alt.Chart(data = df_iris).mark_circle().encode(x = 'petal_length', y = 'petal_width', color = 'species')
        st.altair_chart(chart)

        # Get location info and show it on the map
        # streamlit map chart

        df_location = pd.read_csv('./data/location.csv')

        st.dataframe(df_location)

        st.map(data = df_location)

        # Draw plotly chart 
        df_prog = pd.read_csv('./data/prog_languages_data.csv', index_col=0)
        st.dataframe(df_prog)
        
        # 1. pie chart
        chart2 = px.pie(df_prog, names = 'lang', values='Sum', title= 'Several Languages pie chart')

        st.plotly_chart(chart2)
        
        # 2. bar chart
        sorted_df = df_prog.sort_values('Sum',ascending=False)
        chart3 = px.bar(sorted_df, x ='lang', y='Sum')
        st.plotly_chart(chart3)



if __name__ == '__main__':
    main()