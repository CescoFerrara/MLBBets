import requests
import pandas as pd
import sqlite3
import MLBStatsAPIClient

base_url = "https://statsapi.mlb.com/api"

client = MLBStatsAPIClient()

print(client.baseurl)