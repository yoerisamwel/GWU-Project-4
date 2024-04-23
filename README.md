# Furniture Ecommerce
By: 
[Alaa Aleryani](https://github.com/alaa-aleryani) and
[Yoeri Samwel](https://github.com/yoerisamwel)

<!-- ![ecommerce](Images/ecommerce.jpg) -->
<img src="Images/ecommerce.jpg" alt="Ecommerce" width="1000" height="300">


## Built With:

<div align="center">
  <table>
    <tr>
      <td align="center" width="96">
        <a href="http://python.org">
          <img src="./Images/python-original.svg" width="48" height="48" alt="Python" />
        </a>
        <br>Python
      </td>
      <td align="center" width="96">
        <a href="https://jupyter.org/" >
          <img src="./Images/jupyter-logo.svg" width="48" height="48" alt="Jupyter Notebook" />
        </a>
        <br>Jupyter Notebook
      </td>
      <td align="center" width="96">
        <a href="https://public.tableau.com/app/discover" >
          <img src="Images/tableau.png" width="48" height="48" alt="Tableau" />
        </a>
        <br>Tableau 
      </td>
      <td align="center" width="96">
        <a href="https://scikit-learn.org/stable/" >
          <img src="./Images/scikitlearn.png" width="48" height="48" alt="scikit learn" />
        </a>
        <br> Scikit Learn
      </td>
      <td align="center" width="96">
        <a href="https://facebook.github.io/prophet/docs/quick_start.html" >
          <img src="./Images/prophet.png" width="48" height="48" alt="Time Series Forecast" />
        </a>
        <br> Prophet
      </td>
    </tr>
  </table>
</div>

## Overview
The purpose of this project is to:
  - **Understand Regional Market** and **Enhance Personalization:** By analyzing past purchase history,  understand the unique characteristics, preferences, and behaviors of customers in different geographic areas. 
  - **Identify Growth Opportunities:** identify trends and patterns in sales performance, and market demand.
  - **Understanding Seasonal Influences:** understand how seasonal factors, and local events impact consumer behavior and purchasing patterns in different regions.

> **Note:**
> we got our data from [Kaggle](https://www.kaggle.com/datasets/dkhalidashik/superstore-furniture-sales)
>


## Visualizations
For some insights into our dataset, feel free to check our visualization dashboard at [Tableau Public](https://public.tableau.com/app/profile/alaa.al.eryani/viz/Ecommerce_17070771557310/ProfitDashboard)

## Analysis

We used three machine learning models:
  - **Model 1:** [Linear Regression](https://github.com/yoerisamwel/GWU-Project-4/blob/main/Analysis/Linear_Regression.ipynb) 
  - **Model 2:** [Ridge Regression](https://github.com/yoerisamwel/GWU-Project-4/blob/main/Analysis/Linear_Regression.ipynb)  
  - **Model 3:** [Time Series Forecasts using Facebook's Prophet.](https://github.com/yoerisamwel/GWU-Project-4/blob/main/Analysis/Sales_TimeSeries_Prediction_Prophet.ipynb)
  

## Results 📈 📉


<!-- Hidden Pictures -->
<!-- Model 1 -->

<details>
<summary><b> Model 1 👇:</b></summary>
  
Our first step in the analysis used a `Linear Regression` model to predict the Original Price by looking at various factors. We chose this model for its simplicity and ease of understanding. It helped us see how different variables influence the price. Although it's straightforward to use, the model's accuracy score of 64% in our tests shows it's not entirely accurate. This result suggests that we might need to consider more advanced methods in future to improve our predictions.

  <img width="674" alt="Model 1 Result" src="./Images/regression_fit_plot_model_1.png"> <br>

This graph visualizes the `linear regression` model's predictions, showing how the target variable (e.g., 'Original_Price') changes as a function of the 'Quantity' feature, alongside actual data points for comparison.

</details>


<!-- Model 2 -->

<details>
<summary><b> Model 2 👇:</b></summary>

The `Ridge Regression` model showed exceptionally high performance on the test data for predicting the Original Price, with an almost negligible error (MAE) of 0.0007296897175481192 and a nearly perfect score (R²) of 0.9999999999955044. However, these near-perfect results suggest the possibility of overfitting, where the model might have learned the training data too closely, including its noise and outliers, rather than capturing the underlying pattern. This concern arises because models that perform too well on the training data often struggle to generalize to new, unseen data, leading to less accurate predictions in real-world scenarios. While the model's high accuracy initially appears impressive, it raises questions about its ability to perform consistently across different datasets. 
  
  <img width="676" alt="Model 2 Result" src="./Images/regression_fit_plot_model_2.png"> <br>

This graph illustrates the `Ridge Regression` model's predictions, demonstrating the relationship between the target variable (e.g., 'Original_Price') and the 'Quantity' feature, juxtaposed with actual data points for contextual comparison.
  
</details>


<!-- Model 3 -->

<details>
<summary><b> Model 3 👇:</b></summary>
  
For the last model we used `Time Series Forecast` using Facebook's open source library `Prophet`, which was released as an open source on February 2017. We chose this model for its ease of use and because it automatically handles missing data, outliers, and holidays. However, because of it's limited features it may not be effective for many forecasting tasks.

  <details>
  <summary><b> Forecasting graph:</b></summary>
    <img width="668" alt="Model 3 Result1" src="./Images/Sales_Forecasting_Prophet.png"> <br>
  This graph illustrates a one year sales forecast based on historical data. Giving us a trend with the averages and a high and low amounts that we could expect. 
  </details>


  <details>
  <summary><b> Trend graph:</b></summary>
    <img width="668" alt="Model 3 Result2" src="./Images/forecast_sales_trend.png"> <br>
  In this trend graph, we could see that the trend line demonstrates a subtle decline with a high level of certainity for the first couple of months. Then the uncertainity boundries increases over time.
  </details>

  <details>
  <summary><b> Seasonality trend graph:</b></summary>
    <img width="668" alt="Model 3 Result3" src="./Images/Seasonality_forecast_Prophet.png"> <br>
  For the daily trend, we see that tuesdays are the high days and wednesdays are the low days. 
  For the yearly trend, we see that February tend to have the highest sales. Then comes April then August.
  </details>

</details>


## Summary

This project aimed to explore how different regions have their own unique shopping trends and customer behaviors. The main goal was to figure out what makes each area different, spot where there might be chances to sell more, and make shopping more tailored and enjoyable for customers. By looking at what people have bought in the past, the project tried to help businesses offer more of what customers in specific regions like. It also looked into how changes in seasons or local events affect what people buy in different places.

To do this, we used three types of computer programs or models. The first model was a simple one that tried to predict prices based on other information we know. The second model was a bit more complex and made sure we didn't rely too much on just one piece of information, making our predictions more reliable. The third model was special for looking at how things change over time, like predicting how sales might go up or down during different times of the year. We also made a special online page where anyone can see our findings in a clear and interactive way, making it easier to understand what we found out.

In conclusion, our analysis has provided valuable insights into regional purchasing behaviors, offering a foundational understanding for businesses aiming to tailor their strategies to diverse geographical markets. However, integrating profitability metrics for individual products and categories emerges as a compelling direction for future research. By adopting a more granular approach towards category-specific profitability, businesses could gain a deeper understanding of financial performance across different regions. This refined analysis would not only illuminate top-selling products but also highlight those contributing most significantly to revenue. Consequently, such an approach would enable businesses to craft more nuanced strategies, prioritizing not just volume of sales but also optimizing for higher profit margins.

---

### Contact Info:

<details>
<summary><b> Alaa Aleryani:</b></summary>   <br>
  <a href="mailto:alaaaleryani31@gmail.com">
    <img align="left" alt="Alaa's email" width="25px" height="25"
      src="https://cdn1.iconfinder.com/data/icons/google-new-logos-1/32/gmail_new_logo-256.png">
  </a> 
  <a href="https://www.linkedin.com/in/alaa-aleryani-6183a121b/"> 
    <img align="left" alt="Alaa's LinkedIn Page" width="25px" height="25"
      src="https://cdn2.iconfinder.com/data/icons/social-media-with-original-colors/256/icon-linkedin.png">
</a>
</details>


<br>


<details>
<summary><b> Yoeri Samwel:</b></summary> <br>
  <a href="mailto:yoerisamwel@gmail.com">
    <img align="left" width="25px" alt="Yoeri's email" src="https://cdn1.iconfinder.com/data/icons/google-new-logos-1/32/gmail_new_logo-256.png">
  </a>
  <a href="https://www.linkedin.com/in/yoeri-samwel-07301826"> 
    <img align="left" alt="Yoeri's LinkedIn Page" width="25px" height="25"
      src="https://cdn2.iconfinder.com/data/icons/social-media-with-original-colors/256/icon-linkedin.png">
</a>

</details>

 <br>

 ---
