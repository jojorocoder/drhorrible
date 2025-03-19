# drhorrible

This project was done based on a dataset of different cars in the United States. Descriptions include the price of the vehicle, model, type of car, odometer reading, how many days it's been listed, and its condition. These cars were listed for sale in a car advertisement and the goal of my project was to show interesting correlations in the data and then upload it as a web service. This repository contains the streamlit files that make it compatible with render which I uploaded this project to. It also contains my virtual environment (.venv) which I used to code everything. It also contains a notebook that contains general exploratory data analysis with histograms and scatter plots to describe interesting trends with the data. The app.py file contains the code to launch the app via streamlit. The requirements.txt is what you will need to install in order to run this app properly and the vehicles_us.csv is the dataframe that I used to base this project off of. Below I will explain the processes and setup for the app.

Methods and libraries used include pandas, numpy, and plotly express. The dataset was fairly simple to clean up, as there were not too many issues initially. I did not have to deal with duplicate values and only had to sift through missing values. This included ensuring that removing or replacing those missing values was safe for the data.

Setup Instructions:

To launch the project, follow these steps:

Clone the repository:

git clone https://github.com/jojorocoder/drhorrible.git

cd drhorrible

Create and activate a virtual environment (optional but recommended):


python -m venv venv

source venv/bin/activate   # On macOS/Linux

venv\Scripts\activate      # On Windows

Install dependencies from requirements.txt:


pip install -r requirements.txt

streamlit run app.py  


This project has been deployed on Render.com. You can view it here:

🔗 https://drhorriblecars.onrender.com




