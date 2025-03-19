# drhorrible

This project was done based on a dataset of different cars in the United States. Descriptions include the price of the vehicle, model, type of car, odometer reading, how many days it's been listed, and its condition. These cars were listed for sale in a car advertisement and the goal of my project was to show interesting correlations in the data and then upload it as a web service

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




