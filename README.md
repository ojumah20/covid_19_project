# Covid-19 Severity Prediction App
<div> 
    <p> This project tackles the challenge of predicting COVID-19 severity in patients using machine learning. It provides a user-friendly web application built with Flask and Bootstrap, allowing users to input clinical data and receive predictions on potential disease severity.</p>
    <h3>Key Features </h3>
    <ul>
        <li>
        Machine learning models (XGBoost) for predicting COVID-19 severity levels.
        </li>
        <li>Interactive web app interface for user input and prediction results.</li>
        <li>Docker containerization for efficient deployment.</li>
    </ul>
    
<h3>Project Goals </h3>
<ul>
        <li>
        Develop a model to predict COVID-19 severity based on patient data.
        </li>
        <li>Deploy the model as a web application for broader user access.</li>
        <li>Automate deployment through a platform like Render.</li>
    </ul>

</div>


![covid_19](https://github.com/ojumah20/covid_19_project/blob/main/COVID%20testing%20policy%20drupal.jpg "Covid_19")
<div>
    <h3> 1. Introduction </h3>
    <p> The COVID-19 pandemic has significantly impacted global health. Traditional diagnostic methods primarily focus on virus detection, but don't always predict disease severity. This project explores using machine learning to analyze patient data and predict potential COVID-19 severity levels.</p>
</div>



<div>
    <h3>2. Data Acquisition and Preprocessing </h3>
    <p> The dataset used for this project was obtained from Kaggle [https://www.kaggle.com/datasets/e626783d4672f182e7870b1bbe75fae66bdfb232289da0a61f08c2ceb01cab01/data]. It contains various clinical features for patients diagnosed with COVID-19. Data cleaning and preprocessing steps were performed to handle missing values, outliers, and ensure data quality. Techniques like SMOTE were used to address data class imbalance. The image below illustrates the comparison between positive and negative cases in the dataset using the 'SARS-Cov-2 exam result' column</p> <img src="https://github.com/ojumah20/covid_19_project/blob/main/cases.png" alt="Covid-19 cases" title="Covid-19 cases">
<p>Among the positive cases, columns [Patient addmited to regular ward (1=yes, 0=no),Patient addmited to semi-intensive unit (1=yes, 0=no),	Patient addmited to intensive care unit (1=yes, 0=no)] allows us to know the severity of the covid-19 cases and would be used in creatin the target variables </p>
 <img src="https://github.com/ojumah20/covid_19_project/blob/main/cases_1.png" alt="Covid-19 cases" title="Covid-19 Positive cases">
  
</div>

<div>
    <h3> 3. Feature Engineering</h3>
    <p> The feature engineering stage involved label encoding categorical features using scikit-learn's LabelEncoder. Additionally, three admission-related columns were merged into a single feature with labels ranging from 1 (regular ward admission) to 3 (intensive care unit admission), with 0 representing no admission. Furthermore, I utilized Random Forest with Recursive Feature Elimination with Cross-Validation (RFECV) for feature selection, with details available in the provided Jupyter notebook. Feature importance was visualized <img src="https://github.com/ojumah20/covid_19_project/blob/main/features.png" alt="Feature Importance" title="Covid-19 Features">, and finally, I standardized the independent variables using StandardScaler to prevent bias in model training by ensuring all features have similar scales.</p>

  
</div>

<div>
    <h3> 5. Methodology </h3>
    <p> The XGBoost algorithm, known for its efficiency and accuracy in classification tasks, was chosen for predicting COVID-19 severity. Other classification models like random forest was explored based on popularity from literature reviewed. Building with 18 features after preprocessing appeared unrealistic , hence ploting the feature importance curve to determine the optimal number of features was important. </p>
    <img src="https://github.com/ojumah20/covid_19_project/blob/main/feature%20importance.png" alt="Feature Importance curve" title="Covid-19 Features_curve">
    <p>Based on the curve, the top five features were selected. The features selected were mean corpuscular hemoglobin concentration, Mean corpuscular hemoglobin, Red cell distribution width, Eosinophils and Proteina C reativa mg/dL</p>
    
</div>



<div>
     <h3> 4. Model Evaluation </h3>
     <p>The evaluation metrics used for the model were accuracy, precision, recall, and F1-score.These metrics are crucial in clinical data analysis for evaluating the model's ability to identify patients who require intensive care and minimizing the risk of falsely identifying patients who do not need it. A higher value for these metrics indicates better model performance. The result were</p>
    <img src="https://github.com/ojumah20/covid_19_project/blob/main/model_result.png" alt="model_result" title = "model_result"> 
    <p> The XGBoost model was saved as a pickel file to be used on new data input through the web app.</p>  
</div>



<div>
<h3> 5. Web Application Development</h3>
 <p> The web application leverages Flask for backend functionality and Bootstrap for a user-friendly frontend. The application takes user input for relevant clinical features and utilizes the trained model to generate severity predictions. </p>
</div>

<div>
    <h3> 6. Deployment</h3>
    <p>The web application is containerized using Docker for easy deployment and management. The containerized application is then deployed on a platform like Render, allowing users to access it remotely.</p>
        <img src="https://github.com/ojumah20/covid_19_project/blob/main/Image%2024-04-2024%20at%2019.56.jpeg" alt="Render_deployment1" title="Render1">
      <img src="https://github.com/ojumah20/covid_19_project/blob/main/Image%2024-04-2024%20at%2019.41.jpeg" alt="Render_deployment" title="Render">
  
</div>

<div>
    <h3>7. Installation and Usage</h3>
    <h3>Local Installation</h3>
    <p>To install, fork the repository, clone to github desktop and open with VS code, run the web app local using python app.py. </p>
    <h3>Web Access</h3>
    <p>The webapp can be access through https://coding-project.onrender.com </p>
    <img src="https://github.com/ojumah20/covid_19_project/blob/main/Image%2024-04-2024%20at%2019.54.jpeg" alt="webapp_deployment" title="webapp">

  
</div>

<div>
    <h3> 8. Limitations and Future Work </h3>
    <p>The project acknowledges limitations such as Error handling  and Potential for improvement in the user interface design. </p>
    <p>Future exploration could involve evaluating other classification models for potentially better performance and enhancing user experience and incorporating additional features.</p>
</div>

<div> 
    <h3>9. Conclusion </h3>
    <p> This project demonstrates the feasibility of applying machine learning to predict COVID-19 severity. The developed web app offers a convenient tool for healthcare professionals or researchers to gain insights into potential disease course. We encourage contributions and feedback to further refine and improve this project.</p>

</div>
<p> 
#machinelearning
#datascience
#artificialintelligence
#covid19
#healthcare
#webdevelopment
#webapplication
#flask
#bootstrap
#opentosource
#project
#mlops
#modeldeployment
#covid19prediction
#covidseverity
#xgboost (if your project uses XGBoost)
#featureengineering
#datascaling
#modeloperation
#deployment
#docker
#render
</p>
