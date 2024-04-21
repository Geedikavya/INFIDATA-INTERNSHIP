#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

df=sns.load_dataset("iris") #loading the dataset

#creating a count plot
sns.countplot(x="sepal_length",hue="species",data=df,palette='Set2')

#displaying the count plot
plt.show()