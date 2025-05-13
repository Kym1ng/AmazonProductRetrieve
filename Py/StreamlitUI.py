# import the necessary libraries
import streamlit as st
from pymongo import MongoClient

# Create a connection to the MongoDB database
client = MongoClient(host="localhost", port=27017)
client = MongoClient('mongodb://localhost:27017/')

# collection name list
db_list = ['db_1', 'db_2', 'db_3']


# Create a new database and collection
db_backup = client['db_backup']

# Create a new collection
collection_backup = db_backup['collection_backup']

# Set the page configuration
st.set_page_config(
    page_title="Amazon Product Database",
    page_icon=":shopping_cart:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Set the background color of the page with CSS
page_bg_color = """
<style>
body {
    background-color: #f0f0f0;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Title and subtitle in the center of the page using HTML
st.write("""
<div style='text-align: center; background-color: #e6e6e6; padding: 20px; border-radius: 10px;'>
    <h1 style='color: #333333;'>Amazon Product Database</h1>
</div>
""", unsafe_allow_html=True)

# define the input blcok to insert data for query conditions
search_title_input = st.text_input("Enter products title to find:")
search_brand_input = st.text_input("Enter products brands to find:")

# Slider for price range selection
# Retrieve the minimum and maximum price from the collection
price_range_data = collection_backup.aggregate([
    {
        "$group": {
            "_id": None,  # Grouping all documents together
            "min_price": {"$min": "$price"},  # Get the minimum price in the collection
            "max_price": {"$max": "$price"}   # Get the maximum price in the collection
        }
    }
])
# Extract the price range data from the aggregation result
try:
    price_data = next(price_range_data)
    min_price = price_data["min_price"]
    max_price = price_data["max_price"]
except StopIteration:
    # Default price range if the collection is empty or the prices are not set
    min_price, max_price = 0, 100

# Define the price range slider
price_range = st.slider('Select a price range:', min_value=min_price, max_value=max_price, value=(min_price, max_price))

# Define the search button
search_button = st.button("Search", use_container_width=True, help="Click to search for products")

# Custom CSS for the button
button_css = """
<style>
div.stButton > button:first-child {
    background-color: #ff9900;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    padding: 10px 20px;
}
div.stButton > button:first-child:hover {
    background-color: #e68a00;
}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)

# Handle button click event
if search_button:
    # Start with the price range condition
    query_conditions = [{"price": {"$gte": price_range[0], "$lte": price_range[1]}}]

    # Add title or brand to the query conditions if they are not empty
    if search_title_input and search_brand_input:
        # If both fields have input, search for matches in either field
        query_conditions.append({"$and": [
            {"title": {"$regex": search_title_input, "$options": "i"}},
            {"brand": {"$regex": search_brand_input, "$options": "i"}}
        ]})
    elif search_title_input:
        # If only title has input, search only by title
        query_conditions.append({"title": {"$regex": search_title_input, "$options": "i"}})
    elif search_brand_input:
        # If only brand has input, search only by brand
        query_conditions.append({"brand": {"$regex": search_brand_input, "$options": "i"}})

    # Combine all the conditions using the AND operator
    query_filter = {"$and": query_conditions}

    # MongoDB query to find products within selected price range and title containing search input
    results = collection_backup.find(query_filter)
    results_count = collection_backup.count_documents(query_filter)

# Use an expander to show the results
    with st.expander("See Results"):

        # Display the results if any are found
        if results_count == 0:
            st.info("No results found for the given criteria.")
            
        # Display the results if any are found
        else:
            st.write(f"Results found: {results_count}")
            for item in results:
                # Display the title, brand, and price of the product
                st.markdown(f"### **{item.get('title', 'No Title')}**")
                st.markdown(f"**Brand:** {item.get('brand', 'No Brand')}")
                st.markdown(f"**Price:** {item.get('price', 'No Price')}")

                # Get the features from the item
                features = item.get('feature', [])
                if not isinstance(features, list):
                    features = features.split(',')  # Split by comma or your chosen separator
                    
                # If there are features, display them as bullet points
                if features:
                    st.markdown("**Features:**")  # Title for the features list
                    for feature in features:
                        st.markdown(f"- {feature.strip()}")

                # Get the image URLs from the item
                image_urls = item.get('imageURL', [])

                # Check if there are any image URLs present
                if image_urls:
                    # If you want to display the first image only:
                    st.image(image_urls[0], caption=item.get('title', 'No Title'), width=150)




