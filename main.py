import glob
import os
import streamlit as st

# 1. Automatically grab every single python file in your root folder
all_python_files = sorted(glob.glob("*.py"))

pages = []
for file in all_python_files:
    # 2. Skip main.py so the router script doesn't recursively load itself
    if file == "main.py":
        continue
        
    # 3. Convert filenames cleanly into sidebar titles
    # Example: "fourier_square.py" -> "Fourier Square"
    base_name = os.path.splitext(file)[0]
    clean_title = base_name.replace("_", " ").title()
    
    # 4. Register the file as a dynamic page
    pages.append(st.Page(file, title=clean_title))

# 5. Build and run the automated navigation layout
if pages:
    st.navigation(pages).run()
else:
    st.title("Welcome to your Dashboard")
    st.info("Drop any Python graph file into this directory and it will appear here automatically!")