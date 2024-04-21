#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

df=sns.load_dataset("iris") #loading the dataset

#creating a count plot
sns.scatterplot(x="sepal_length",y="petal_length",data=df,hue='species',size='species')#size='species'

#displaying the count plot
plt.show()