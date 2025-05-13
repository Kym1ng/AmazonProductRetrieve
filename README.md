# AmazonProductRetrieve
# Distributed Databases for Amazon Products

## Project Overview

This project focuses on building a distributed database system for Amazon product information using MongoDB. The system is designed for optimal performance and scalability, leveraging hashing for data distribution across multiple database nodes. It includes interfaces for both database managers (with CRUD operations) and end-users (for searching and viewing products).

## Features

* **Data Cleaning and Loading:** Processes and combines raw product data and metadata into a clean dataset ready for storage.
* **Distributed Database with Sharding:** Implements data distribution across multiple MongoDB nodes using a hashing strategy based on the product ASIN.
* **Backup and Recovery Mechanism:** Includes a dedicated database node for backup and robust failover.
* **Database Manager Interface (Tkinter):** Provides a graphical interface for administrators to perform Create, Read, Update, and Delete (CRUD) operations on the product data.
* **User-Facing Web Interface (Streamlit):** Offers an intuitive web interface for users to search and filter product information based on various criteria (title, brand, price range).

## Architecture

The system architecture involves:

1.  **Data Preprocessing:** Raw datasets are cleaned and combined to form a final dataset.
2.  **Data Storage:** The final dataset is stored locally in a distributed MongoDB database.
3.  **Data Distribution:** Hashing techniques on the 'asin' are used to shard data across primary database nodes.
4.  **Interfaces:**
    * A Data Manager Interface (Tkinter) interacts with MongoDB for CRUD operations.
    * A User Interface (Streamlit) queries data from MongoDB and presents it to users via a web application.
    * A dedicated node is used for backup and recovery.

(You could potentially add a simplified version of the architecture flowchart from your report here or link to it).

## Technology Stack

* **Database:** MongoDB (Distributed, NoSQL)
* **Backend/Data Processing:** Python (with libraries like pandas and PyMongo)
* **Database Manager UI:** Tkinter (Python GUI toolkit)
* **User Web UI:** Streamlit (Python framework for building web applications)

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Prerequisites:**
    * Install Python (3.x recommended).
    * Install MongoDB and set up your distributed database environment (including sharding and the backup node) as per your project's design.
    * Ensure Git and Git LFS are installed.

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Kym1ng/AmazonProductRetrieve.git
    cd AmazonProductRetrieve
    ```

3.  **Install Dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    # Create a virtual environment
    python -m venv venv
    # Activate the virtual environment
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    # venv\Scripts\activate
    # Install Python packages (Create a requirements.txt file first if you don't have one)
    pip install -r requirements.txt
    ```
    *(You'll need to create a `requirements.txt` file listing all the Python libraries your project uses, e.g., `pymongo`, `pandas`, `tkinter`, `streamlit`, `hashlib`).*

4.  **Handle Large Data Files (using Git LFS):**
    This repository contains large data files (`data/AMAZON_FASHION.json`, `data/meta_AMAZON_FASHION.json`) that are tracked using Git LFS. Make sure Git LFS is installed (`git lfs install`) after cloning. The files should be downloaded automatically during the clone, but if not, you might need to run `git lfs pull`.

5.  **Load & Clean the Data(You Dont Need This since We Did It Already):**
    Run the Python script responsible for data cleaning, processing, and loading data into your configured MongoDB database.
    *(Provide instructions or command to run your data loading script, e.g., `python data/Data Cleaning.ipynb`)*

6.  **Run the Database Manager Interface:**
    *(Provide instructions or command to run your Tkinter application, e.g., `python Py/database_manager_final.ipynb`)*

7.  **Run the User Web Interface:**
    *(Provide instructions or command to run your Streamlit application, e.g., `streamlit run Py/StreamlitUI.py`)*

## Usage

* **Database Manager Interface:** Use the Tkinter application to perform CRUD operations (Insert, Read, Update, Delete) on the product database. You can generate new ASINs for insertions and search by ASIN for other operations.
* **User Web Interface:** Access the Streamlit application via your web browser (the address will be provided when you run the Streamlit command). Use the search bar and filters (title, brand, price range) to query and view product information.

## Data

The project utilizes two main datasets, which are combined and cleaned:
* Amazon Fashion JSON file
* Related metadata from a CSV file

The data undergoes cleaning steps including formatting 'rank', handling missing 'price' values, and cleaning 'feature' and 'title' fields.

## Contributors

* Erkang Chen (Data searching, cleaning, and uploading to MongoDB)
* Haoming Guo (Hash function design, User-facing web interface)
* Mingji Xi (Database Manager Interface for CRUD process)
* All team members participated in the demo, video recording, and final report writing.

## Future Scope

Potential future improvements include:
* Enhancing the user interface with more intuitive features, responsive design, and personalized recommendations.
* Implementing real-time data processing for dynamic updates.
* Integrating machine learning techniques for predictive analytics and sentiment analysis.

## License

*(Add information about your project's license here, e.g., MIT, Apache 2.0, etc.)*