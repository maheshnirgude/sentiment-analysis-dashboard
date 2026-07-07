# Sentiment Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## Overview

The Sentiment Analysis Dashboard is a lightweight Streamlit application designed to classify and visualize the sentiment of text reviews. Utilizing a lexicon-based model, this dashboard provides immediate insights into sentiment distribution without relying on heavy machine learning dependencies. It offers a clear, interactive way to understand customer feedback or textual data sentiment at a glance.

## Features

*   **Lexicon-based Sentiment Classification:** Employs a rule-based approach for rapid sentiment analysis, categorizing text as positive, neutral, or negative.
*   **Interactive Streamlit Dashboard:** Provides a user-friendly web interface for seamless interaction and data exploration.
*   **Sentiment Distribution Visualization:** Clearly presents the proportion of positive, neutral, and negative sentiments using intuitive charts.
*   **Lightweight & Efficient:** Designed for quick deployment and minimal computational overhead, avoiding complex ML frameworks.
*   **Customizable Review Input:** Supports analysis of pre-loaded sample data or user-uploaded CSV files containing text reviews.

## Tech Stack

| Technology    | Description                                            |
| :------------ | :----------------------------------------------------- |
| Python        | Core programming language for the application logic.   |
| NLP           | Natural Language Processing techniques for text analysis. |
| Streamlit     | Framework for rapidly building interactive web applications. |
| pandas        | Powerful library for data manipulation and analysis.   |
| Data Analysis | Methodologies used for processing and interpreting sentiment data. |

## Installation

Follow these steps to get the project up and running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repository-name/sentiment-analysis-dashboard.git
    cd sentiment-analysis-dashboard
    ```
    *(Replace `your-repository-name` with the actual name of your repository if applicable.)*

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit dashboard:

```bash
streamlit run app.py

Once the application is running, your web browser will automatically open the Streamlit dashboard. You can:

*   View pre-loaded sample reviews and their sentiment analysis.
*   Upload your own CSV file containing a column of text reviews for analysis.
*   Interact with the dashboard to see the distribution of positive, neutral, and negative sentiments.

### Screenshot

*(Include a screenshot of the dashboard here)*

## Project Structure

```
.
├── app.py                  # Main Streamlit dashboard application
├── sentiment.py            # Contains the lexicon-based sentiment analysis logic
├── sample_reviews.csv      # Sample dataset for demonstration
├── test_sentiment.py       # Unit tests for the sentiment analysis module
└── requirements.txt        # Lists all Python dependencies

## Interview Q&A

Here are some realistic questions a recruiter might ask about this project, along with strong answers.

---

**Q1: Why did you choose a lexicon-based model for sentiment analysis instead of a more advanced machine learning model (e.g., logistic regression, BERT)?**

**A1:** "I opted for a lexicon-based model primarily for its simplicity, speed, and interpretability, aligning with the project's goal of creating a lightweight dashboard without heavyweight dependencies. For student projects, it demonstrates core NLP concepts effectively without requiring extensive training data or computational resources. It's also very effective for clear, unambiguous sentiment detection in common review scenarios, allowing us to focus on the Streamlit dashboard and data visualization aspects. If the project's scope were to handle more nuanced language or domain-specific jargon, a machine learning approach would be the next logical step for improved accuracy and adaptability."

---

**Q2: How would you enhance this dashboard to provide deeper insights or handle more complex sentiment nuances?**

**A2:** "To enhance it, I would implement several improvements. First, I'd integrate more sophisticated sentiment models, such as VADER for handling emojis and slang, or even fine-tuned Transformer models like BERT for deeper contextual understanding. Second, I'd introduce advanced visualizations, such as aspect-based sentiment analysis to identify sentiment towards specific product features, or dynamic word clouds highlighting key positive and negative terms. Third, I would consider adding functionality for real-time data ingestion from APIs or external sources, transforming it from a static analysis tool into a dynamic monitoring dashboard. Finally, improving the user experience with features like sentiment scoring thresholds or the ability to filter reviews by sentiment would add significant value."

---

**Q3: What were the main challenges you faced while developing this Streamlit dashboard, especially concerning data handling or visualization?**

**A3:** "One key challenge was ensuring robust error handling for user-uploaded CSV files – specifically validating column names, gracefully handling missing values, and dealing with non-textual or malformed data to prevent application crashes. Streamlit's stateless nature also required careful management of session state to maintain user interactions and data consistency across reruns without reloading the entire application. For visualization, ensuring the charts were clear, responsive, and effectively communicated the sentiment distribution, particularly when dealing with potentially imbalanced datasets, required iterative refinement and thoughtful use of libraries like Plotly or Matplotlib integrated within Streamlit's components."

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
