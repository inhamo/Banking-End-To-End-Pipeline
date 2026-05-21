# Banking-End-To-End-Pipeline
## MASTER REQUIREMENTS & GOVERNANCE DOCUMENT

## 📑 TABLE OF CONTENTS

1. Executive Summary
2. Project Vision & Business Case
3. Project Governance & Team Structure
4. Scope, Constraints & Assumptions
5. Functional Requirements
6. Technical Requirements
7. Data Architecture Decisions
8. Data Modelling Strategy
9. Team Responsibilities (RACI)
10. Deliverables & Milestones
11. Risk & Issue Management
12. Quality Gates & Acceptance Criteria
13. Communication Plan
14. Sign-off & Approval

---

## 1. EXECUTIVE SUMMARY

### 1.1 Project Purpose
This project aims to modernise the bank's legacy data estate by implementing a Microsoft Fabric-based Lakehouse architecture. It will enable near-real-time risk reporting, democratise data access for business analysts, and provide a governed platform for data science teams to build and deploy credit risk models. This directly supports the bank's strategic pillar of becoming a data-driven organisation. Keeping in mind it is all about learning data engineering, science and analysis fundamentals before one even touches a tool.

### 1.2 Business Objectives (SMART)

| Objective ID | Objective Description | Success Metric | Target | Measurement Method |
|--------------|----------------------|----------------|--------|-------------------|
| OBJ-01 | | | | |
| OBJ-02 | | | | |
| OBJ-03 | | | | |
| OBJ-04 | | | | |

### 1.3 Stakeholder Summary

| Stakeholder | Role | Interest/Influence | Engagement Approach |
|-------------|------|-------------------|---------------------|
| | Executive Sponsor | High / High | Weekly steering committee |
| | Business Owner | High / High | Weekly prioritisation call |
| | Compliance Officer | High / Medium | Fortnightly review |
| | IT Director | Medium / High | Monthly architecture review |
| | End Users (Analysts) | Medium / Low | Fortnightly demo & feedback |

---

## 2. PROJECT VISION & BUSINESS CASE

### 2.1 Current State (As-Is)
*Describe the current pain points:*

| Pain Point | Impact | Quantified Impact (if known) |
|------------|--------|------------------------------|
| Data silos across business units | | |
| Manual reporting processes | | |
| No single source of truth | | |
| Data quality issues | | |
| Slow time-to-insight | | |
| Compliance/regulatory risk | | |
| | | |

### 2.2 Future State (To-Be)
*Paint the picture of success:*

```
[DESCRIBE THE IDEAL FUTURE STATE]
```

### 2.3 Business Case Summary

| Item | Description |
|------|-------------|
| **Expected Benefits** | |
| - Quantitative (revenue/cost) | |
| - Qualitative (risk/compliance/experience) | |
| **Estimated Investment** | |
| - Microsoft Fabric capacity (F-SKU) | |
| - Internal resource effort | |
| - External consultancy (if any) | |
| **ROI Timeline** | |
| **Go/No-Go Decision** | ☐ Go ☐ No-Go ☐ Conditional |
| **Approved Budget** | |

---

## 3. PROJECT GOVERNANCE & TEAM STRUCTURE

### 3.1 Governance Framework

```
[PROGRAMME STEERING COMMITTEE]
        │
        ├── Executive Sponsor
        ├── Business Owner
        ├── Head of Data & Analytics
        └── IT Director
                │
[PROJECT MANAGEMENT OFFICE]
        │
        ├── Programme Manager / Lead BA
        └── Scrum Master / Delivery Lead
                │
    ┌───────────┼───────────┐
    │           │           │
[DATA ENG]  [DATA ANAL]  [DATA SCI]
 Lead        Lead         Lead
```

### 3.2 Full Team Roster

| Name | Role | Team | Allocation | Core/Extended |
|------|------|------|------------|---------------|
| | Programme Manager | PMO | 50% | Core |
| | Business Analyst Lead | PMO | 100% | Core |
| | Product Owner | Business | 60% | Core |
| | Data Architect | Architecture | 50% | Core |
| | Lead Data Engineer | Data Engineering | 100% | Core |
| | Data Engineer (2x) | Data Engineering | 100% | Core |
| | Lead Data Analyst | Data Analysis | 100% | Core |
| | Data Analyst | Data Analysis | 100% | Core |
| | Lead Data Scientist | Data Science | 80% | Core |
| | Data Science Engineer | Data Science | 100% | Core |
| | Data Steward | Governance | 40% | Extended |
| | Compliance SME | Compliance | 20% | Extended |
| | Infrastructure Engineer | IT Ops | 30% | Extended |
| | Power BI Developer | BI Team | 100% | Core |
| | Test Lead | QA | 50% | Extended |

### 3.3 Escalation Path

| Level | Decision Authority | Escalation Trigger |
|-------|-------------------|-------------------|
| 1 - Working Team | Technical Leads | Day-to-day blockers |
| 2 - Project Management | Programme Manager | Resource/schedule/scope changes |
| 3 - Steering Committee | Executive Sponsor | Budget changes, strategic shifts |

---

## 4. SCOPE, CONSTRAINTS & ASSUMPTIONS

### 4.1 In Scope

| Area | Description |
|------|-------------|
| **Source Systems** | [e.g., Core Banking System, CRM, Trading Platform, Payment Gateway] |
| **Data Domains** | [e.g., Customer, Account, Transaction, Risk, Finance] |
| **Fabric Capabilities** | [e.g., Data Factory, Lakehouse, Notebooks, Pipelines, Power BI] |
| **Deliverables** | [e.g., Bronze/Silver/Gold layers, 5 dashboards, 2 ML models] |
| **Environments** | [e.g., Dev, Test, Prod Fabric Workspaces] |

### 4.2 Out of Scope (Explicit)

| Area | Reason | Future Consideration? |
|------|--------|----------------------|
| | | ☐ |
| | | ☐ |
| | | ☐ |

### 4.3 Constraints

| Constraint Type | Description | Impact |
|-----------------|-------------|--------|
| **Time** | | |
| **Budget** | | |
| **Technology** | Microsoft Fabric only (no multi-cloud) | |
| **Regulatory** | | |
| **Resource** | | |

### 4.4 Assumptions

| Assumption ID | Assumption | Validated By | Validation Date | Status |
|---------------|-----------|--------------|-----------------|--------|
| A-01 | | | | ☐ Open |
| A-02 | | | | ☐ Open |
| A-03 | | | | ☐ Open |
| A-04 | | | | ☐ Open |

### 4.5 Key Dependencies

| Dependency ID | Description | Depends On | Owner | Target Date | Status |
|---------------|-------------|------------|-------|-------------|--------|
| D-01 | Fabric capacity provisioned | IT Infrastructure | | | ☐ |
| D-02 | Source system access granted | Source System Owner | | | ☐ |
| D-03 | Business glossary completed | Data Steward | | | ☐ |
| D-04 | | | | | ☐ |

---

## 5. FUNCTIONAL REQUIREMENTS

### 5.1 Data Ingestion Requirements

| FR-ID | Requirement | Source System | Type | Frequency | Priority | Owner |
|-------|-------------|--------------|------|-----------|----------|-------|
| FR-ING-01 | | | Batch / Streaming / CDC | Daily / Hourly / Real-time | Must / Should / Could | |
| FR-ING-02 | | | | | | |
| FR-ING-03 | | | | | | |

### 5.2 Data Storage & Organisation Requirements

| FR-ID | Requirement | Details | Priority |
|-------|-------------|---------|----------|
| FR-STO-01 | Implement Medallion Architecture (Bronze/Silver/Gold) | | Must |
| FR-STO-02 | Bronze layer must preserve raw source data | No transformations, append-only | Must |
| FR-STO-03 | Silver layer must contain cleaned, deduplicated data | | Must |
| FR-STO-04 | Gold layer must contain business-aggregated views | | Must |
| FR-STO-05 | | | |

### 5.3 Data Transformation Requirements

| FR-ID | Business Rule / Transformation | Input Entity | Output Entity | Priority |
|-------|-------------------------------|--------------|---------------|----------|
| FR-TRN-01 | | | | |
| FR-TRN-02 | | | | |

### 5.4 Data Quality Requirements

| FR-ID | Data Quality Rule | Entity/Field | Rule Type | Threshold | Failure Action |
|-------|------------------|-------------|-----------|-----------|----------------|
| FR-DQ-01 | | | Completeness / Accuracy / Uniqueness / Timeliness / Consistency | | Flag / Quarantine / Reject |
| FR-DQ-02 | | | | | |

### 5.5 Security & Access Requirements

| FR-ID | Requirement | Details | Priority |
|-------|-------------|---------|----------|
| FR-SEC-01 | Row-Level Security (RLS) on all Gold-layer reporting tables | Based on user's business unit | Must |
| FR-SEC-02 | Column-Level Security (CLS) on PII fields | | Must |
| FR-SEC-03 | Dynamic Data Masking for sensitive columns | | Must |
| FR-SEC-04 | All access via Entra ID / Microsoft Entra groups | | Must |
| FR-SEC-05 | | | |

### 5.6 Reporting & Analytics Requirements

| FR-ID | Report/Dashboard Name | Audience | Refresh Cadence | Priority |
|-------|----------------------|----------|-----------------|----------|
| FR-RPT-01 | | | | |
| FR-RPT-02 | | | | |

### 5.7 Data Science / Machine Learning Requirements

| FR-ID | Model/Use Case | Target Variable | Business Outcome | Priority |
|-------|---------------|-----------------|------------------|----------|
| FR-DS-01 | | | | |
| FR-DS-02 | | | | |

---

## 6. TECHNICAL REQUIREMENTS

### 6.1 Platform: Microsoft Fabric

| Capability | Fabric Service | Justification |
|------------|---------------|---------------|
| **Data Ingestion** | Data Factory (Dataflows Gen2 / Pipelines) | |
| **Data Storage** | OneLake (Lakehouse / Warehouse) | |
| **Data Transformation** | Notebooks (PySpark) / Dataflows / T-SQL | |
| **Orchestration** | Data Pipelines | |
| **Data Science** | Notebooks, Experiments, ML Models | |
| **Real-Time Analytics** | Eventstreams, KQL Database | |
| **Semantic Layer** | Semantic Model (Power BI / Analysis Services) | |
| **Governance** | Microsoft Purview (integrated) | |
| **CI/CD** | Azure DevOps / Fabric Git Integration | |
| **Monitoring** | Fabric Capacity Metrics App, Azure Monitor | |

### 6.2 Fabric Workspace Architecture

| Workspace | Purpose | Owner Team | Access Pattern |
|-----------|---------|------------|----------------|
| **Admin/Governance** | Shared utilities, shared notebooks, configuration | Architecture | Read: All teams |
| **Data Engineering - Bronze** | Raw ingestion, landing zone | Data Engineering | Read: None externally |
| **Data Engineering - Silver** | Transformed, cleansed data | Data Engineering | Read: Analysts (request-based) |
| **Data Engineering - Gold** | Business-ready aggregates | Data Engineering | Read: All analysts, scientists |
| **Data Analysis** | Semantic models, Power BI reports | Data Analysis | Read: Business users |
| **Data Science** | Experiments, model training, feature stores | Data Science | Read: Analysts (limited) |
| **Sandbox** | Individual exploration | All teams | Read: Self-contained |

### 6.3 Technical Standards & Best Practices

| Area | Standard | Reference |
|------|----------|-----------|
| **Naming Conventions** | [Define: CamelCase, snake_case, prefix rules] | |
| **Code Repository** | Azure DevOps Git repo, branch strategy | |
| **Notebook Format** | PySpark with Markdown documentation cells | |
| **Data Format** | Delta Lake (Parquet) for all layers | |
| **Partition Strategy** | By date (YYYY/MM/DD) for fact tables | |
| **Security** | Managed Identity for service-to-service auth | |
| **Error Handling** | Try-except blocks, dead letter lake for failures | |
| **Logging** | Structured logging to Delta table | |
| **Documentation** | Every notebook must have header docstring | |

### 6.4 Performance & Scalability Requirements

| Requirement | Target | Measurement |
|-------------|--------|-------------|
| Bronze ingestion SLA | | |
| Silver transformation SLA | | |
| Gold aggregation SLA | | |
| Report query response time | | |
| Max concurrent users | | |
| Data volume (Year 1) | | |
| Data volume (Year 2 projected) | | |

### 6.5 Disaster Recovery & Business Continuity

| Requirement | Target |
|-------------|--------|
| Recovery Point Objective (RPO) | |
| Recovery Time Objective (RTO) | |
| Backup Strategy | |
| DR Testing Frequency | |

---

## 7. DATA ARCHITECTURE DECISIONS

> *This section captures key architecture decisions and their rationale. Every decision must be justified.*

### Architecture Decision Record (ADR)

### ADR-001: Medallion Architecture (Bronze-Silver-Gold)

| Field | Detail |
|-------|--------|
| **Status** | Proposed / Accepted / Deprecated |
| **Context** | We need a structured approach to data processing that balances raw data preservation with business consumption |
| **Decision** | Implement Medallion Architecture with 3 layers |
| **Options Considered** | 1. Traditional ETL (direct source-to-warehouse) 2. Medallion (Bronze/Silver/Gold) 3. Data Mesh (domain-specific) |
| **Rationale** | Medallion provides: incremental improvement in data quality, audit trail from raw to curated, flexibility for multiple consumption patterns, and native Fabric tooling support |
| **Consequences** | Additional storage cost (3 copies), need for orchestration between layers, clear governance needed at each transition |
| **Date** | |
| **Decided By** | |

### ADR-002: Data Modelling Approach

| Field | Detail |
|-------|--------|
| **Status** | Proposed / Accepted / Deprecated |
| **Context** | Gold layer must serve both analytical queries (BI) and data science feature engineering |
| **Decision** | |
| **Options Considered** | 1. Kimball Dimensional (Star Schema) 2. Data Vault 2.0 3. One Big Table (OBT) 4. Mixed approach |
| **Rationale** | |
| **Consequences** | |
| **Date** | |
| **Decided By** | |

### ADR-003: Choice Between Lakehouse and Warehouse

| Field | Detail |
|-------|--------|
| **Status** | Proposed / Accepted / Deprecated |
| **Context** | Fabric offers both Lakehouse (Spark) and Warehouse (T-SQL) endpoints |
| **Decision** | |
| **Options Considered** | 1. Lakehouse only 2. Warehouse only 3. Lakehouse for Bronze/Silver + Warehouse for Gold |
| **Rationale** | |
| **Consequences** | |
| **Date** | |
| **Decided By** | |

### ADR-004: Real-Time vs Batch Strategy

| Field | Detail |
|-------|--------|
| **Status** | |
| **Context** | |
| **Decision** | |
| **Options Considered** | |
| **Rationale** | |
| **Consequences** | |
| **Date** | |
| **Decided By** | |

### Additional ADRs (Add as needed)

| ADR ID | Topic | Decision | Rationale Summary |
|--------|-------|----------|-------------------|
| ADR-005 | Orchestration tool choice | | |
| ADR-006 | CI/CD strategy | | |
| ADR-007 | Monitoring approach | | |
| ADR-008 | Data lineage tracking | | |

---

## 8. DATA MODELLING STRATEGY

### 8.1 Modelling Principles
- [ ] Business-driven (not source-driven) design
- [ ] Conformed dimensions across all subject areas
- [ ] Slowly Changing Dimensions explicitly handled (Type 1/2)
- [ ] Grain declared for every fact table
- [ ] Surrogate keys for all dimensions
- [ ] Natural keys preserved for traceability
- [ ] No NULL foreign keys in fact tables

### 8.2 Conceptual Data Model (Subject Areas)

```
[Draw or describe high-level entities and their relationships]

Example:
┌──────────┐     ┌──────────┐     ┌──────────┐
│ CUSTOMER │────<│ ACCOUNT  │>────│TRANSACTION│
└──────────┘     └──────────┘     └──────────┘
     │                │
     │           ┌──────────┐
     └──────────>│   RISK   │
                 └──────────┘
```

**Your model here:**
```
[DESCRIBE OR SKETCH CONCEPTUAL MODEL]
```

### 8.3 Dimension Inventory

| Dimension Name | Source System | SCD Type | Estimated Row Count | Key Fields |
|----------------|---------------|----------|---------------------|------------|
| DimCustomer | | | | |
| DimAccount | | | | |
| DimProduct | | | | |
| DimDate | | | | |
| DimBranch | | | | |
| DimTransactionType | | | | |

### 8.4 Fact Inventory

| Fact Name | Grain (one row per...) | Source System | Estimated Volume | Associated Dimensions |
|-----------|----------------------|---------------|-----------------|----------------------|
| FactTransaction | | | | |
| FactAccountBalance | | | | |
| FactRiskAssessment | | | | |
| FactCustomerInteraction | | | | |

### 8.5 Data Lineage Expectations
- All Gold layer fields traceable to Silver transformations
- All Silver layer fields traceable to Bronze source
- Lineage visualised via Microsoft Purview
- Transformation logic documented in code comments

---

## 9. TEAM RESPONSIBILITIES (DETAILED RACI)

### 9.1 RACI Matrix - Full Project

| Activity / Deliverable | Programme Mgr | Product Owner | Data Architect | Lead DE | DE Team | Lead DA | DA Team | Lead DS | DS Team | Data Steward | BI Dev | Infra |
|------------------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **INITIATION** | | | | | | | | | | | | |
| Business case creation | A | R | C | I | I | C | I | I | I | I | I | I |
| Project charter | A | R | C | C | I | C | I | C | I | I | I | I |
| Stakeholder identification | A | R | I | I | I | I | I | I | I | I | I | I |
| **REQUIREMENTS** | | | | | | | | | | | | |
| Functional requirements | A | R | C | C | I | C | I | C | I | C | I | I |
| Technical requirements | C | I | A | R | C | C | I | C | I | C | I | C |
| Source system analysis | I | I | C | R | C | C | I | I | I | C | I | I |
| Data profiling | I | I | I | R | R | C | I | I | I | C | I | I |
| **ARCHITECTURE** | | | | | | | | | | | | |
| Platform architecture design | I | I | A | R | C | C | I | C | I | I | I | C |
| Data modelling (conceptual) | I | C | A | C | I | R | C | C | I | C | I | I |
| Data modelling (logical) | I | C | A | R | C | R | C | C | C | C | I | I |
| Data modelling (physical) | I | I | A | R | R | C | I | C | C | C | I | I |
| Security architecture | I | C | A | R | C | I | I | I | I | C | I | C |
| **DEVELOPMENT** | | | | | | | | | | | | |
| Bronze pipeline build | I | I | C | A | R | I | I | I | I | I | I | I |
| Silver transformation build | I | I | C | A | R | C | I | I | I | I | I | I |
| Gold aggregation build | I | C | C | A | R | C | I | I | I | I | I | I |
| Data quality framework | I | I | C | A | R | C | I | I | I | R | I | I |
| CI/CD pipelines | I | I | C | A | R | I | I | I | I | I | I | C |
| Unit testing | I | I | I | A | R | I | I | I | I | I | I | I |
| **ANALYTICS** | | | | | | | | | | | | |
| Semantic model design | I | C | C | C | I | A | R | C | I | I | R | I |
| Power BI report design | I | C | I | I | I | C | A | I | I | I | R | I |
| DAX measures development | I | I | I | I | I | C | R | I | I | I | R | I |
| **DATA SCIENCE** | | | | | | | | | | | | |
| Feature engineering | I | C | I | C | C | C | I | A | R | I | I | I |
| Model training & evaluation | I | C | I | I | I | I | I | A | R | I | I | I |
| Model deployment (MLOps) | I | I | C | C | C | I | I | A | R | I | I | C |
| **TESTING** | | | | | | | | | | | | |
| Integration testing | I | I | C | R | R | R | R | R | R | I | I | I |
| User Acceptance Testing | A | R | I | C | I | C | C | C | I | I | I | I |
| Performance testing | I | I | C | R | R | C | I | C | I | I | I | C |
| Security testing | I | I | C | C | C | I | I | I | I | C | I | R |
| **DEPLOYMENT** | | | | | | | | | | | | |
| Production deployment | C | I | A | R | R | I | I | C | I | I | C | C |
| Post-deployment validation | I | C | C | R | R | R | R | R | R | I | R | I |
| **OPERATIONS** | | | | | | | | | | | | |
| Monitoring & alerting | I | I | I | R | R | I | I | I | I | I | I | C |
| Incident management | I | I | I | A | R | I | I | I | I | I | I | I |
| Model retraining | I | C | I | I | I | I | I | A | R | I | I | I |

*(R=Responsible executes the work, A=Accountable signs off, C=Consulted gives input, I=Informed kept in the loop)*

### 9.2 Key Handoff Points

| Handoff | From | To | Artefact | Acceptance Criteria |
|---------|------|-----|----------|---------------------|
| Source data ready | Source System Owner | Data Engineering | Source system access, data dictionary | DE can read sample data |
| Bronze complete | Data Engineering | Data Engineering (Silver) | Raw data in Delta format | Row counts match source |
| Silver complete | Data Engineering | Data Analysts / Scientists | Cleansed, deduplicated data | DQ checks passing |
| Gold complete | Data Engineering | Data Analysts | Business-ready aggregates | Semantic model can be built |
| Semantic model ready | Data Analysts | BI Developers | Star schema model | All measures validate |
| Features ready | Data Engineering | Data Scientists | Feature table in Gold | DS can read and explore |
| Model ready | Data Scientists | Data Engineering (MLOps) | Trained model artefacts | Performance metrics met |
| Reports ready | BI Developers | Business Users | Power BI reports | UAT signed off |

---

## 10. DELIVERABLES & MILESTONES

### 10.1 Phased Delivery Plan

| Phase | Phase Name | Duration | Key Deliverables | Milestone Criteria |
|-------|-----------|----------|------------------|--------------------|
| **Phase 0** | Project Setup & Governance | Week 1-2 | Fabric capacity, workspace setup, team onboarding, this document signed | Environments accessible |
| **Phase 1** | Discovery & Analysis | Week 2-4 | Source system analysis, data profiling, business glossary, conceptual model | Requirements baselined |
| **Phase 2** | Architecture & Design | Week 4-6 | Logical data model, physical data model, architecture design doc, ADRs approved | Design review passed |
| **Phase 3** | Build - Bronze Layer | Week 6-9 | Ingestion pipelines, Bronze Lakehouse, DQ framework foundation | Bronze data flowing |
| **Phase 4** | Build - Silver Layer | Week 9-13 | Transformation notebooks, Silver Lakehouse, DQ checks operational | Silver data validated |
| **Phase 5** | Build - Gold Layer | Week 13-17 | Aggregation pipelines, Gold Lakehouse, feature engineering tables | Gold data available |
| **Phase 6** | Analytics & BI Development | Week 14-18 | Semantic models, Power BI dashboards, DAX measures | Reports in UAT |
| **Phase 7** | Data Science Development | Week 15-20 | Feature stores, model training, experiments, model evaluation | Model performance validated |
| **Phase 8** | Testing & QA | Week 18-22 | Integration testing, UAT, performance testing, security testing | All tests passed |
| **Phase 9** | Deployment & Go-Live | Week 22-24 | Production deployment, cutover, hypercare | Business sign-off |
| **Phase 10** | Closure & Handover | Week 24-26 | Documentation, runbooks, support model, lessons learned | Project closed |

### 10.2 Detailed Deliverable Register

| Deliverable ID | Deliverable | Phase | Owner | Reviewer | Due Date | Status |
|----------------|------------|-------|-------|----------|----------|--------|
| DEL-001 | Project README (this document) | 0 | PM/BA | All Leads | | |
| DEL-002 | Fabric Workspace Architecture | 0 | Data Architect | Infra Lead | | |
| DEL-003 | Source System Catalogue | 1 | Data Engineer | Data Architect | | |
| DEL-004 | Data Profiling Report | 1 | Data Engineer | Data Analyst | | |
| DEL-005 | Business Glossary | 1 | Data Steward | Product Owner | | |
| DEL-006 | Conceptual Data Model | 1 | Data Architect | All Leads | | |
| DEL-007 | Architecture Decision Records (ADRs) | 2 | Data Architect | Programme Mgr | | |
| DEL-008 | Logical Data Model | 2 | Data Architect | Data Analysts | | |
| DEL-009 | Physical Data Model | 2 | Lead DE | Data Architect | | |
| DEL-010 | Security Matrix | 2 | Data Architect | Compliance | | |
| DEL-011 | Bronze Ingestion Pipelines | 3 | DE Team | Lead DE | | |
| DEL-012 | Data Quality Rulebook | 3 | Data Steward | Data Analysts | | |
| DEL-013 | Silver Transformation Notebooks | 4 | DE Team | Lead DE | | |
| DEL-014 | Gold Aggregation Notebooks | 5 | DE Team | Data Analysts | | |
| DEL-015 | Feature Tables | 5 | DE Team | Lead DS | | |
| DEL-016 | Semantic Model | 6 | Data Analyst | Lead DA | | |
| DEL-017 | Power BI Dashboards (list) | 6 | BI Dev | Product Owner | | |
| DEL-018 | ML Models (list) | 7 | DS Team | Lead DS | | |
| DEL-019 | Test Report | 8 | Test Lead | Programme Mgr | | |
| DEL-020 | Deployment Runbook | 9 | Lead DE | Data Architect | | |
| DEL-021 | Operational Runbook | 9 | Lead DE | Infra Lead | | |
| DEL-022 | Training Materials | 9 | Lead DA | Product Owner | | |
| DEL-023 | Lessons Learned | 10 | Programme Mgr | All | | |

---

## 11. RISK & ISSUE MANAGEMENT

### 11.1 Risk Register

| Risk ID | Risk Description | Category | Impact (1-5) | Likelihood (1-5) | Score (I×L) | Mitigation Strategy | Owner | Status |
|---------|-----------------|----------|--------------|------------------|-------------|---------------------|-------|--------|
| RSK-01 | Source data quality worse than expected | Technical | 4 | 4 | 16 | Early profiling in Phase 1, buffer time in plan | Lead DE | Open |
| RSK-02 | Source system owners unresponsive | Stakeholder | 4 | 3 | 12 | Escalate to Steering Committee, identify backups | PM | Open |
| RSK-03 | Fabric capacity performance insufficient | Technical | 4 | 3 | 12 | Performance testing early, right-size SKU, scale-up contingency | Data Architect | Open |
| RSK-04 | Key team member unavailability | Resource | 3 | 3 | 9 | Cross-train, document everything, identify backup resources | PM | Open |
| RSK-05 | Regulatory change mid-project | External | 5 | 2 | 10 | Regular compliance touchpoints, flexible architecture | Compliance SME | Open |
| RSK-06 | Scope creep | Project | 3 | 4 | 12 | Rigorous change control, MVP-first approach, backlog for Phase 2 | PM | Open |
| RSK-07 | | | | | | | | | |

### 11.2 Issue Log

| Issue ID | Issue Description | Raised By | Date Raised | Impact | Resolution | Owner | Status |
|----------|-------------------|-----------|-------------|--------|------------|-------|--------|
| ISS-01 | | | | | | | Open/Resolved |
| ISS-02 | | | | | | | |

### 11.3 Change Request Log

| CR ID | Change Description | Requested By | Date | Impact Assessment | Decision | Approved By |
|-------|-------------------|-------------|------|-------------------|----------|-------------|
| CR-01 | | | | | Approved/Rejected/Deferred | |

---

## 12. QUALITY GATES & ACCEPTANCE CRITERIA

### 12.1 Phase Gate Checklist

**Gate 0 → Gate 1 (Proceed to Discovery)**
- [ ] Project charter approved
- [ ] Team onboarded
- [ ] Fabric environments provisioned
- [ ] Access to source systems requested
- [ ] This README document baselined

**Gate 1 → Gate 2 (Proceed to Design)**
- [ ] All source systems profiled
- [ ] Data quality issues documented
- [ ] Business glossary baselined
- [ ] Conceptual data model approved
- [ ] Requirements signed off by Product Owner

**Gate 2 → Gate 3 (Proceed to Build)**
- [ ] Architecture design approved
- [ ] ADRs accepted
- [ ] Logical and physical data models approved
- [ ] Security design reviewed by Compliance
- [ ] Development standards agreed

**Gate 3 → Gate 4+5+6 (Mid-Build Check)**
- [ ] Bronze pipelines running in Dev
- [ ] Data quality framework implemented
- [ ] Sample Silver data validated by Analysts
- [ ] Dev environment stable

**Gate 5/6 → Gate 7 (Proceed to Testing)**
- [ ] All Gold tables built
- [ ] Semantic model built and validated
- [ ] Reports developed and in UAT
- [ ] Models trained and evaluated
- [ ] Unit tests all passing

**Gate 7 → Gate 8 (Proceed to Go-Live)**
- [ ] UAT signed off
- [ ] Performance tests passed
- [ ] Security tests passed
- [ ] Deployment runbook tested
- [ ] Rollback plan documented
- [ ] Support team briefed

### 12.2 Acceptance Criteria Template

| Deliverable | Acceptance Criteria | Validated By | Validation Method |
|-------------|--------------------|------------|-------------------|
| | 1. | | |
| | 2. | | |
| | 3. | | |

---

## 13. COMMUNICATION PLAN

| Communication | Audience | Frequency | Channel | Owner |
|---------------|----------|-----------|---------|-------|
| Daily Stand-up | Working Team | Daily (15 min) | Teams call | Scrum Master |
| Sprint Review / Demo | Extended Team, Stakeholders | Fortnightly | Teams call + recording | Programme Mgr |
| Steering Committee Update | Exec Sponsor, Business Owner | Monthly | PowerPoint deck + meeting | Programme Mgr |
| Risk & Issue Review | Programme Mgr, Technical Leads | Weekly | Teams call | Programme Mgr |
| Business Newsletter | All stakeholders | Monthly | Email | BA Lead |
| Technical Deep Dive | Technical Teams | As needed | Teams call | Data Architect |

### Communication Escalation Triggers
- Risk score exceeds 15
- Milestone slip > 2 weeks
- Budget variance > 10%
- Critical resource loss
- Compliance/regulatory incident

---

## 14. SIGN-OFF & APPROVAL

This document serves as the **single source of truth** for the project. By signing, you confirm:

- Requirements are complete and accurate
- Scope is understood and agreed
- Responsibilities are clear
- Timeline and deliverables are achievable

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Executive Sponsor** | | | |
| **Business Owner / Product Owner** | | | |
| **Programme Manager** | | | |
| **Data Architect** | | | |
| **Lead Data Engineer** | | | |
| **Lead Data Analyst** | | | |
| **Lead Data Scientist** | | | |
| **Compliance Officer** | | | |
| **IT Infrastructure Lead** | | | |

---

## APPENDICES

### A. Glossary of Terms

| Term | Definition |
|------|------------|
| **Fabric** | Microsoft's unified data platform |
| **OneLake** | Single, unified logical data lake across Fabric |
| **Lakehouse** | Combines data lake flexibility with warehouse structure |
| **Medallion** | Bronze (raw) → Silver (cleansed) → Gold (curated) architecture |
| **Semantic Model** | Power BI modelling layer for business logic |
| **Delta Lake** | Open-source storage layer with ACID transactions on data lakes |
| **dbt** | Data build tool (can integrate with Fabric) |
| **CDE** | Critical Data Element |
| **SCD** | Slowly Changing Dimension |
| **RPO/RTO** | Recovery Point/Time Objective |

### B. Reference Documents

| Document | Location | Owner |
|----------|----------|-------|
| Bank's Data Strategy | [Link] | |
| Microsoft Fabric Documentation | [Link] | |
| Data Governance Policy | [Link] | |
| Security Classification Policy | [Link] | |

### C. References to Industry Literature (Learning Context)

| Book / Resource | Key Concepts Applied |
|-----------------|---------------------|
| **Fundamentals of Data Engineering** (Reis & Housley) | Lifecycle thinking, undercurrents (security, data ops, architecture) |
| **The Data Warehouse Toolkit** (Kimball) | Dimensional modelling, star schemas, conformed dimensions |
| **Designing Data-Intensive Applications** (Kleppmann) | Reliability, scalability, maintainability in data systems |
| **Data Mesh** (Dehghani) | Domain ownership, data as product, federated governance |
| **Building the Data Lakehouse** (Armbrust et al.) | Medallion architecture, Delta Lake, Lakehouse paradigm |
| **Microsoft Fabric Documentation** | Workspace architecture, CI/CD, OneLake, semantic models |

---

**END OF MASTER README**

---

This is your master document. It sits **above** the individual team documents and ensures everyone is aligned before the Data Engineering team builds their detailed design, the Data Analysts build their semantic model spec, and the Data Scientists build their model requirements. Each team can then derive their own detailed specification from this single source of truth.
