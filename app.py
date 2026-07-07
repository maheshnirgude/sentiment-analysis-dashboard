import pandas as pd
import streamlit as st
from sentiment import analyze

st.set_page_config(page_title="Sentiment Dashboard", layout="wide")
st.title("Customer Review Sentiment")

uploaded = st.file_uploader("Upload a CSV with a 'review' column", type="csv")
sample = st.button("Use sample data")

if uploaded or sample:
    df = pd.read_csv(uploaded) if uploaded else pd.read_csv("sample_reviews.csv")
    df["sentiment"] = df["review"].astype(str).map(lambda r: analyze(r)["label"])
    df["score"] = df["review"].astype(str).map(lambda r: analyze(r)["score"])

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Distribution")
        st.bar_chart(df["sentiment"].value_counts())
    with col2:
        st.subheader("Most negative")
        st.dataframe(df.nsmallest(5, "score")[["review", "score"]])

    st.subheader("All reviews")
    st.dataframe(df)
