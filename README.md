# Twitter Automation with Crew AI

This repository contains an advanced Twitter automation project built using Crew AI. It utilizes multiple AI agents to autonomously monitor and interact with AI-related content on Twitter. The agents perform various actions, including liking, replying, and retweeting posts related to AI, ensuring each interaction is contextually relevant.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Model Details](#model-details)
4. [AI Agents](#ai-agents)
5. [Logging and Reporting](#logging-and-reporting)
6. [Folder Structure](#folder-structure)
7. [Getting Started](#getting-started)
8. [Usage](#usage)

---

## Project Overview

This project creates a multi-AI-agent system that monitors, curates, and interacts with Twitter content related to artificial intelligence. The system reads from a dummy dataset (`dummy_tweets.json`) and interacts with posts in the following ways:
- **Feeds**: Checks for trending AI-related content.
- **Interactions**: Likes, replies, and retweets relevant tweets.
- **Context Relevancy**: Ensures all replies align with the tone and context of the original tweet.
- **Logging**: Keeps records of every interaction for transparency and analysis.

---

## Tech Stack

- **Crew AI**: Agent orchestration and task management
- **Serper API**: Used for web searches related to trending AI news
- **Programming Language**: Python

## Model Details

The following models are used in this project:

1. **Ollama 3.1 (8B)**: For general interaction and monitoring tasks.
2. **Mistral 7B**: Supports complex language generation and comprehension tasks.
3. **Gemma 2-9B-IT**: Serves as the main LLM for conversation and contextual analysis.
4. **Text Embedding 3 Small (Dimension 1536)**: Used for embedding tasks, such as similarity and context-checking.

## AI Agents

The following agents are set up in the project, each designed for specific tasks:

1. **Feed Scanning Agent**  
   - **Purpose**: Scans Twitter feed at intervals to curate relevant AI-related posts.
   - **Output**: A list of 6-7 highly relevant tweets.

2. **Interaction Agent**  
   - **Purpose**: Likes, replies, or retweets selected tweets.
   - **Output**: Logs of each interaction action (like, reply, comment) taken, saved in `report.md`.

3. **Context Relevancy Check Agent**  
   - **Purpose**: Verifies that replies match the tone and context of the original post.
   - **Output**: Filters non-relevant responses.

4. **Mention Response Agent**  
   - **Purpose**: Engages selectively with mentions to keep interactions consistent.
   - **Output**: Logs responses to mentions.

5. **Conversation Management Agent** (Optional)  
   - **Purpose**: Monitors and concludes prolonged conversations to prevent over-engagement.

6. **Conversational Length Manager**  
   - **Purpose**: Manages the length of conversations to ensure they remain succinct and relevant.

7. **Tool for Checking Mentions**  
   - **Purpose**: Monitors and responds to mentions effectively.

---

## Logging and Reporting

Logs are generated in two primary files:
- **logs.txt**: Contains raw logs whenever an agent tweets, likes, or replies.
- **report.md**: Contains detailed reports for each interaction, outlining the action taken by the `Interaction Agent` (like, reply, or comment) with specifics on each action.

## Folder Structure

```plaintext
.
├── dummy_tweets.json       # Sample dataset of tweets for testing
├── logs.txt                # Log file with all interaction records
├── report.md               # Detailed report on each interaction action
├── scripts/                # Contains agent scripts and task definitions
└── README.md               # Project documentation
