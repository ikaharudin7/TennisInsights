from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt
import os


# Create a Random Forest Classifier to determine what are the key features for ND to win a match 
ND_rally = pd.DataFrame()

file_path = os.path.join('MLModels/Djokovic/djokovic_rally.csv')
ND_rally = pd.read_csv(file_path)

# Add in statistic features
X = ND_rally.drop(['Match', 'Result', 'RallyWinners', 'RallyUFEs'], axis=1)
y = ND_rally['Result'].apply(lambda x:x[0] if isinstance(x, str) else x)

# Function to remove % sign and convert to float
def remove_percentage_sign(column):
    if column.dtype != 'object':
        return column
    return column.str.replace('%', '').astype(float)

X = X.apply(remove_percentage_sign)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Classifier and define K-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

cv_scores = cross_val_score(rf_classifier, X, y, cv=kf, scoring='accuracy')

# Predict and evaluate
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:\n' + report)

# Display Feature Importances
importances = rf_classifier.feature_importances_
feature_names = X.columns
feature_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)

print('Rally Statistic Feature Importances:')
print(feature_importances)

# Plotting the Feature Importances
plt.figure(figsize=(10,6))
plt.barh(feature_importances['Feature'], feature_importances['Importance'], color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Which Rally Statistics must Novak Djokovic Win to ')
plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature at the top
plt.show()

# NEXT is to do serve and return stats, and see which of those features are most important. 
# Then feed this into the next step of the neural network and train the data based on these features. 