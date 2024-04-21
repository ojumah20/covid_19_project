# Covid-19 Severity Prediction App
![covid_19](https://github.com/ojumah20/covid_19_project/blob/main/COVID%20testing%20policy%20drupal.jpg "Covid_19")
<h3> Overview </h3>
SARS-CoV-2, the virus behind the COVID-19 pandemic, emerged in Wuhan, China in December 2019 and rapidly spread worldwide, causing significant social and economic disruptions. Despite vaccination efforts and medical advancements, the virus remains a major global health concern, with over 763 million confirmed cases and 6 million reported deaths as of the latest data. The influx of COVID-19 patients has strained healthcare systems, requiring efficient resource allocation and patient prioritization based on severity. Current diagnostic methods can detect the presence of the virus but not the severity of the illness, necessitating supplementary approaches like blood testing, serology, medical imaging, and clinical notes analysis. However, the multitude of parameters from these tests can be challenging for physicians to interpret. Utilizing statistical or machine learning methods could help analyze these parameters and predict COVID-19 severity more accurately, ultimately improving patient outcomes by identifying patterns and providing precise prognostic information.
A web app was developed to predict based on selected features if a patient has covid-19 and to what intensity. 

<div> 
<h3>Aim</h3>
This project aims to develop a machine learning model for predicting the severity risk of COVID-19 patients and deploy it as a web application using Flask and Bootstrap, allowing users to input new data for predictions, with automated deployment to Render facilitated through GitHub Actions.
</div>

<div>
<h3>Objectives </h3>
  
1. **Design of Experiments and Web Application Development:**
   - Collect and analyze a dataset containing records of COVID-19 patients, focusing on demographic, clinical, and laboratory information.
   - Create an web interface using Flask and Bootstrap to enable users to input data for predictions.
   
2. **Model Selection and Integration:**
   - Develop machine learning models, including logistic regression and XGBoost, to predict the severity of COVID-19 cases.
   - Incorporate the developed machine learning model into the web application, ensuring seamless interaction between user inputs and prediction outputs.

3. **Model Evaluation and Deployment Automation:**
   - Evaluate the performance of the developed models using precision, recall, and F1-score metrics.
   - Establish automated workflows using GitHub Actions to streamline the deployment process of the web application to Render.

4. **Hyperparameter Tuning and Testing:**
   - Fine-tune the hyperparameters of the logistic regression model using GridSearchCV to optimize model accuracy and prevent overfitting.
   - Conduct thorough testing of the web application to ensure functionality, performance, and security.

5. **Conclusion and Further Work:**
   - Conclude on the effectiveness of machine learning techniques in predicting COVID-19 severity and the usability of the deployed web application.
   - Propose areas for further research, such as exploring advanced feature selection techniques and enhancing user experience for clinical decision-making.
</div>



<div>
<h3>Problem Statement </h3>
The problem is the need for a machine learning model to accurately predict the severity risk of COVID-19 patients, facilitating efficient resource allocation and improved patient care in light of traditional diagnostic limitations and the complexity of patient data.
 </div>


<div>
<h3>Data Collection and Preprocessing</h3>
The dataset comprises records of 5644 patients, encompassing 111 parameters. Among these patients, only 558 tested positive for COVID-19 and fell within the 0 to 20 age quantiles. Notably, just 8.5% of positive cases necessitated hospital admission. Within this subset, 36 patients were placed in regular wards, 8 in semi-intensive units, and 8 in intensive care units, revealing a significant data imbalance. Patient information such as ID, age quantile, admission status, and results from various medical tests are included in the dataset. The admission status will serve as the target variable for predicting COVID-19 severity among positive patients.
  
</div>




Feature Selection
https://github.com/ojumah20/covid_19_project/blob/main/features.png







<h3>Exploratory Data Analysis (EDA)</h3>
<h3>Feature Engineering</h3>
<h3> Model Selection and development</h3>
<h3> Model evaluation </h3>
<h3> Model deployment and App development</h3>
<h3>Installation </h3>
<h3>Usage</h3>
<h3>Contributing</h3>
<h3>Additional Information</h3>
<h3>Limitations and Room for Contributions</h3>
https://www.kaggle.com/datasets/e626783d4672f182e7870b1bbe75fae66bdfb232289da0a61f08c2ceb01cab01








Further Work
There is a need for error handling especailly when a user input a text or anything other than a float.
The look and feel of the web app can also be improve. I am opened to open source contributions. 

