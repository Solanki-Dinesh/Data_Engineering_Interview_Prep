import numpy as np


# Using z-score
def detect_outliers_zscore(data):

    outliers = []

    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z_score = (i-mean)/std
        if np.abs(z_score) > threshold:
            outliers.append(i)

    return outliers


# Using IQR
def detect_outliers_iqr(data):

    outliers = []
    sorted(data)

    q1, q3 = np.percentile(data, [25, 75])

    iqr = q3 - q1

    lower_bound = q1 - 1.5*iqr
    upper_bound = q3 + 1.5*iqr

    for i in data:
        if i < lower_bound or i > upper_bound:
            outliers.append(i)

    return outliers


if __name__ == "__main__":

    dataset = [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

    outliers_zscore = detect_outliers_zscore(dataset)
    outliers_iqr = detect_outliers_iqr(dataset)

    print(outliers_zscore)
    print(outliers_iqr)


