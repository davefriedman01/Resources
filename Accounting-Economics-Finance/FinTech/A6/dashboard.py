#####
#
# imports
#
#####

import numpy as np
import pandas as pd
from pylab import mpl, plt
plt.style.use('seaborn')

import panel as pn
pn.extension('plotly')
import hvplot.pandas
import plotly.express as px

#####
#
# MapBox API
#
#####

from dotenv import find_dotenv, get_key
mapbox = get_key(find_dotenv(), 'mapbox')
px.set_mapbox_access_token(mapbox)

#####
#
# Data
#
#####

sfo = pd.read_csv('data/sfo_neighborhoods_census_data.csv', index_col='year')

#####
#
# Definitions
#
#####

def housing_units ():
    """ Number of San Fran Housing Units from 2010 to 2016 by Year """

    # compute the number of housing units per year
    df_housing_units = sfo['housing_units'].groupby(sfo.index).mean()

    # plot the number of housing units per year
    fig = plt.figure(figsize=(10, 6))
    ax = df_housing_units.plot.bar()
    ax.set_ylim(df_housing_units.min() - df_housing_units.std(), df_housing_units.max() + df_housing_units.std());
    ax.set_xlabel('Year', fontsize=12);
    ax.set_ylabel('Housing Units', fontsize=12);
    ax.set_title('Number of Housing Units in San Francisco from 2010 to 2016 by Year', fontsize=14, fontweight='bold');
    plt.close(fig);
    
    return df_housing_units, pn.pane.Matplotlib(fig, tight=True)

def housing_costs ():
    """ Average San Fran Housing Costs by Year """
    
    # compute the average sale price per square foot by year
    # compute the average monthly rent by year
    df_housing_costs = sfo[['sale_price_sqr_foot', 'gross_rent']].groupby(sfo.index).mean()

    # plot the average sale price per square foot by year
    # plot the average monthly rent by year
    fig = plt.figure(figsize=(10, 6))
    ax1 = df_housing_costs['sale_price_sqr_foot'].plot(color='blue')
    ax1.set_xlabel('Year', fontsize=12);
    ax1.set_ylabel('Average Sale Price per Square Foot', fontsize=12);
    ax1.set_title('Average Costs by Year', fontsize=14, fontweight='bold');
    ax1.legend();
    ax2 = ax1.twinx()
    ax2 = df_housing_costs['gross_rent'].plot(color='red')
    ax2.set_ylabel('Average Gross Rent', fontsize=12);
    ax2.legend(loc='upper right');
    ax2.grid(False);
    plt.close(fig);
    
    return df_housing_costs, pn.pane.Matplotlib(fig, tight=True)

def housing_costs_by_neighborhood ():
    """ Yearly San Fran Housing Costs by Neighborhood"""
    
    df = sfo.reset_index()
    
    # plot the average sale price per square foot by neighborhood
    plot_1_by_neighborhood = df.hvplot.line(
        'year',
        'sale_price_sqr_foot',
        groupby='neighborhood',
        xlabel='Year',
        ylabel='Average Sale Price per Square Foot',
        title='Yearly San Fran Sale Price per Square Foot by Neighborhood',
    )
    
    # plot the average gross rent by neighborhood
    plot_2_by_neighborhood = df.hvplot.line(
        'year',
        'gross_rent',
        groupby='neighborhood',
        xlabel='Year',
        ylabel='Average Gross Rent',
        title='Yearly San Fran Gross Rent by Neighborhood',
    )
    
    # plot the average costs by neighborhood
    plot_3_by_neighborhood = df.hvplot.bar(
        'year',
        ['gross_rent', 'sale_price_sqr_foot'],
        groupby='neighborhood',
        xlabel='Year',
        ylabel='Value',
        title='Yearly San Fran Housing Costs Comparison by Neighborhood',
        height=500,
        rot=90,
    )
    
    return plot_1_by_neighborhood, plot_2_by_neighborhood, plot_3_by_neighborhood

def top_ten ():
    """ Top Ten Most Expensive San Fran Neighborhoods by Sale Price per Square Foot """
    
    df = sfo.reset_index()
    
    df_top_ten = sfo.groupby('neighborhood').mean()
    df_top_ten = df_top_ten.sort_values(by='sale_price_sqr_foot', ascending=False)
    df_top_ten = df_top_ten.head(10)
    df_top_ten = df_top_ten.reset_index()

    plot_top_ten = df_top_ten.hvplot.bar(
        'neighborhood',
        'sale_price_sqr_foot',
        xlabel='Neighborhood',
        ylabel='Average Sale Price per Square Foot',
        title='Top Ten Most Expensive Neighborhoods in San Francisco',
        height=400,
        rot=90,
    )
    
    # filter data for top ten most expensive neighborhood data
    #df_top_ten_data = df_top_ten
    # or
    df_top_ten_data = df[df['neighborhood'].isin(df_top_ten['neighborhood'])]

    plot_categories = px.parallel_categories(
        df_top_ten_data,
        color='sale_price_sqr_foot',
        color_continuous_scale=px.colors.sequential.Inferno,
        title='Parallel Categories Visualization of Top Ten Most Expensive San Fran Neighborhoods data by Sale Price per Square Foot',
    )

    plot_coordinates = px.parallel_coordinates(
        df_top_ten_data,
        color='sale_price_sqr_foot',
        color_continuous_scale=px.colors.sequential.Inferno,
        title='Parallel Coordinates Visualization of Top Ten Most Expensive San Fran Neighborhoods data by Sale Price per Square Foot',
    )

    plot_sunburst = px.sunburst(
        df_top_ten_data,
        path=['year', 'neighborhood'],
        values='sale_price_sqr_foot',
        color='gross_rent',
        color_continuous_scale='Blues',
        title='Sunburst Visualization of Top Ten Most Expensive San Fran Neighborhoods data by Sale Price per Square Foot',
        height=700,
    )
    
    return df_top_ten, df_top_ten_data, plot_top_ten, plot_categories, plot_coordinates, plot_sunburst

def neighborhood_map ():
    """ San Fran Neighborhood Map """
    
    df_coords = pd.read_csv('data/neighborhoods_coordinates.csv')

    df_nebhds = sfo.groupby('neighborhood').mean()
    df_nebhds = df_nebhds.reset_index()
    df_nebhds = df_nebhds.rename(columns={'neighborhood': 'Neighborhood'})

    df_nebhds = pd.merge(df_coords, df_nebhds, on='Neighborhood', how='inner')

    plot_neighborhood_map = px.scatter_mapbox(
        df_nebhds,
        lat='Lat',
        lon='Lon',
        size='sale_price_sqr_foot',
        color='gross_rent',
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=11,
        hover_name='Neighborhood',
        title='Average San Fran Housing Costs',
    )
    
    return df_nebhds, plot_neighborhood_map



df_housing_units, plot_housing_units = housing_units()
df_housing_costs, plot_housing_costs = housing_costs()
plot1, plot2, plot3 = housing_costs_by_neighborhood()
df_top_ten, df_top_ten_data, plot_top_ten, plot_categories, plot_coordinates, plot_sunburst = top_ten()
df_nebhds, plot_neighborhood_map = neighborhood_map()

#####
#
# Dashboard
#
#####

title = pn.pane.Markdown(
    '## Real Estate Analysis of San Francisco from 2010 to 2016',
    width=800,
)
welcome = pn.pane.Markdown(
    '''
    This dashboard presents a visual analysis of historical prices of house units,
    sale price per square foot, and gross rent in San Francisco, CA from 2010 to 2016.
    You can navigate through the tabs above to explore more details about the evolution
    of the real estate market in the Golden City.
    '''
)
tabs = pn.Tabs(
    ('Welcome', pn.Column(welcome, plot_neighborhood_map)),
    ('Yearly Market Analysis', pn.Row(plot_housing_units, plot_housing_costs)),
    ('Neighborhood Analysis', pn.Column(plot1, plot2, plot_top_ten, plot3)),
    ('Parallel Plots Analysis', pn.Column(plot_categories, plot_coordinates, width=960)),
    ('Sunburst Plot Analysis', pn.Column(plot_sunburst)),
)
dashboard = pn.Column(pn.Row(title), tabs, width=900)
dashboard.servable()