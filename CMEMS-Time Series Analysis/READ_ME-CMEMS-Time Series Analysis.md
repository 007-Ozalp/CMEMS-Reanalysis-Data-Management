# CMEMS Ocean Model Data Time Series Analysis

  Input Dataset: CMEMS Reanalysis Model Sea Surface Temperature from 1987 to 2019 (==Water Potential Temperature at 1st Vertical level).
  
  Programming language is in Python through Anaconda [Jupyter Lab](https://jupyter.org/).
  
  Python libraries: [Xarray](https://pypi.org/project/xarray/), [Numpy](https://pypi.org/project/numpy/), [Matplotlib](https://pypi.org/project/matplotlib/), [Seaborn](https://pypi.org/project/seaborn/), [Statsmodel](https://pypi.org/project/statsmodels/) and [Cartopy](https://pypi.org/project/Cartopy/)

. [TS_Analysis_file_conversion.ipynb](https://github.com/007-Ozalp/CMEMS-Reanalysis-Data-Management/blob/main/CMEMS-Time%20Series%20Analysis/TS_Analysis_file_conversion.ipynb) shows file conversion to use in Time Series Analysis. File format types are: 
  
            1D: .csv and .nc 
  
            2D: .nc

. [TS_PLOTS.ipynb](https://github.com/007-Ozalp/CMEMS-Reanalysis-Data-Management/blob/main/CMEMS-Time%20Series%20Analysis/TS_PLOTS.ipynb) contains:

        1D .CSV file format
        
           1.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea.

           2.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea **Annual Boxplot**.

           3.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea **Monthly Boxplot**.

           4.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea **Monthly Violin plot**.

           5.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea **Monthly Cat plot**.


. [TS_PLOTS_SEASONAL.ipynb](https://github.com/007-Ozalp/CMEMS-Reanalysis-Data-Management/blob/main/CMEMS-Time%20Series%20Analysis/TS_PLOTS_SEASONAL.ipynb) contains:

         1D .NC file format
        
           1.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea.

           2.Temperature at Sea Surfacefrom 1987 to 2019 over Adriatic Sea within **Histogram**.

           3.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea-Season **Winter**.

           4.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea-Season **Summer**.

           5.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea-Season **Spring**.

           6.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea-Season **Autumn**.

           7.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea-**Box Plot by Season**.
           
           8.Temperature at Sea Surface from 1987 to 2019 over Adriatic Sea-**Violin Plot by Season**.


. [TS_PLOTS_SEASONAL_SCATTER.ipynb](https://github.com/007-Ozalp/CMEMS-Reanalysis-Data-Management/blob/main/CMEMS-Time%20Series%20Analysis/TS_PLOTS_SEASONAL_SCATTER.ipynb) contains:

            ADRIATIC SEA PHYSICS REANALYSIS-MEAN Temperature per Season within **Scatter plot**. 

. [TS_2D_SEASONAL_PLOTS.ipynb](https://github.com/007-Ozalp/CMEMS-Reanalysis-Data-Management/blob/main/CMEMS-Time%20Series%20Analysis/TS_2D_SEASONAL_PLOTS.ipynb) displays **2D maps for the Mean TS analysis**.

. [Rolling_month_year.ipynb](https://github.com/007-Ozalp/CMEMS-Reanalysis-Data-Management/blob/main/CMEMS-Time%20Series%20Analysis/Rolling_month_year.ipynb) contains:
 
              ################################################????????????????????????????????????????????????????????################################################
              
         1D .NC file format
         
            1. Sea Surface Temperature from 1987 to 2019 over Adriatic Sea.
            
            2. Mean Sea Surface Temperature from 1987 to 2019 over Adriatic Sea within TS by year. 
            
            3. Mean Sea Surface Temperature from 1987 to 2019 over Adriatic Sea within TS by month.
            
            4. Rolling Mean=12 Sea Surface Temperature by MONTH from 1987 to 2019 over Adriatic Sea.
            
            5. Rolling Mean=33 Sea Surface Temperature by YEAR from 1987 to 2019 over Adriatic Sea.
           
             ################################################????????????????????????????????????????????????????????################################################
