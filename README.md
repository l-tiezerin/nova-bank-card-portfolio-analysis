# Nova Bank – Card Portfolio Analysis

This project analyzes the performance and usability of the **Cards product** in a fictional financial institution (Nova Bank), using synthetic data and a realistic analytics architecture.

The goal is to **visually assess product health, usage, and growth** through well-defined KPIs and dashboards, as part of a personal data/analytics portfolio.

> 🚧 **Work in progress**: metrics, data model, and dashboards are being iteratively improved.

---

## 🎯 Objectives

- Monitor the performance of the Cards product over time  
- Evaluate customer adoption, activation, and usage  
- Simulate a real-world banking analytics environment  
- Showcase data modeling, metric design, and BI visualization skills

---

## 📊 Key Metrics (Initial Scope)

### Portfolio & Base
- Total bank customers
- Customers with active cards
- Active cards
- Cards with available limit
- Card penetration rate

### Usage & Transactions
- Total purchase volume (TPV)
- Number of transactions
- Average ticket
- IPP (installments per purchase)
- Purchase frequency per active card

### Credit & Limits
- Total credit limit
- Used vs available limit
- Average limit per card
- Limit utilization rate

### Customer & Card Status
- Activation rate
- Monthly churn (cards and customers)
- New vs existing customers
- Card modality distribution (credit, debit, hybrid)

---

## 🧱 Data Model (Planned)

- Customer monthly snapshots (24 months)
- Card monthly snapshots
- Transaction fact table (card purchases)
- Dimensions:
  - Customer
  - Card
  - Time
- Support for:
  - Multiple cards per customer
  - Temporal changes in limits and card attributes

All data is **synthetic**, generated with Python.

---

## 🛠️ Tech Stack

- **Python** – synthetic data generation
- **PostgreSQL** – local analytical database
- **Power BI** – data modeling and dashboards
- **Docker** (planned) – reproducible local environment

---

## 🚀 Roadmap

- [ ] Finalize metric definitions  
- [ ] Improve dimensional modeling (SCD, cohorts)  
- [ ] Add Docker setup for easy replication  
- [ ] Build Power BI dashboards  
- [ ] Document insights and assumptions  

---

## ⚠️ Disclaimer

This project uses **fictional data and a fictional bank**.  
It does not represent any real financial institution.

---

## 📌 Author

Developed as a personal portfolio project focused on analytics, product performance, and BI.