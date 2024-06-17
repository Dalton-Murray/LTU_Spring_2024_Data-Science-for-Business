#####################
## Dalton Murray    #
## 03/26/2024       #
## Final Project    #
#####################
## Import libraries and set alias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

## Import select functions from modules
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score

## Load dataset
originalData = pd.read_csv("./predictive_maintenance.csv")

## Basic statistics
print("Predictive maintenance original data head:\n", originalData.head(10))
print("\nPredictive maintenance original data describe:\n", originalData.describe())

## Basic visualizations for insight
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 12))
fig.tight_layout(pad=5.0)

# Plotting histograms for numerical features
sns.histplot(originalData["Air temperature [K]"], bins = 30, kde = True, ax = axes[0, 0])
axes[0, 0].set_title("Distribution of Air Temperature [K]")

sns.histplot(originalData["Process temperature [K]"], bins = 30, kde = True, ax = axes[0, 1])
axes[0, 1].set_title("Distribution of Process Temperature [K]")

sns.histplot(originalData["Rotational speed [rpm]"], bins = 30, kde = True, ax = axes[1, 0])
axes[1, 0].set_title("Distribution of Rotational Speed [rpm]")

sns.histplot(originalData["Torque [Nm]"], bins = 30, kde = True, ax = axes[1, 1])
axes[1, 1].set_title("Distribution of Torque [Nm]")

sns.histplot(originalData["Tool wear [min]"], bins = 30, kde = True, ax = axes[2, 0])
axes[2, 0].set_title("Distribution of Tool Wear [min]")

# Removing the empty subplot
axes[2, 1].set_visible(False)

plt.show()

sns.set_theme(style = "whitegrid")

# Create a pairplot to visualize the relationships between continuous variables
sns.pairplot(originalData, hue = "Target", vars=["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"])
plt.show()

# Visualize categorical data distribution
fig, axs = plt.subplots(1, 2, figsize = (14, 6))

sns.countplot(data = originalData, x = "Type", ax = axs[0], palette = "coolwarm").set_title("Distribution of Product Types")
sns.countplot(data = originalData, x = "Failure Type", ax = axs[1], palette="coolwarm").set_title("Distribution of Failure Types")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# Convert relevant columns to numeric if needed and drop non-numeric columns for correlation analysis
numeric_data = originalData.select_dtypes(include = ["float64", "int64"])

# Calculate the correlation matrix
correlation_matrix = numeric_data.corr()

# Plot the correlation heatmap
plt.figure(figsize = (10, 8))
sns.heatmap(correlation_matrix, annot = True, cmap = "coolwarm", fmt = ".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.show()

## Dataset preparation
# After analysis there is no real pre-processing that needs to be done, no dimension reduction is required, no outlier removal, and no data cleansing is necessary, standardization is already in place
# The only real things I need to do are prepare it for partitioning and training

# Map any failure type other than "No Failure" to 1 and "No Failure" to 0
originalData["Target"] = (originalData["Failure Type"] != "No Failure").astype(int)

# Define the features to be scaled and the categorical features
numericFeatures = ["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"]
categoricalFeatures = ["Type"]  # "Type" remains as a categorical feature

# Preprocessor configuration
preprocessorFinal = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numericFeatures),
        ("cat", OneHotEncoder(), categoricalFeatures)
    ],
    remainder = "drop"  # Drop other non-relevant columns
)

# Apply transformations to the data
processedFeatures = preprocessorFinal.fit_transform(originalData.drop(["Target", "UDI", "Product ID", "Failure Type"], axis = 1))

# Extract feature names for the new DataFrame
transformedFeatureNames = preprocessorFinal.named_transformers_["cat"].get_feature_names_out(categoricalFeatures)
newFeatureNames = numericFeatures + list(transformedFeatureNames)

# Create DataFrame for the transformed features
processedFeatures_df = pd.DataFrame(processedFeatures, columns = newFeatureNames)
processedFeatures_df["Target"] = originalData["Target"]

## Data partition
X = processedFeatures_df.drop("Target", axis = 1)
y = processedFeatures_df["Target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42, stratify = y)

## Training/Testing
k_values = [1, 3, 5, 7, 10, 15] # 3, 7, 15
knn_models = {}
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    knn_models[k] = knn

## Evaluation
for k in knn_models:
    y_pred = knn_models[k].predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    misclassification_error = 1 - accuracy

    # Print formatted output
    print(f"K={k}:")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"Misclassification Error: {misclassification_error:.3f}")
    print("Confusion Matrix:")
    print("\t\tPredicted: No    Predicted: Yes")
    print(f"Actual: No     {cm[0,0]:<12} {cm[0,1]:<14}")
    print(f"Actual: Yes    {cm[1,0]:<12} {cm[1,1]:<14}")
    print("\n")