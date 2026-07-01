# S1-Python for Data Science & API Foundations

## Objectives
- Build strong Python foundation
- Understand how ML models are exposed in production
- Learn REST APIs and containerization basics
- Introduce software engineering discipline (structure, logging, validation)

# Practice Project - Production - Style ML Scoring API

Function requirement:
- Endpoint: POST "/predict"
- Input Json:
`
{
  "age": 35,
  "income": 50000,
  "loan_amount": 10000,
  "credit_score": 680
}
`
- Output JSON:
`
{
  "risk_score": 0.42,
  "risk_category": "LOW"
}
`
## Modul de creare a *python environment*
`python -m venv .s1_venv`

## Activare *envirenment*
`.\.s1_venv\Scripts\activate`

### Technical Requirements
- [x] Use Pydanic models
- [ ] Input validation
- [ ] Error handiling (invalid input)
- [ ] Envirement variables for config
- [x] Dockerzied application
- [x] Requirements.txt
- [x] README.md

# Bibliografie
- [Building a Machine Learning API in 15 Minutes | Coding Challenge](https://www.youtube.com/watch?v=C82lT9cWQiA)
- [Loan Approval Classification Dataset](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)