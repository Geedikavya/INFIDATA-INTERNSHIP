#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

#violin plot
#loading dataset
df=sns.load_dataset("iris") #loading the dataset


#creating a violinplot
sns.violinplot(x="species",y="sepal_width",data=df)
plt.show()#displaying the violinplot