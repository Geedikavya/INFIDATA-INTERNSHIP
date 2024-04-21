#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

#loading dataset
data=sns.load_dataset("iris") #loading the dataset

#creating a histogram plot
sns.histplot(x="species",y="sepal_width",data=data)

#displaying the histogram plot
plt.show()