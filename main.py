import streamlit as st
import subprocess
import os

st.title("Oil Painting Executor")

def run_oil_painting():
    # Construct the command to run the script with arguments
    command = ['py', 'Oil-Painting.py', '--f', '44a.jpg', '--p', '4']
    # Execute the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    return result

if st.button("Start"):
    st.write("Running Oil-Painting.py...")
    result = run_oil_painting()
    
    # Check if the process executed successfully
    if result.returncode == 0:
        st.success("Done successfully!")
        
        # Define the path to the final image
        final_image_path = os.path.join("output", "44a-p-4", "Final_Result.png")
        
        # Check if the image exists, then display it
        if os.path.exists(final_image_path):
            st.image(final_image_path, caption="Final Result", use_column_width=True)
        else:
            st.error(f"Final image not found at {final_image_path}")
    else:
        st.error("There was an error running the script.")
        st.error(f"Error details: {result.stderr}")
