#importing packages
import seaborn as sns #advanced visualization
import pandas as pd
import matplotlib.pyplot as plt # for basic visualization

#df=pd.read_csv("exam_marks.csv")


#creating a count plot
#sns.scatterplot(x="hours",y="marks",data=df)

#displaying the count plot
#plt.show()


example1_data=pd.DataFrame({'x':[6.83,6.56,0,5.67,8.67],
                            'y':[78.5,76.74,78.68,78.68]})

print(example1_data) #displaying example 1 dataframe

x=example1_data['x'].values.reshape(-1,1) #choosing input values
y=example1_data['y'].values.reshape(-1,1) #choosing output values

from sklearn.linear_model import LinearRegression #importing algo
linear_regressor=LinearRegression()#initalising algorithm
linear_regressor.fit(x,y)#training the algo on our data
print('[info] linear regression model training complete....')

m=linear_regressor.coef_[0][0]
c=linear_regressor.intercept_[0]

print(f"m value is:{m}")
print(f"c value is:{c}")
print(f"equation of line is:y={m}x+c")

new_user_input=float(input("enter the no.of hours:"))
new_user_input=[[new_user_input]]
new_output=linear_regressor.predict(new_user_input)[0]
print(f"when x = {new_user_input} , y = {new_output}")
