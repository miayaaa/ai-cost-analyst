# 🧠 Snowflake Cost Analyst (GenAI Demo)

A Generative AI–powered Streamlit app that lets you analyze Snowflake cost data using **natural language**.  
Users can ask questions like:

> “Plot the average credits per warehouse over the past 30 days”  
> “Visualize total daily credits in a line chart”

The app uses **LangChain Agents**, **OpenAI API**, and **matplotlib** to generate and render Python code in real time.


## 🚀 Features

✅ Ask questions in plain English  
✅ LLM automatically generates and runs analysis code  
✅ Interactive charts rendered with Streamlit  
✅ Works with your own Snowflake cost data (via CSV)


## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)


## 📦 Setup

```bash
# 1. Clone this repo
git clone https://github.com/your-username/AI-cost-analyst.git
cd snowflake-cost-analyst

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## 🧪 Run the App

```bash
streamlit run cost_analyst_app.py
```

Then open the local URL that Streamlit provides in your browser.

## 📌 Sample Questions
Plot average daily credits used per warehouse.
Show credit usage trends for each warehouse.
Visualize total daily credits in a line chart.



