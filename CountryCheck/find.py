import plotly.express as px
from countryinfo import CountryInfo
import pandas as pd

country = CountryInfo(input("Enter country: ")).name()

data = pd.DataFrame({
    'Country': [country],
    'Values': [100]
})


fig = px.choropleth(
    data, 
    locations='Country', 
    locationmode='country names', 
    color='Values', 
    color_continuous_scale='Inferno', 
    title=f'Country Map Highlighting {country}'
)
fig.show()
