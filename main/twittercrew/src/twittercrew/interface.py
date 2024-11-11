#!/usr/bin/env python
import streamlit as st
import subprocess
from crew import TwittercrewCrew
import time
import os

# error fixing for streamlit cloud for sqlite
__import__('pysqlite3')
import sys 
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3

# Define the main Streamlit function
def main():
    st.title("🚀 Twitter Crew AI Project Interface")
    st.subheader("Autonomously Engage with AI-Related Tweets")
    st.markdown("""
        This interface allows you to run the Crew AI project and view real-time interactions, including tweet likes, replies, and retweets.
        The **report.md** file will update with all interactions for easy review.
    """)

    # Button to kick off the Crew AI
    if st.button("Kick Off Crew AI"):
        st.write("Starting the Crew AI...")
        kickoff_crew()

    # Display log updates from report.md
    st.subheader("🔍 Real-Time Activity Report")
    report_display = st.empty()

    # Continuously read and render Markdown content from report.md
    if os.path.exists("report.md"):
        while True:
            # Read the contents of report.md and render it as Markdown
            with open("report.md", "r") as report_file:
                markdown_content = report_file.read()
                report_display.markdown(markdown_content, unsafe_allow_html=True)
            # Refresh content every few seconds
            time.sleep(2)

def kickoff_crew():
    """
    Function to initialize and kick off the Crew AI.
    """
    try:
        # Run the Crew AI kickoff
        TwittercrewCrew().crew().kickoff()
        # Log to report.md to indicate start
        with open("report.md", "a") as report_file:
            report_file.write("# Crew AI initiated...\n")
        st.success("Crew AI started successfully!")
    except Exception as e:
        st.error(f"Error starting Crew AI: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
