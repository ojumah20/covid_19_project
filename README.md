# Covid-19 Severity Prediction App
<p> This project tackles the challenge of predicting COVID-19 severity in patients using machine learning. It provides a user-friendly web application built with Flask and Bootstrap, allowing users to input clinical data and receive predictions on potential disease severity.</p>
<h3>Key Features </h3>
<ul><li>
Machine learning models (XGBoost) for predicting COVID-19 severity levels.
</li>
<li>Interactive web app interface for user input and prediction results.</li>
<li>Docker containerization for efficient deployment.</li>
</ul>

<h3>Project Goals </h3>
<ul><li>
Develop a model to predict COVID-19 severity based on patient data.
</li>
<li>Deploy the model as a web application for broader user access.</li>
<li>Automate deployment through a platform like Render.</li>
</ul>

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
<h3>Data Collection </h3>
The dataset comprises records of 5644 patients, encompassing 111 parameters. Among these patients, only 558 tested positive for COVID-19 and fell within the 0 to 20 age quantiles. Notably, just 8.5% of positive cases necessitated hospital admission. Within this subset, 36 patients were placed in regular wards, 8 in semi-intensive units, and 8 in intensive care units, revealing a significant data imbalance. Patient information such as ID, age quantile, admission status, and results from various medical tests are included in the dataset. The admission status will serve as the target variable for predicting COVID-19 severity among positive patients.
Original data souce is (https://www.kaggle.com/datasets/e626783d4672f182e7870b1bbe75fae66bdfb232289da0a61f08c2ceb01cab01/data) while the data was uploaded to my google drive and mounted from there for the model development (https://drive.google.com/drive/folders/1CglWG0EouMz4BJNylNSBzQPuiWA2-9C9?usp=drive_link).
  
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
  <li> Performed Synthetic Minority Over-sampling Technique due to the imbalance observed </li>
  <li>Used the Random Forest algorithm with Recursive Feature Elimination with Cross-Validated (RFECV) selection, with 100 estimators, a random state of 42, and 10 k-fold. further explaination can be found in the ipynb file </li>
  <li><img src="https://github.com/ojumah20/covid_19_project/blob/main/features.png" alt="Feature Importance" title="Covid-19 Features"> </li>
  <li>The independent variables were scaled using StandardScaler. This helped to standardize the range of features in the dataset so that they have similar means and standard deviations. This step ensured that the model does not place more meaning on a feature over the others, which could create bias. </li>
 </ul>

  
</div>




<div> 
 <h3> Model Selection and development</h3>
  
 <p> Two classification models were selected based on their popularities and high perfomance in literatures reviewed. Since it is a classification problem, other classification models can be explored to see the impact on performance. The Random Forest model was trained with n_estimators=1000, max_depth=10, and random_state=0. Finally, the XGBClassifier was trained with n_estimators=1000 and learning_rate=0.05 were compared and the XGBoost gave the better performnce with up to 99% across evaluation metrics however for the two models,the not admitted cases and regular cases are misclassified which is not a big case in the context of this project. </p>
<p>Building the web app with 18 fearures felt like a lot of inputs needed from new users , hence the model was retrained with the top five features based on the plotted feature importance during feature engineering. The top five features was selected based on the elblow method on the ploted Cross validation score versus number of features.</p>
<img src="https://github.com/ojumah20/covid_19_project/blob/main/feature%20importance.png" alt="Feature Importance curve" title="Covid-19 Features_curve">


</div>



<div>
 <h3> Model evaluation </h3>
 <p>The evaluation metrics used for the model were accuracy, precision, recall, and F1-score.These metrics are crucial in clinical data analysis for evaluating the model's ability to identify patients who require intensive care and minimizing the risk of falsely identifying patients who do not need it. A higher value for these metrics indicates better model performance.
 The result were <img src="https://github.com/ojumah20/covid_19_project/blob/main/model_result.png" alt="model_result" title = "model_result"></p>
 <p>The XGBoost model was saved as a pickel file to be used on new data input through the web app</p>
 <p> More details of the model evaluation can be found in the ipynb file.</p>

  
</div>



<div>
<h3> App development</h3>
 <p>The web app, leveraging Bootstrap for frontend development and Flask for backend functionality, incorporates Bootstrap for rapid interface design and Flask for processing the five user-input features and utilizing the saved model to generate predictions. </p> 
 <p>The Dockerfile snippet encapsulates the web app, including the saved model and other files, into a Docker image. It initializes a Python 3.11 environment, copies local files to the /app_dir directory, installs dependencies from requirements.txt, exposes a specified port, and initiates a Gunicorn server with four workers, binding to the designated port and launching the Flask application named my_app. </p>
</div>

<div>
<h3>Dockerfile Deployment</h3>
<p>The Dockerfile, which encapsulates the web app and model, is deployed to Render. Render was chosen as the deployment platform because it offers a free tier for hobbyists to showcase their work.</p>
    <img src="https://github.com/ojumah20/covid_19_project/blob/main/Image%2024-04-2024%20at%2019.56.jpeg" alt="Render_deployment1" title="Render1">
  
  <img src="https://github.com/ojumah20/covid_19_project/blob/main/Image%2024-04-2024%20at%2019.41.jpeg" alt="Render_deployment" title="Render">
  
</div>

<div>
<h3>Installation</h3>
To install, fork the repository, clone to github desktop and open with VS code, run the web app local using python app.py.
<h3>Usage</h3>
The webapp can be access through https://coding-project.onrender.com
   <img src="https://github.com/ojumah20/covid_19_project/blob/main/Image%2024-04-2024%20at%2019.54.jpeg" alt="webapp_deployment" title="webapp">

  
</div>

<div>
<h3>Limitations and Room for Contributions</h3>
<ul> <li>
 There is a need for error handling especailly when a user input a text or anything other than a float.
</li>
<li>Other classsification models can be explored to see if they give better model performance</li>
 <li>The look and feel of the web app can also be improved</li>
</ul>
</div>

<p> I am very open to contributions and feedback.</p>
expand_more
