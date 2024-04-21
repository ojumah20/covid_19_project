### Covid-19 Severity Prediction App
![covid_19](https://github.com/ojumah20/covid_19_project/blob/main/COVID%20testing%20policy%20drupal.jpg "Covid_19")

SARS-CoV-2, the virus behind the COVID-19 pandemic, emerged in Wuhan, China in December 2019 and rapidly spread worldwide, causing significant social and economic disruptions. Despite vaccination efforts and medical advancements, the virus remains a major global health concern, with over 763 million confirmed cases and 6 million reported deaths as of the latest data. The influx of COVID-19 patients has strained healthcare systems, requiring efficient resource allocation and patient prioritization based on severity. Current diagnostic methods can detect the presence of the virus but not the severity of the illness, necessitating supplementary approaches like blood testing, serology, medical imaging, and clinical notes analysis. However, the multitude of parameters from these tests can be challenging for physicians to interpret. Utilizing statistical or machine learning methods could help analyze these parameters and predict COVID-19 severity more accurately, ultimately improving patient outcomes by identifying patterns and providing precise prognostic information.
A web app was developed to predict based on selected features if a patient has covid-19 and to what intensity. 


**Data Source**
The dataset comprises records of 5644 patients, encompassing 111 parameters. Among these patients, only 558 tested positive for COVID-19 and fell within the 0 to 20 age quantiles. Notably, just 8.5% of positive cases necessitated hospital admission. Within this subset, 36 patients were placed in regular wards, 8 in semi-intensive units, and 8 in intensive care units, revealing a significant data imbalance. Patient information such as ID, age quantile, admission status, and results from various medical tests are included in the dataset. The admission status will serve as the target variable for predicting COVID-19 severity among positive patients.

https://www.kaggle.com/datasets/e626783d4672f182e7870b1bbe75fae66bdfb232289da0a61f08c2ceb01cab01



Project Lifecycle / System Design




Further Work
There is a need for error handling especailly when a user input a text or anything other than a float.
The look and feel of the web app can also be improve. I am opened to open source contributions. 

**Test Case**
MGHG =
MCH = 

Expected result = 
