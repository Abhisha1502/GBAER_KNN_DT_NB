from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def split_data(df):
    """
    Split features and target into train and test sets
    """
    X = df.drop('Pollution_Severity', axis=1)
    y = df['Pollution_Severity']

    return train_test_split(
        X, y, test_size=0.2, random_state=42
    )


def train_naive_bayes(X_train, y_train):
    model = GaussianNB()
    model.fit(X_train, y_train)
    return model


def train_knn(X_train, X_test, y_train, y_test):
    """
    Train KNN and select best K
    """
    best_k = 1
    best_accuracy = 0

    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        acc = accuracy_score(y_test, knn.predict(X_test))

        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k

    final_knn = KNeighborsClassifier(n_neighbors=best_k)
    final_knn.fit(X_train, y_train)

    return final_knn, best_k


def train_decision_tree(X_train, y_train):
    model = DecisionTreeClassifier(
        max_depth=5,
        min_samples_split=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model
