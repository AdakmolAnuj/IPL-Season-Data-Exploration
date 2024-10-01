import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
print(os.getcwd())

# Step 1: Read the dataset
data = pd.read_csv("IPL2022.csv")

# Step 2: Analyze the number of matches won by each team
figure1 = px.bar(data, x=data["match_winner"],
            title="Number of Matches Won in IPL 2022")
figure1.show()

# Step 3: Analyze matches won by defending or chasing
data["won_by"] = data["won_by"].map({"Wickets": "Chasing", 
                                     "Runs": "Defending"})
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold','lightgreen']
figure2 = go.Figure(data=[go.Pie(labels=label, values=counts)])
figure2.update_layout(title_text='Number of Matches Won By Defending Or Chasing')
figure2.update_traces(hoverinfo='label+percent', textinfo='value', 
                      textfont_size=30,
                      marker=dict(colors=colors, 
                                  line=dict(color='black', width=3)))
figure2.show()

# Step 4: Analyze toss decisions
toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']
figure3 = go.Figure(data=[go.Pie(labels=label, values=counts)])
figure3.update_layout(title_text='Toss Decision')
figure3.update_traces(hoverinfo='label+percent', 
                      textinfo='value', textfont_size=30,
                      marker=dict(colors=colors, 
                                  line=dict(color='black', width=3)))
figure3.show()

# Step 5: Analyze top scorers
figure4 = px.bar(data, x=data["top_scorer"],
            title="Top Scorers in IPL 2022")
figure4.show()

# Step 6: Analyze high scores
figure5 = px.bar(data, x=data["top_scorer"], 
                y = data["highscore"], 
                color = data["highscore"],
            title="Top Scorers in IPL 2022")
figure5.show()

# Step 7: Analyze player of the match awards
figure6 = px.bar(data, x = data["player_of_the_match"], 
                title="Most Player of the Match Awards")
figure6.show()

# Step 8: Analyze best bowlers
figure7 = px.bar(data, x=data["best_bowling"],
            title="Best Bowlers in IPL 2022")
figure7.show()

# Step 9: Analyze wickets fall while setting or chasing target
figure8 = go.Figure()
figure8.add_trace(go.Bar(
    x=data["venue"],
    y=data["first_ings_wkts"],
    name='First Innings Wickets',
    marker_color='gold'
))
figure8.add_trace(go.Bar(
    x=data["venue"],
    y=data["second_ings_wkts"],
    name='Second Innings Wickets',
    marker_color='lightgreen'
))
figure8.update_layout(barmode='group', xaxis_tickangle=-45)
figure8.show()
