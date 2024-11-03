from src.graph import RoadGraph
from src.geohashing import GeoHashing
from src.matching import Matcher
import pandas as pd

def main():
    # Initialize components
    road_graph = RoadGraph()
    matcher = Matcher()
    
    # Load driver data
    drivers = pd.read_csv('data/drivers.csv')
    for _, row in drivers.iterrows():
        matcher.add_driver(row['id'], (row['latitude'], row['longitude']))
        
    # Load rider data
    riders = pd.read_csv('data/riders.csv')
    for _, row in riders.iterrows():
        matched_driver = matcher.match_rider((row['latitude'], row['longitude']))
        print(f"Rider {row['id']} matched with Driver: {matched_driver}")

if __name__ == "__main__":
    main()
