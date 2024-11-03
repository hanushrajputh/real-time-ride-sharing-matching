# Real-Time Ride-Sharing Matching System
Project Description
This project is a real-time ride-sharing matching system, inspired by popular ride-sharing platforms like Uber and Lyft. The goal is to efficiently match drivers with riders based on proximity and availability, minimizing wait times for riders and idle times for drivers. The system utilizes data structures and algorithms such as geohashing, graph-based shortest path calculation, and priority queues to achieve optimal matching in real-time.

## Key components include:

Graph Representation: Models the road network for route calculations.


Geohashing: Quickly identifies nearby drivers within a radius.

Priority Queue Matching: Selects the best match for each rider based on location and other criteria.
This project demonstrates the use of real-time data structures and algorithms to solve real-world matching and routing challenges in a highly scalable manner.

Installation Instructions
Prerequisites
Ensure that Python 3.7+ is installed on your system. You can install necessary dependencies by following these steps:

### Clone the repository:


git clone https://github.com/hanushrajputh/real-time-ride-sharing-matching.git  
cd real-time-ride-sharing-matching  

### Install required packages:


pip install -r requirements.txt 

Requirements

* numpy: For numerical calculations.  
* pandas: For data manipulation.  
* networkx: To manage the road network graph.  
* geopy: For geographic distance calculations.  

These dependencies are listed in the requirements.  txt file and can be installed as shown above.

## How to Run the Program
Start the Application

Run the main program to start matching drivers with riders:  
python src/main.py  

## Sample Data

Sample data for drivers and riders is provided in the data/ folder. Modify these files or create new ones to test different scenarios.


## Running the Tests
To run tests for each module, execute the following command from the project root directory:  

python -m unittest discover -s tests  
This will run all test cases in the tests/ folder to verify the functionality of each component.

## File and Module Overview  

### Root Directory  

README.md: Project documentation, including an overview, setup instructions, and usage.  

requirements.txt: List of Python packages required to run the project.  

## Folders and Files  
#### data/: Contains sample data for testing.  

drivers.csv: Sample data representing driver locations.  
riders.csv: Sample data representing rider locations.  
#### src/: Contains the main source code for the system.

* main.py: The main program that ties all components together to start matching riders with drivers.  

* graph.py: Defines the RoadGraph class, which models the road network as a graph structure and calculates the shortest path between locations.  

* geohashing.py: Contains the GeoHashing class, responsible for converting latitude/longitude coordinates to geohashes and finding nearby geohashes for efficient spatial indexing.  

* matching.py: Implements the Matcher class, which manages driver and rider matching using a priority queue.  

* utils.py: Contains helper functions used across different modules.  

#### tests/: Contains unit tests for each module.

* test_graph.py: Tests for graph.py and road network operations.  

* test_geohashing.py: Tests for geohashing and proximity functions.  

* test_matching.py: Tests for the matching algorithm used in matching.py.

* test_utils.py: Tests for utility functions.
