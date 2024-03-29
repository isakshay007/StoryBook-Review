import streamlit as st
import os
import shutil

def remove_existing_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            st.error(f"Error while removing existing files: {e}")


def get_files_in_directory(directory):
    # This function help us to get the file path along with filename.
    files_list = []

    if os.path.exists(directory) and os.path.isdir(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            if os.path.isfile(file_path):
                files_list.append(file_path)

    return files_list

def save_uploaded_file(directory, uploaded_file):
    remove_existing_files(directory=directory)
    file_path = os.path.join(directory, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.read())
    st.success("File uploaded successfully")


def reviewer(agent):
    results = {}
    prompts = {
        "Summary": "Write the summary of the story in 2 sentences",
        "Analyze": "How the author uses symbolism to enhance the story's themes",
        "Findings": "Identify key turning points or pivotal moments that drive the plot forward",
        "Discussion and Conclusions": "Reflect on the overall message or moral lesson conveyed by the story and its relevance to readers. Make a 4-5 line of response",
    }

    for heading, prompt in prompts.items():
        response = agent.query(prompt)
        results[heading] = response.response

    return results


def get_response(response:dict):
    for heading, response in response.items():
        st.subheader(heading)
        st.write(response)
        st.markdown("---")  