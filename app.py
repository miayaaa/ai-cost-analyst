from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent, AgentType
from dotenv import load_dotenv
import os
import re
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# ✅ Streamlit Page Configuration
st.set_page_config(
    page_title="Snowflake Cost Analyst (GenAI)", layout="centered")

# ✅ Load OpenAI API Key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Load and clean CSV data


@st.cache_data
def fetch_cost_data():
    df = pd.read_csv("cost_data.csv", parse_dates=["date"])
    df.columns = df.columns.str.strip().str.lower()
    return df


df = fetch_cost_data()

# ✅ Preview the data
with st.expander("📊 Preview Data"):
    st.dataframe(df.head())
    st.markdown("**Available columns**: `date`, `warehouse`, `credits`")

# ✅ Safely execute LLM-generated Python plotting code and return figure


def clean_code_block(code: str):
    # Remove ```python or ``` or similar
    return re.sub(r"```[\w]*\n?", "", code).strip()


def safe_execute(code: str, df):
    local_vars = {"df": df, "plt": plt}
    try:
        cleaned_code = clean_code_block(code)
        exec(cleaned_code, {}, local_vars)
        fig = plt.gcf()
        return fig
    except Exception as e:
        return str(e)

# ✅ Wrapper for code execution


def run_code(code: str):
    return safe_execute(code, df)

# ✅ Create LangChain Agent


def run_agent():
    tools = [
        Tool(
            name="PythonPlotTool",
            func=run_code,
            description=(
                "You are a data analyst. Return only Python code using the 'df' DataFrame and matplotlib to answer data questions. "
                "Don't return explanation text. Just return valid Python code like: "
                "df.groupby('warehouse')['credits'].mean().plot(kind='bar') "
                "Available columns: ['date', 'warehouse', 'credits']"
            )
        )
    ]

    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=10,
        return_intermediate_steps=True
    )


agent = run_agent()

# ✅ Streamlit UI
st.title("🧠 Snowflake Cost Analyst")
query = st.text_input(
    "Ask a cost-related question about your warehouse costs:")

if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        output = agent.invoke({"input": query})

        st.success("Agent Response:")
        st.write(output["output"])  # Display the agent's answer

        # ✅ Display the generated plot if available
        for action, result in reversed(output["intermediate_steps"]):
            if isinstance(result, plt.Figure):
                st.pyplot(result)
                break
