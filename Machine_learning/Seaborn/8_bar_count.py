#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

#loading dataset
df=sns.load_dataset("iris") #loading the dataset

#creating a histogram plot
sns.barplot(x="sepal_length",y="sepal_width",data=df,color='red')

#displaying the histogram plot
plt.show()