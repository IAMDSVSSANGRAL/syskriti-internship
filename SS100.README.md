# 🚀 Hiring Pitch Deck – Vishal Singh Sangral

> Data Analyst | ML Engineer | Business-Driven Problem Solver

---

## 🎯 Slide 1 – Who I Am & Why I Matter

### 👋 About Me

I am a data professional who bridges **business operations and machine learning systems**.

Unlike traditional analysts, I don’t just create dashboards —  
I build **decision systems that drive measurable impact**.

### 💡 Core Strengths

- Python, SQL, Spark , Clickhouse, 
- Machine Learning & NLP (Transformers, Deep Learning)
- MLOps (Docker, MLflow, DVC)
- Data Pipelines & Automation
- Business Operations & Revenue Optimization

### 🔥 My Edge

- Managed 250,000+ orders in an eCommerce business
- Led teams of 4 members
- Deployed dagster pipeline in production and build mulitple kpi Dashboards for busines.
- Strong ownership mindset

---

## 📊 Slide 2 – Proof of Execution

### 📈 Business Impact

- Generated ₹1 Crore+ in revenue operations
- Built internal reporting systems to reduce operational costs
- Automated analytics workflows to improve decision-making speed

### ⚙️ Technical Projects

- Dynamic CSV → PostgreSQL ingestion Python package
- Marine Port Berth Utilization forecasting model
- NLP-based review intelligence system
- Google Sheets → Python → Dashboard automation pipeline

### 🧠 Leadership & Ownership

- SLA & Client management experience
- Cross-functional collaboration
- Operated in high-responsibility roles without supervision

---

## 📈 Slide 3 – Why I’m the Ideal Fit

### 🎯 What Modern Companies Need

- Data-driven decision makers
- Ownership mentality
- End-to-end problem solvers
- Business-aligned technical professionals

### 🚀 What I Deliver

- Technical depth + business acumen
- Ability to convert raw data → insights → action
- Scalable system design thinking
- Continuous learner mindset

---

## 🏁 Closing Statement

I don’t just analyze data.  
I build systems that improve decisions, reduce inefficiencies, and scale operations.

If you're looking for someone who takes ownership beyond dashboards —  
let’s connect.

---

📩 Open to opportunities in:
- Senior Data Analyst
- ML Engineer
- Analytics Engineer
- Data Science Roles


# Task SQL100 TASK2 


# 📊 Database Replication Expansion Proposal  
## From 3 Replicas to 10 Replicas  
### Reducing Latency from 20ms → 1ms  

**Prepared By:** Vishal Singh Sangral  
**Audience:** Engineering Leadership & Management  

---

# 🟦 Slide 1 — Executive Summary & Problem Statement

## 📌 Current State

- 1 Primary Database Server  
- 2 Read Replicas  
- Single-Primary Replication  
- Average Read Latency: **20 milliseconds**  
- Increasing global user traffic  

## ⚠️ Business Problem

- Higher response time impacting user experience  
- Increased load on limited replicas  
- Risk of downtime affecting SLA  
- Limited horizontal scalability  

---

## 🎯 Proposal

Increase replicas from **3 → 10** to:

- Reduce latency to **~1 millisecond**
- Improve availability
- Distribute read load efficiently
- Enable future global expansion

---

# 🟦 Slide 2 — Technical Architecture & Performance Impact

## 🏗 Current Architecture

- Single Primary (Read + Write)
- 2 Read Replicas
- Asynchronous Replication
- Limited geographic distribution

---

## 🚀 Proposed Architecture

- 1 Primary Server (Write Operations)
- 9 Read Replicas (Read Operations)
- Multi-region deployment
- Load balancer for read routing
- Asynchronous replication model

---

## 📈 Performance Improvements

| Metric | Current | Proposed |
|--------|----------|-----------|
| Read Latency | 20ms | ~1ms |
| Read Throughput | Moderate | High |
| Availability | Medium | High |
| Scalability | Limited | Horizontal Scaling |

---

## 💡 Why It Works

- Local replicas reduce network travel time
- Read traffic distributed across 9 nodes
- Reduced bottleneck on primary
- Faster query response for global users

---

# 🟦 Slide 3 — Risks & Mitigation Strategy

## ⚠️ Risk 1: Eventual Consistency

Asynchronous replication may cause short stale-read windows.

### ✅ Mitigation:
- Route critical reads to Primary
- Monitor replication lag
- Define SLA thresholds
- Alerting system for lag spikes

---

## ⚠️ Risk 2: Write Bottleneck

Primary still handles all writes.

### ✅ Mitigation:
- Vertical scaling of primary
- Optimized indexing
- Partitioning large tables
- Future sharding consideration

---

## ⚠️ Risk 3: Operational Complexity

More servers = more monitoring and management.

### ✅ Mitigation:
- Automated health checks
- Auto-failover mechanisms
- Infrastructure-as-Code deployment
- Managed cloud replication services

---

# 🟦 Slide 4 — Cost, ROI & Strategic Value

## 💰 Cost Considerations

### Infrastructure Cost
- 7 Additional Servers
- Storage & Backup Costs
- Network Traffic Costs

### Operational Cost
- Monitoring
- Maintenance
- DevOps Effort

---

## 📊 Cost vs Business Value

| Factor | Impact |
|--------|--------|
| Infrastructure Cost | Moderate |
| Latency Reduction | High Business Impact |
| SLA Improvement | Critical |
| Customer Experience | High |
| Revenue Protection | High |

---

## 🎯 Strategic Benefits

✔️ Future-proof Infrastructure  
✔️ Supports Global Expansion  
✔️ High Availability Architecture  
✔️ Better Load Distribution  
✔️ Improved User Experience  

---

## 🧠 Trade-Off Awareness

Every distributed system balances:

- Consistency  
- Latency  
- Cost  
- Complexity  

This proposal prioritizes:

**Performance + Availability + Scalability**  
while managing consistency through controlled eventual consistency.

---

# 🏁 Conclusion

Increasing database replicas from **3 → 10** is a strategic infrastructure upgrade that:

- Reduces latency from 20ms → ~1ms  
- Increases availability  
- Enhances scalability  
- Protects revenue and brand trust  

This is not just a performance improvement —  
it is an investment in long-term system resilience and business growth.

---

## 📚 Concepts Referenced

- Single-Primary Replication
- Eventual vs Strong Consistency
- Load Balancing
- Indexing & Partitioning
- OLTP Optimization
- Distributed Database Architecture


