import dash
from dash import html, dcc
from dash import Input, Output
import pandas as pd
from utils import load_combined_data

# Load data
df = load_combined_data()

# Extract dropdown options
countries = sorted(df['Country'].dropna().unique())
years = sorted(df['Year'].dropna().unique())

# Create app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Gender Gap in Energy Sector"

# Layout
app.layout = html.Div([
    html.H1("Gender Gap Visual Analytics Dashboard", style={'textAlign': 'center'}),

    dcc.Tabs([

        # Overview Tab
        dcc.Tab(label='Overview', children=[
            html.Div([
                html.Div([
                    html.Label("Select Country:"),
                    dcc.Dropdown(
                        id='country-dropdown',
                        options=[{'label': c, 'value': c} for c in countries],
                        value='France',
                        clearable=False
                    )
                ], style={'width': '30%', 'display': 'inline-block'}),

                html.Div([
                    html.Label("Select Year Range:"),
                    dcc.RangeSlider(
                        id='year-slider',
                        min=min(years),
                        max=max(years),
                        value=[min(years), max(years)],
                        marks={str(y): str(y) for y in years[::2]},
                        step=1
                    )
                ], style={'width': '65%', 'display': 'inline-block', 'paddingLeft': '30px'}),

                html.Br(), html.Br(),

                html.Div([
                    html.Div(id="kpi-wage-gap", className="kpi-box"),
                    html.Div(id="kpi-senior-roles", className="kpi-box"),
                    html.Div(id="kpi-inventors", className="kpi-box"),
                    html.Div(id="kpi-founders", className="kpi-box"),
                ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginTop': '20px'})
            ])
        ]),

        # Employment Tab
        dcc.Tab(label='Employment', children=[
            html.Div([
                html.H3("Employment Analytics", style={'textAlign': 'center'}),

                html.Div([
                    html.Label("Select Country:"),
                    dcc.Dropdown(
                        id='emp-country',
                        options=[{'label': c, 'value': c} for c in countries],
                        value='France',
                        clearable=False
                    ),
                ], style={'width': '30%', 'margin': '10px'}),

                dcc.Graph(id='emp-wage-line'),
                html.Br(),
                dcc.Graph(id='emp-bar-gap'),
            ])
        ]),

        # Senior Management Tab
        dcc.Tab(label='Senior Management', children=[
            html.Div([
                html.H3("Senior Management Representation", style={'textAlign': 'center'}),

                html.Div([
                    html.Label("Select Country:"),
                    dcc.Dropdown(
                        id='sm-country',
                        options=[{'label': c, 'value': c} for c in countries],
                        value='France',
                        clearable=False
                    ),
                ], style={'width': '30%', 'margin': '10px'}),

                dcc.Graph(id='sm-role-bar'),
                html.Br(),
                dcc.Graph(id='sm-role-trend')
            ])
        ]),

        # Innovation & Patents Tab — FIXED!
        dcc.Tab(label='Innovation & Patents', children=[
            html.Div([
                html.H3("Innovation & Patents", style={'textAlign': 'center'}),

                html.Div([
                    html.Label("Select Country:"),
                    dcc.Dropdown(
                        id='innovation-country',
                        options=[{'label': c, 'value': c} for c in countries],
                        value='France',
                        clearable=False
                    ),
                ], style={'width': '30%', 'margin': '10px'}),

                html.Div([
                    html.Label("Select Technology or Sector:"),
                    dcc.Dropdown(
                        id='innovation-sector',
                        options=[{'label': 'All', 'value': 'All'}],
                        value='All',
                        clearable=False
                    ),
                ], style={'width': '50%', 'margin': '10px'}),

                dcc.Graph(id='innovation-tech-bar'),
                html.Br(),
                dcc.Graph(id='innovation-trend-line')
            ])
        ]),

        # Empty Tabs (you can fill them later!)
        dcc.Tab(label='Entrepreneurship', children=[
    html.Div([
        html.H3("Entrepreneurship & Startups", style={'textAlign': 'center'}),

        html.Div([
            html.Label("Select Country:"),
            dcc.Dropdown(
                id='entrepreneurship-country',
                options=[{'label': c, 'value': c} for c in countries],
                value='France',
                clearable=False
            ),
        ], style={'width': '30%', 'margin': '10px'}),

        dcc.Graph(id='entrepreneurship-sector-bar'),
        html.Br(),
        dcc.Graph(id='entrepreneurship-trend-line')
    ])
]),

        dcc.Tab(label='Explorer', children=[
    html.Div([
        html.H3("Explorer", style={'textAlign': 'center'}),

        html.Div([
            html.Label("Select Country:"),
            dcc.Dropdown(
                id='explorer-country',
                options=[{'label': c, 'value': c} for c in countries],
                value='France',
                clearable=False
            ),
        ], style={'width': '30%', 'margin': '10px'}),

        html.Div([
            html.Label("Select Topic:"),
            dcc.Dropdown(
                id='explorer-topic',
                options=[{'label': t, 'value': t} for t in sorted(df['Topic'].dropna().unique())],
                value='Employment',
                clearable=False
            ),
        ], style={'width': '30%', 'margin': '10px'}),

        html.Div([
            html.Label("Select Indicator:"),
            dcc.Dropdown(
                id='explorer-indicator',
                options=[],  # Will be updated dynamically
                value=None,
                clearable=False
            ),
        ], style={'width': '50%', 'margin': '10px'}),

        dcc.Graph(id='explorer-trend-line')
    ])
]),

        dcc.Tab(label='Advanced Insights', children=[
    html.Div([
        html.H3("Advanced Insights", style={'textAlign': 'center'}),

        html.Div(id='advanced-kpi-senior-roles', className='kpi-box', style={'margin': '10px'}),
        html.Div(id='advanced-kpi-female-inventors', className='kpi-box', style={'margin': '10px'}),
        html.Div(id='advanced-kpi-wage-gap', className='kpi-box', style={'margin': '10px'}),
        html.Div(id='advanced-kpi-diverse-founders', className='kpi-box', style={'margin': '10px'})
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around', 'marginTop': '20px'})
]),


    ])  # CLOSE dcc.Tabs here
])  # CLOSE html.Div here


# End of layout above...

@app.callback(
    Output("kpi-wage-gap", "children"),
    Output("kpi-senior-roles", "children"),
    Output("kpi-inventors", "children"),
    Output("kpi-founders", "children"),
    Input("country-dropdown", "value"),
    Input("year-slider", "value")
)
def update_kpis(country, year_range):
    dff = df[(df["Country"] == country) & 
             (df["Year"] >= year_range[0]) & 
             (df["Year"] <= year_range[1])]

    wage_gap = dff[dff["Indicator"].str.contains("wage gap", case=False, na=False)]
    avg_wage_gap = wage_gap["Value"].mean()

    senior = dff[(dff["Topic"] == "Senior Management") & 
                 (dff["Indicator Categories"].str.lower() == "women")]
    senior_pct = senior["Value"].mean()

    inventors = dff[(dff["Topic"] == "Innovation") & 
                    (dff["Indicator"].str.contains("female inventors", case=False, na=False))]
    inventors_pct = inventors["Value"].mean()

    founders = dff[(dff["Topic"] == "Entrepreneurship") & 
                   (dff["Indicator"].str.contains("gender diverse", case=False, na=False))]
    founders_pct = founders["Value"].mean()

    return (
        f"📊 Avg Gender Wage Gap: {avg_wage_gap:.2f}%" if not pd.isna(avg_wage_gap) else "📊 No data",
        f"👩‍💼 % Women in Senior Roles: {senior_pct:.2f}%" if not pd.isna(senior_pct) else "👩‍💼 No data",
        f"💡 % Female Inventors: {inventors_pct:.2f}%" if not pd.isna(inventors_pct) else "💡 No data",
        f"🚀 % Gender-Diverse Founders: {founders_pct:.2f}%" if not pd.isna(founders_pct) else "🚀 No data"
    )

@app.callback(
    Output('emp-wage-line', 'figure'),
    Output('emp-bar-gap', 'figure'),
    Input('emp-country', 'value')
)
def update_employment_charts(selected_country):
    dff = df[(df['Country'] == selected_country) & (df['Topic'] == 'Employment')]

    # Line chart: Wage gap over time
    wage_data = dff[dff['Indicator'].str.contains("wage gap", case=False, na=False)]
    wage_data = wage_data[(wage_data['Value'] > -100) & (wage_data['Value'] < 100)]

    if wage_data.empty:
        line_fig = {
            "layout": {
                "title": f"No Data Available for {selected_country} in this Period",
                "xaxis": {"visible": False},
                "yaxis": {"visible": False},
                "annotations": [
                    {
                        "text": "No data found for wage gap indicators",
                        "xref": "paper",
                        "yref": "paper",
                        "showarrow": False,
                        "font": {"size": 16}
                    }
                ]
            }
        }
    else:
        # Group by year and calculate average wage gap
        grouped = wage_data.groupby("Year")["Value"].mean().reset_index()

        line_fig = {
            "data": [
                {
                    "x": grouped["Year"],
                    "y": grouped["Value"],
                    "type": "line",
                    "name": "Avg Wage Gap (%)",
                    "line": {"color": "blue"}
                }
            ],
            "layout": {
                "title": f"Average Gender Wage Gap Over Time in {selected_country}",
                "yaxis": {"title": "Wage Gap (%)"},
                "xaxis": {"title": "Year"},
                "height": 400
            }
        }

    # Bar chart: Gap by contract type or occupation
    bar_data = dff[dff["Indicator"].str.contains("contract|occupation", case=False, na=False)]
    bar_data = bar_data[(bar_data['Value'] > -100) & (bar_data['Value'] < 100)]

    if bar_data.empty:
        bar_fig = {
            "layout": {
                "title": f"No contract/occupation data for {selected_country}",
                "xaxis": {"visible": False},
                "yaxis": {"visible": False}
            }
        }
    else:
        bar_fig = {
            "data": [
                {
                    "x": bar_data["Indicator"],
                    "y": bar_data["Value"],
                    "type": "bar",
                    "name": "Gap (%)"
                }
            ],
            "layout": {
                "title": f"Employment Gaps by Type in {selected_country}",
                "yaxis": {"title": "Gap (%)"},
                "xaxis": {"title": "Indicator", "tickangle": -45}
            }
        }

    return line_fig, bar_fig

@app.callback(
    Output('sm-role-bar', 'figure'),
    Output('sm-role-trend', 'figure'),
    Input('sm-country', 'value')
)
def update_senior_management_charts(country):
    dff = df[(df['Country'] == country) & 
             (df['Topic'] == 'Senior Management') & 
             (df['Indicator'].str.contains("Share of female senior managers", case=False, na=False))]

    # === Bar Chart ===
    grouped = dff.groupby("Indicator Categories")["Value"].mean().reset_index()
    bar_fig = {
        "data": [{
            "x": grouped["Indicator Categories"],
            "y": grouped["Value"],
            "type": "bar",
            "name": "Women (%)"
        }],
        "layout": {
            "title": f"% of Women in Senior Roles – {country}",
            "yaxis": {"title": "Percentage"},
            "xaxis": {"title": "Role"}
        }
    }

    # === Time Series Chart ===
    if dff.empty:
        trend_fig = {
            "layout": {
                "title": f"No time series data for {country}",
                "xaxis": {"visible": False},
                "yaxis": {"visible": False},
                "annotations": [{
                    "text": "No data available",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 16}
                }]
            }
        }
    else:
        trend_data = []
        for role in dff["Indicator Categories"].dropna().unique():
            role_data = dff[dff["Indicator Categories"] == role].groupby("Year")["Value"].mean().reset_index()
            trend_data.append({
                "x": role_data["Year"],
                "y": role_data["Value"],
                "type": "line",
                "name": role
            })

        trend_fig = {
            "data": trend_data,
            "layout": {
                "title": f"Women in Senior Roles Over Time – {country}",
                "yaxis": {"title": "% of Women"},
                "xaxis": {"title": "Year"}
            }
        }

    return bar_fig, trend_fig

@app.callback(
    Output('innovation-tech-bar', 'figure'),
    Output('innovation-trend-line', 'figure'),
    Output('innovation-sector', 'options'),
    Input('innovation-country', 'value'),
    Input('innovation-sector', 'value')
)
def update_innovation_charts(country, selected_sector):
    dff = df[(df['Country'] == country) & 
             (df['Topic'] == 'Innovation') & 
             (df['Indicator'].str.contains("female inventors", case=False, na=False))]

    # Build sector dropdown options dynamically
    sector_options = [{'label': 'All', 'value': 'All'}]
    sector_options += [{'label': tech, 'value': tech} for tech in sorted(dff['Technology or Sector'].dropna().unique())]

    # Apply sector filter if not 'All'
    if selected_sector != 'All':
        dff = dff[dff['Technology or Sector'] == selected_sector]

    # === Bar Chart: % Female Inventors by Technology ===
    tech_grouped = dff.groupby("Technology or Sector")["Value"].mean().reset_index()

    tech_bar_fig = {
        "data": [{
            "x": tech_grouped["Technology or Sector"],
            "y": tech_grouped["Value"],
            "type": "bar",
            "name": "Female Inventors (%)"
        }],
        "layout": {
            "title": f"% Female Inventors by Technology – {country}",
            "yaxis": {"title": "% Female Inventors"},
            "xaxis": {"title": "Technology", "tickangle": -45}
        }
    }

    # === Line Chart: % Female Inventors Over Time ===
    if dff.empty:
        trend_fig = {
            "layout": {
                "title": f"No innovation data for {country}",
                "xaxis": {"visible": False},
                "yaxis": {"visible": False},
                "annotations": [{
                    "text": "No data available",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 16}
                }]
            }
        }
    else:
        trend_grouped = dff.groupby("Year")["Value"].mean().reset_index()

        trend_fig = {
            "data": [{
                "x": trend_grouped["Year"],
                "y": trend_grouped["Value"],
                "type": "line",
                "name": "% Female Inventors",
                "line": {"color": "green"}
            }],
            "layout": {
                "title": f"% Female Inventors Over Time – {country} ({selected_sector})",
                "yaxis": {"title": "% Female Inventors"},
                "xaxis": {"title": "Year"}
            }
        }

    return tech_bar_fig, trend_fig, sector_options

@app.callback(
    Output('entrepreneurship-sector-bar', 'figure'),
    Output('entrepreneurship-trend-line', 'figure'),
    Input('entrepreneurship-country', 'value')
)
def update_entrepreneurship_charts(country):
    dff = df[(df['Country'] == country) & 
             (df['Topic'] == 'Entrepreneurship') & 
             (df['Indicator'].str.contains("gender diverse", case=False, na=False))]

    # === Bar Chart: % Gender-Diverse Founders by Sector ===
    sector_grouped = dff.groupby("Technology or Sector")["Value"].mean().reset_index()

    sector_bar_fig = {
        "data": [{
            "x": sector_grouped["Technology or Sector"],
            "y": sector_grouped["Value"],
            "type": "bar",
            "name": "Gender-Diverse Founders (%)"
        }],
        "layout": {
            "title": f"% Gender-Diverse Founders by Sector – {country}",
            "yaxis": {"title": "% Gender-Diverse Founders"},
            "xaxis": {"title": "Sector", "tickangle": -45}
        }
    }

    # === Line Chart: % Gender-Diverse Founders Over Time ===
    if dff.empty:
        trend_fig = {
            "layout": {
                "title": f"No entrepreneurship data for {country}",
                "xaxis": {"visible": False},
                "yaxis": {"visible": False},
                "annotations": [{

                    "text": "No data available",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 16}
                }]
            }
        }
    else:
        trend_grouped = dff.groupby("Year")["Value"].mean().reset_index()

        trend_fig = {
            "data": [{
                "x": trend_grouped["Year"],
                "y": trend_grouped["Value"],
                "type": "line",
                "name": "% Gender-Diverse Founders",
                "line": {"color": "purple"}
            }],
            "layout": {
                "title": f"% Gender-Diverse Founders Over Time – {country}",
                "yaxis": {"title": "% Gender-Diverse Founders"},
                "xaxis": {"title": "Year"}
            }
        }

    return sector_bar_fig, trend_fig

@app.callback(
    Output('explorer-indicator', 'options'),
    Output('explorer-indicator', 'value'),
    Input('explorer-country', 'value'),
    Input('explorer-topic', 'value')
)
def update_explorer_indicator_options(country, topic):
    dff = df[(df['Country'] == country) & (df['Topic'] == topic)]
    indicator_options = sorted(dff['Indicator'].dropna().unique())

    options = [{'label': ind, 'value': ind} for ind in indicator_options]

    # Auto-select the first indicator by default
    value = indicator_options[0] if indicator_options else None

    return options, value
@app.callback(
    Output('explorer-trend-line', 'figure'),
    Input('explorer-country', 'value'),
    Input('explorer-topic', 'value'),
    Input('explorer-indicator', 'value')
)
def update_explorer_trend(country, topic, indicator):
    dff = df[(df['Country'] == country) & 
             (df['Topic'] == topic) & 
             (df['Indicator'] == indicator)]

    if dff.empty or indicator is None:
        fig = {
            "layout": {
                "title": "No data available",
                "xaxis": {"visible": False},
                "yaxis": {"visible": False},
                "annotations": [{
                    "text": "No data available",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 16}
                }]
            }
        }
    else:
        grouped = dff.groupby("Year")["Value"].mean().reset_index()

        fig = {
            "data": [{
                "x": grouped["Year"],
                "y": grouped["Value"],
                "type": "line",
                "name": indicator,
                "line": {"color": "orange"}
            }],
            "layout": {
                "title": f"{indicator} Over Time – {country} ({topic})",
                "yaxis": {"title": indicator},
                "xaxis": {"title": "Year"}
            }
        }

    return fig

@app.callback(
    Output('advanced-kpi-senior-roles', 'children'),
    Output('advanced-kpi-female-inventors', 'children'),
    Output('advanced-kpi-wage-gap', 'children'),
    Output('advanced-kpi-diverse-founders', 'children'),
    Input('explorer-country', 'value')  # Trigger update
)
def update_advanced_insights(_):
    # Define valid countries — based on IEA dataset
    VALID_COUNTRIES = ['Austria', 'France', 'Germany', 'Portugal', 'Spain']

    # === Women in Senior Roles ===
    senior = df[(df['Topic'] == 'Senior Management') &
                (df['Indicator'].str.contains("Share of female senior managers", case=False, na=False))]
    senior = senior[senior['Country'].isin(VALID_COUNTRIES)]
    senior_grouped = senior.groupby('Country').agg(
        mean_value=('Value', 'mean'),
        count=('Value', 'count')
    ).reset_index()
    senior_filtered = senior_grouped[senior_grouped['count'] >= 5]
    if not senior_filtered.empty:
        best_senior = senior_filtered.sort_values(by='mean_value', ascending=False).iloc[0]
        senior_text = f"🏆 Country with Highest % Women in Senior Roles: {best_senior['Country']} ({best_senior['mean_value']:.2f}%)"
    else:
        senior_text = "🏆 No country with sufficient data for Senior Roles"

    # === Female Inventors ===
    inventors = df[(df['Topic'] == 'Innovation') &
                   (df['Indicator'].str.contains("female inventors", case=False, na=False))]
    inventors = inventors[inventors['Country'].isin(VALID_COUNTRIES)]
    inventors_grouped = inventors.groupby('Country').agg(
        mean_value=('Value', 'mean'),
        count=('Value', 'count')
    ).reset_index()
    inventors_filtered = inventors_grouped[inventors_grouped['count'] >= 5]
    if not inventors_filtered.empty:
        best_inventors = inventors_filtered.sort_values(by='mean_value', ascending=False).iloc[0]
        inventors_text = f"💡 Country with Highest % Female Inventors: {best_inventors['Country']} ({best_inventors['mean_value']:.2f}%)"
    else:
        inventors_text = "💡 No country with sufficient data for Female Inventors"

    # === Largest Gender Wage Gap (most negative) ===
    wage = df[(df['Topic'] == 'Employment') &
              (df['Indicator'].str.contains("wage gap", case=False, na=False))]
    wage = wage[wage['Country'].isin(VALID_COUNTRIES)]
    wage_grouped = wage.groupby('Country').agg(
        mean_value=('Value', 'mean'),
        count=('Value', 'count')
    ).reset_index()
    wage_filtered = wage_grouped[wage_grouped['count'] >= 5]
    if not wage_filtered.empty:
        worst_wage_gap = wage_filtered.sort_values(by='mean_value', ascending=True).iloc[0]
        wage_text = f"⚠️ Country with Largest Gender Wage Gap: {worst_wage_gap['Country']} ({worst_wage_gap['mean_value']:.2f}%)"
    else:
        wage_text = "⚠️ No country with sufficient data for Wage Gap"

    # === Gender-Diverse Founders ===
    founders = df[(df['Topic'] == 'Entrepreneurship') &
                  (df['Indicator'].str.contains("gender diverse", case=False, na=False))]
    founders = founders[founders['Country'].isin(VALID_COUNTRIES)]
    founders_grouped = founders.groupby('Country').agg(
        mean_value=('Value', 'mean'),
        count=('Value', 'count')
    ).reset_index()
    founders_filtered = founders_grouped[founders_grouped['count'] >= 5]
    if not founders_filtered.empty:
        best_founders = founders_filtered.sort_values(by='mean_value', ascending=False).iloc[0]
        founders_text = f"🚀 Country with Highest % Gender-Diverse Founders: {best_founders['Country']} ({best_founders['mean_value']:.2f}%)"
    else:
        founders_text = "🚀 No country with sufficient data for Gender-Diverse Founders"

    # Return all KPI texts
    return senior_text, inventors_text, wage_text, founders_text





if __name__ == '__main__':
    app.run(debug=True)


