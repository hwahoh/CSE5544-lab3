import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt



st.title("Hayden Wahoff CSE 5544 Lab 3")

st.header("Visualization 1")



data = pd.read_csv("https://raw.githubusercontent.com/CSE5544/data/main/ClimateData.csv")


dataviz1 = data.drop(columns=['Non-OECD Economies'])
dataviz1 = dataviz1.drop(index=[17,43,44,45])
dataviz1 = pd.melt(dataviz1, id_vars=['Country\year'], var_name='year')
dataviz1['value'] = dataviz1['value'].apply(pd.to_numeric, errors='coerce')
dataviz1.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)

heatmap1 = alt.Chart(dataviz1).mark_rect().encode(
    x=alt.X('country:N', title = 'Country'),
    y=alt.Y('year:O', title = 'Year'),
    color=alt.Color('emission:Q',scale=alt.Scale(scheme="inferno")),
    tooltip=['country', 'year', 'emission']
).properties(
    title='Emissions of Countries Each Year'
)

heatmap1 = heatmap1.configure_title(
    fontSize=30,
    font='Courier'
)

heatmap1 = heatmap1.configure_legend(
    fillColor = 'gray'
)

st.altair_chart(heatmap1, use_container_width = True)

st.header("Visualization 2")
dataviz2 = data.drop(columns=['Non-OECD Economies'])
dataviz2 = dataviz2.drop(index=[17,43,44,45,61])
dataviz2 = pd.melt(dataviz2, id_vars=['Country\year'], var_name='year')
dataviz2['value'] = dataviz2['value'].apply(pd.to_numeric, errors='coerce')
dataviz2.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)

heatmap2 = alt.Chart(dataviz2).mark_rect().encode(
    x=alt.X('country:N', title = 'Country'),
    y=alt.Y('year:O', title = 'Year'),
    color=alt.Color('emission:Q',scale=alt.Scale(scheme="rainbow")),
    tooltip=['country', 'year', 'emission']
).properties(
    title='The Rest of The World\'s Carbon Emissions ',
    background = "indigo",
)

heatmap2 = heatmap2.configure_title(
    fontSize = 30,
    color = 'yellow'
)

heatmap2 = heatmap2.configure_axisX(
    labelColor = 'yellow',
    titleColor = 'yellow'
)

heatmap2 = heatmap2.configure_axisY(
    labelColor = 'yellow',
    titleColor = 'yellow'
)

heatmap2 = heatmap2.configure_legend(
    labelColor = 'yellow',
    titleColor = 'yellow'
)

st.altair_chart(heatmap2, use_container_width =True)

st.markdown('As you can see from the above visualizations, there is a clear difference between the two visualizations. The first one has a clear and unbiased presentation, as the color scheme is not misleading, the title and axes are clearly defined, the missing data is easily seen, and aggregate categories such as "OECD - Total" and "European Union" are removed to show individual countries only. The second visualization, however, is clearly biased as the United States is completely removed from the graph and the title seems to indicate that this visualization was maybe made by a patriot who wanted to show carbon emissions in the world excluding America. Also, the rainbow color scheme is misleading, because the lower and upper extremes of the graph have similar colors. In addition, the background color is set to indigo to further confuse the viewer where data is missing, implying that emissions are higher than they really are.As you can see from the above visualizations, there is a clear difference between the two visualizations. The first one has a clear and unbiased presentation, as the color scheme is not misleading, the title and axes are clearly defined, the missing data is easily seen, and aggregate categories such as "OECD - Total" and "European Union" are removed to show individual countries only. The second visualization, however, is clearly biased as the United States is completely removed from the graph and the title seems to indicate that this visualization was maybe made by a patriot who wanted to show carbon emissions in the world excluding America. Also, the rainbow color scheme is misleading, because the lower and upper extremes of the graph have similar colors. In addition, the background color is set to indigo to further confuse the viewer where data is missing, implying that emissions are higher than they really are.')