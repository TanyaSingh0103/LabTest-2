from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(df[:10])

df.describe()

target = iris.target
print(target)


import seaborn as sbn

sbn.heatmap(df)

sbn.boxplot(df) #before scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(iris.data)

sbn.boxplot(X_scaled) #after scaling

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, target, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train, Y_train)

y_pred = lr.predict(X_test)
print(y_pred)

from sklearn.metrics import classification_report

print(classification_report(Y_test, y_pred))


