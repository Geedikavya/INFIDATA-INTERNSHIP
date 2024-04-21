#Displot is used basically plot distribution of continous data
#distribution plot
#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

#loading dataset
df=sns.load_dataset("iris") #loading the dataset

#creating a distribution plot
sns.displot(df['sepal_width'],color='b')
plt.show()#displaying the plot