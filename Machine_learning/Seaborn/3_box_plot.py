#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

#box plot
#loading dataset
df=sns.load_dataset("iris") #loading the dataset


#creating a boxplot
sns.boxplot(x="species",y="sepal_width",data=df,palette='Set2')
plt.show()#displaying the boxplot