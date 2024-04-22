#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

#strip plot
#loading dataset
df=sns.load_dataset("iris") #loading the dataset


#creating a strip plot
sns.stripplot(x="species",y="sepal_width",data=df,color='blue')
plt.show()#displaying the stripplot