# Global News Verification Platform for IOM

## Project Overview

This project, the Global News Verification Platform, is an AI-driven tool designed to aid the International Organization for Migration (IOM) in rapidly gathering and summarizing multilingual news. The goal is to provide quick and accurate insights into global events involving migrants, tailored to the IOM’s data verification needs.

The platform features an innovative pipeline that automates the search and synthesis of news articles from around the world, clustering similar events based on user-provided themes, such as migrant incidents.

![Global News Verification Platform Pipeline](Screenshot_2024-04-28_at_19.33.58.png)

## Features

- **GPT Query Generator**: Accepts user input on a specific theme and crafts structured queries for news aggregation.
- **Google News Scraper**: Uses the generated queries to scrape news articles across selected languages and regions.
- **Data Extractor Model**: Extracts relevant details from the collected news articles for further processing.
- **Clustering Algorithm**: Groups similar news events together, sorting through noise and focusing on the incident's core facts.
- **Results Visualization**: Presents a consolidated view of the verified news events, enabling users to quickly grasp the essence of each incident.

## Usage

1. Launch the web app built with React.
2. Enter the details of a global event, such as “Five migrants found dead off the coast of Tunisia”.
3. Select the desired languages and news regions for your search.
4. Submit the query to initiate the pipeline.
5. Review the visualized results, which consolidate similar news events into a coherent summary.

## Installation

Provide step-by-step instructions on how to get a development environment running, including:

```bash
# Clone the repository
git clone https://github.com/RasanYo/MissingMigrants.git

# Navigate to the project directory
cd MissingMigrants

# Install dependencies
npm install

# Start the development server
npm start
```

## Technology Stack

- React.js for frontend web application
- Node.js for backend services
- Open AI api for LLM generated content
- Google News api for web scraping
