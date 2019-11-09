import numpy as np
from sklearn import linear_model, datasets

diabetes = datasets.load_diabetes()
print(type(diabetes))
print("X, features shape is:", diabetes.data.shape)
print("Y, labels shape is:", diabetes.target.shape)
dataForTest = -50
data_train = diabetes.data[:dataForTest]
target_train = diabetes.target[:dataForTest]
print("data trained shape:", data_train.shape)
print("target trained shape:", target_train.shape)

data_test = diabetes.data[dataForTest:]
target_test = diabetes.target[dataForTest:]
print("data test shape:", data_test.shape)
print("target test shape:", target_test.shape)

regression1 = linear_model.LinearRegression()
regression1.fit(data_train, target_train)

print(regression1)

print('score:', regression1.score(data_test, target_test))

for i in range(dataForTest, 0):
    print(i)
    #print(data_test[i].shape, data_test[i])
    dataArray = np.array(data_test[i]).reshape(1, -1)
    #print(dataArray.shape, dataArray)
    print(f"predict={regression1.predict(dataArray)[0]:.1f}/actual:{target_test[i]}")