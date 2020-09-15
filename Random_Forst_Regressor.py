#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset
df=pd.read_csv('Position_Salaries.csv')
X=df.iloc[:,1:2].values
y=df.iloc[:,2].values

#fitting the random forest regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=300,random_state=0)
regressor.fit(X,y)

#predicting a new result
y_pred=regressor.predict(np.array([[6.5]]))

#visualising the regression results (for higher resolution and smoother curve)
X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('Random Forest Regressor')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()