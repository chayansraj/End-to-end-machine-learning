# Data Storytelling along with Machine Learning

<p align="center"> 
  <img width="800" height="400" src="https://user-images.githubusercontent.com/22219089/175320780-c002f13e-8380-4e76-95b2-e61fffd19339.png"> <h6 align = "center" > Source: google </h6>
</p>



Welcome to the year 2912, where your data science skills are needed to solve a cosmic mystery. We've received a transmission from four lightyears away and things aren't looking good.

The Spaceship Titanic was an interstellar passenger liner launched a month ago. With almost 13,000 passengers on board, the vessel set out on its maiden voyage transporting emigrants from our solar system to three newly habitable exoplanets orbiting nearby stars.

While rounding Alpha Centauri en route to its first destination—the torrid 55 Cancri E—the unwary Spaceship Titanic collided with a spacetime anomaly hidden within a dust cloud. Sadly, it met a similar fate as its namesake from 1000 years before. Though the ship stayed intact, almost half of the passengers were transported to an alternate dimension!
 
 
 
 # Methodology - 
* Explorative data analysis
  * Looking at each feature individually i.e Univariate Analysis. Examining descriptive statistics, understanding trends.
  * Examining feature interactions with other features. Multivariate analysis featuring key observations.
  * Describing numerical features in detail by analyzing skewness and kurtosis.
* Data preprocessing 
  * Balancing the dataset - Not every machine learning model is affected by outliers present in our data such as decision trees, random forests, support vector
  machines i.e. they are robust to outliers. But many other algorithms are sensitive to these types of noise and so it is a good idea to eliminate any kind of noise
  from the system.
  * Cleaning the dataset - We will always encounter some missing or NA values in our dataset and that is not okay with our fellow machine learning models. So, it is
  essential to clean the dataset of all the deficiencies keeping the data format in mind. Note - There are some algorithms that can handle missing values like XGBoost
  whereas most algorithms require non null values.
  * Structuring the dataset - It is also important to note that, ML models are basically mathematical functions and hence can accept only numeric data to work upon.
  This is not true for some algorithms like decision trees, random forests where we can also use categorical features along with numeric ones. Note - There are some
  algorithms that can handle categorical values like catboost, decision trees, etc. whereas most algorithms require non null values.
* Data leakage (or leakage) happens when your training data contains information about the target, but similar data will not be available when the model is used for
  prediction. This leads to high performance on the training set (and possibly even the validation data), but the model will perform poorly in production. There are
  two main types of leakage: target leakage and train-test contamination:
  * Target Leakage - Target leakage occurs when your predictors include data that will not be available at the time you make predictions. It is important to think
  about target leakage in terms of the timing or chronological order that data becomes available, not merely whether a feature helps make good predictions.
  * Train-Test Contamination - A different type of leak occurs when you aren't careful to distinguish training data from validation data. Recall that validation is
  meant to be a measure of how the model does on data that it hasn't considered before. You can corrupt this process in subtle ways if the validation data affects the
  preprocessing behavior. This is sometimes called train-test contamination.

* Modeling Process - 
  * The process of developing an effective model is both iterative and heuristic. It is difficult to know the needs of any data set prior to working with it and it is
  common for many approaches to be evaluated and modified before a model can be finalized. A typical modeling process is shown below
  
  
 
<p align="center"> 
  <img width="800" height="350" src="https://user-images.githubusercontent.com/22219089/178803633-ba47a6c3-626e-42e2-ab2b-c0c09de96114.JPG"> <h6 align = "center" > Source: http://www.feat.engineering/index.html </h6>
</p>

  * Models Used - 
    * Knearest Neighbors
    * Decision Trees
    * Random Forests
    * Support Vector Machines
    * XGBoost
    * Neural Networks
