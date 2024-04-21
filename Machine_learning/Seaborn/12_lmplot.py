#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization

df=sns.load_dataset("iris") #loading the dataset

#creating a count plot
sns.lmplot(x="petal_length",y='petal_width',data=df)

#displaying the count plot
plt.show()