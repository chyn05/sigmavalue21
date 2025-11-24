# Sigmavalue Real Estate Analysis Assistant

A full-stack web application that reads structured real-estate data from Excel and lets users ask natural language questions like:

> “Analyze Wakad price and demand from 2021 to 2024”  
> “Compare Wakad and Aundh price trend for the last 3 years”

The backend parses the query, filters and aggregates the dataset, and returns:

- A **text summary** (rule-based or generated via OpenAI)
- **Chart-ready metrics** (yearly trends for price/demand)
- A **filtered data table** (row-level view from the Excel file)

The frontend shows this in a **chat-style interface** with a **trend chart + table**.

See `sigmavalue_backend/` and `sigmavalue-frontend/` for more details.
