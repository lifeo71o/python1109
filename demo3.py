import matplotlib.pyplot as plt
from sklearn import linear_model


regression1 = linear_model.LinearRegression()
features = [[1], [2], [3], [4]]
values = [3, 5, 7, 9]
plt.scatter(features,values)

plt.show()

# apply linear regression
regression1.fit(features, values)
print(type(regression1))  # put debug point here
print(f'coefficient={regression1.coef_}, intercept={regression1.intercept_}')
range1 = [-1, 100]
print(regression1.coef_ * range1 + regression1.intercept_)
print('score=', regression1.score(features, values))
# y=ax+b
plt.plot(range1, regression1.coef_ * range1 + regression1.intercept_, c='gray')
plt.scatter(features, values, c='g', marker='.')
plt.show()