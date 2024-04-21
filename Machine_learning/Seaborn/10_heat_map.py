#importing packages
import seaborn as sns #advanced visualization
import matplotlib.pyplot as plt # for basic visualization
df=sns.load_dataset("iris") #loading the dataset

df['species']=df['species'].map({'setosa:1,'
                                 'versicolor':2,
                                 'virginica':3})
correlation=df.corr()#getting correlation matrix
#creating a plot of correlation matrix as heatmap
sns.heatmap(correlation,cbar=True,
            annot=True,linewidth=0.5,
            cmap='Blues')#displaying plot
plt.show()
#positive correlation is represented as light
#negative correlation is represented as dark
