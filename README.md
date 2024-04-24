# Covid-19 Severity Prediction App
![covid_19](https://github.com/ojumah20/covid_19_project/blob/main/COVID%20testing%20policy%20drupal.jpg "Covid_19")
<h3> Overview </h3>
This project tackles the challenge of predicting COVID-19 severity in patients using machine learning. It provides a user-friendly web application built with Flask and Bootstrap, allowing users to input clinical data and receive predictions on potential disease severity.

<div>
  <h3>Key Features</h3>
 <ul>
   <li>
     Machine learning models (XGBoost) for predicting COVID-19 severity levels.
   </li>
  <li>Interactive web app interface for user input and prediction results.</li>
   <li>Docker containerization for efficient deployment.</li>
 </ul>
  
</div>


<div>
<h3>Objectives </h3>
i. Develop a model to predict COVID-19 severity based on patient data.
ii. Deploy the model as a web application for broader user access.
iii. Automate deployment through a platform like Render.
</div>



<div>
<h3>Problem Statement </h3>
The problem is the need for a machine learning model to accurately predict the severity risk of COVID-19 patients, facilitating efficient resource allocation and improved patient care in light of traditional diagnostic limitations and the complexity of patient data.
 </div>


<div>
<h3>Data Collection </h3>
The dataset comprises records of 5644 patients, encompassing 111 parameters. Among these patients, only 558 tested positive for COVID-19 and fell within the 0 to 20 age quantiles. Notably, just 8.5% of positive cases necessitated hospital admission. Within this subset, 36 patients were placed in regular wards, 8 in semi-intensive units, and 8 in intensive care units, revealing a significant data imbalance. Patient information such as ID, age quantile, admission status, and results from various medical tests are included in the dataset. The admission status will serve as the target variable for predicting COVID-19 severity among positive patients.
Original data souce is (https://www.kaggle.com/datasets/e626783d4672f182e7870b1bbe75fae66bdfb232289da0a61f08c2ceb01cab01/data)  while the data was uploaded to my google drive and mounted from there for the model development (https://drive.google.com/drive/folders/1CglWG0EouMz4BJNylNSBzQPuiWA2-9C9?usp=drive_link).
  
</div>


<div>
  <h3>Exploratory Data Analysis (EDA)</h3>
  <p>The first step was understanding the data, which revealed that it comprises both positive and negative cases. Since the focus is on classifying the severity of COVID-19, the analysis will only consider positive cases. All negative cases have been removed. The image below illustrates the comparison between positive and negative cases in the dataset using the 'SARS-Cov-2 exam result' column.</p>
  <img src="https://github.com/ojumah20/covid_19_project/blob/main/cases.png" alt="Covid-19 cases" title="Covid-19 cases">

  <p>Among the positive cases, columns [Patient addmited to regular ward (1=yes, 0=no),	Patient addmited to semi-intensive unit (1=yes, 0=no),	Patient addmited to intensive care unit (1=yes, 0=no)] allows us to know the severity of the covid-19 cases and would be used in creatin the target variables </p>
  <img src="https://github.com/ojumah20/covid_19_project/blob/main/cases_1.png" alt="Covid-19 cases" title="Covid-19 Positive cases">
<p>From the exploration conducted so far, it is evident that only 558 patients tested positive. Among them, a mere 8.5% required hospital admission. Specifically, 36 were placed in regular wards, 8 in semi-intensive units, and 8 in intensive care units, highlighting a significant imbalance in the data.</p>
<p>Further exploration of the data can involve investigating how various variables influence one other.</p>

</div>


<div>
  <h3>Data preprocessing</h3>
  <ul>
    <li>Removed all negative cases and the 'SARS-Cov-2 exam result' column since it will only contain 'postive' as value.</li>
    <li>Dropped duplicates. Define what missing values are and drop columns with up to 92% missing values .</li> 
    <li>Replaced mising values in the categorical columns with 'missing' and that of the numeric columns with the mean.</li> 
    <li>Used correlation co-efficient to remove one of two columns that are hgihly correlated</li>
  </ul>
</div>


<div>

  <h3>Feature Engineering</h3>
  <ul><li>Performed Label encoding all independent categorical features using skit-learn 'Labelencoder'</li>
    <li>Merged three columns [Patient addmited to regular ward (1=yes, 0=no),	Patient addmited to semi-intensive unit (1=yes, 0=no),	Patient addmited to intensive care unit (1=yes, 0=no)] and encode them from 1-3. Encode no addmission as 0. View ipynb file for more information'</li>
    <li> Performed Synthetic Minority Over-sampling Technique due to the imbalance observed  </li>
    <li>Used the Random Forest algorithm with Recursive Feature Elimination with Cross-Validated (RFECV) selection, with 100 estimators, a random state of 42, and 10 k-fold. further explaination can be found in the ipynb file  </li>
    <li><img src="https://github.com/ojumah20/covid_19_project/blob/main/features.png" alt="Feature Importance" title="Covid-19 Features"> </li>
    <li></li>
  </ul>

  
</div>







<h3> Model Selection and development</h3>


<h3> Model evaluation </h3>


<h3> Model deployment and App development</h3>


<h3>Installation </h3>

<h3>Usage</h3>

<h3>Additional Information</h3>

<h3>Limitations and Room for Contributions</h3>
There is a need for error handling especailly when a user input a text or anything other than a float.
The look and feel of the web app can also be improve. I am opened to open source contributions. 











Further Work

