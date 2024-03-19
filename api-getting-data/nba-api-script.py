import pandas as pd
from nba_api.stats.endpoints import TeamInfoCommon
from nba_api.stats.static import teams
import os

# Get the list of NBA teams
nba_teams = teams.get_teams()

# Create a dictionary of team IDs
team_ids_dict = {team['full_name']: team['id'] for team in nba_teams}

# Create an empty DataFrame to store the data
df = pd.DataFrame()

# Loop through the teams and append to the df
for team_name, team_id in team_ids_dict.items():
    team_info = TeamInfoCommon(team_id=team_id)
    df_team = team_info.get_data_frames()[0]
    df_team['TeamName'] = team_name  # Adding the team name to the DataFrame
    df_team['Season'] = '2023-24'  # Adding the season to the DataFrame
    df = pd.concat([df, df_team], ignore_index=True)

# Define the directory path
directory = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'IS310-repo', 'api-getting-data', 'data')

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Save the combined DataFrame to a CSV file in the specified directory
output_file = os.path.join(directory, 'nba_teams_info.csv')
df.to_csv(output_file, index=False)

print(f"DataFrame saved to {output_file}")
