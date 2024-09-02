# Life Insurance Prediction System

<ul> <b>Objective</b></ul>

The goal of this project is to develop a predictive model for estimating optimal insurance costs based on individual health and lifestyle data. By analyzing health and habit-related parameters.
the model aims to:


- Reduce Financial Risk: Offer precise insurance cost estimates to manage healthcare expenses effectively.
Optimize Insurance Pricing: Enable insurance companies to set fairer premiums, balancing risk and profitability.

- Risk Reduction: Improve financial stability by predicting insurance costs more accurately.
Increased Awareness: Enhance understanding of how lifestyle choices impact insurance premiums, encouraging proactive health management.

<ul><b> Business Problem</b></ul>

Healthcare is a critical sector, and managing insurance costs is essential for both individuals and providers. High medical expenses without adequate coverage can lead to significant financial strain. For insurance companies, accurately predicting costs is crucial for risk management and profitability. This project addresses the need for an accurate, data-driven approach to estimating insurance costs.

<ul>Methodology:</ul>

- Data Loading and Preprocessing: Clean data with pandas to ensure quality.

- Exploratory Data Analysis: Use visualizations like histograms and boxplots to explore data.

- Model Training: Train models including Logistic Regression, Decision Trees, Random Forests, AdaBoost, and Gradient Boosting.

- Model Evaluation: Evaluate models using R², Adjusted R², RMSE, and MAPE.

- Model Selection: Gradient Boosting was chosen for its superior accuracy, using sequential decision trees to refine predictions.

- Flask for Web Interface: Create a Flask-based interface for user input and insurance cost predictions.

<ul>Skills:</ul>
- SQL: CTEs, Joins, Case, aggregate functions

- Power BI: Dax,, ETL, data visualization, data modeling

- Python: Pandas, Matplotlib, Numpy, statistics, scikit-learn, flask



<ul><b>Dashboard:</b> </ul>

![image](https://github.com/user-attachments/assets/a059f25f-51e7-477f-ab54-7e44291c86c1)

<ul><b>Results & Business Recommendation:</b></ul>

- Results:

Model Accuracy:Gradient Boosting exhibited the highest accuracy with a model score of 95.42% and the lowest MAPE of 12.45%, making it the most reliable for predicting insurance costs.
The model identifies four key factors influencing insurance cost:

- Regular check-ups last year
- Weight
- Weight change in the last year
- Coverage by another company
  
Insurance Cost Predictions: The model accurately forecasts the optimal yearly insurance cost by analyzing health and lifestyle parameters, allowing for personalized premium adjustments.

<ul> <b>Business Recommendations:</b></ul>

- Incentives for Check-Ups: Provide insurance bonuses for frequent check-ups and adjust premiums for less frequent ones to promote proactive health management.

- Attract Existing Customers: Offer competitive deals to attract those with existing coverage from other companies.
  
- Support Weight Management: Provide free medical tests and discounted treatments for significant weight changes to boost retention and health outcomes.
  
- Encourage Health Monitoring: Offer incentives for regular health checks to customers dealing with weight issues.
  
- Target High-Risk Customers: Tailor insurance claims and benefits for those involved in high-risk activities like adventure sports, smoking, or heavy drinking.


By implementing these strategies, you can enhance customer retention, attract new clients, and optimize insurance pricing based on health and lifestyle factors.


<ul><b>Conclusion</b></ul>

The Life Insurance Prediction System effectively addresses the need for accurate insurance cost predictions. By integrating advanced machine learning techniques, the system enhances risk management and ensures fairer premiums. Gradient Boosting's robust performance highlights the transformative potential of data science in the insurance sector, offering valuable insights and improving financial management for both providers and consumers.

