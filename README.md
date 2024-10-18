# Time Series Stationarity Transformation

This Python script helps to make a time series stationary using statistical tests such as the Augmented Dickey-Fuller (ADF) test, Phillips-Perron (PP) test, and Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test. It iteratively applies differencing to the time series until it becomes stationary based on the specified significance level.

Features
Augmented Dickey-Fuller (ADF) Test: Checks for stationarity by testing if a unit root is present in the time series.
Phillips-Perron (PP) Test: A complementary unit root test to confirm results from the ADF test.
KPSS Test: Tests for stationarity by checking if the time series is trend-stationary.
Differencing: Automatically applies differencing to the time series until the chosen test indicates stationarity.
Prerequisites
To run this script, you need the following Python libraries installed:

numpy
pandas
statsmodels

Code Explanation
ADF Test: The Augmented Dickey-Fuller test checks if the time series has a unit root (non-stationary). The function iteratively differences the series if the p-value is above the significance level (alpha).

PP Test: Phillips-Perron test is used as a complementary test to ADF, providing an additional check for stationarity.

KPSS Test: Unlike ADF and PP, KPSS tests if the series is trend-stationary. Here, we continue differencing until the p-value is above the alpha threshold, indicating stationarity.

Differencing: If any of the tests indicate non-stationarity, differencing is applied iteratively to the time series. The differencing level is incremented each time until the series becomes stationary.

Return: The function returns the first five rows of the transformed time series after stationarity is achieved.

Limitations
The script assumes that the input is a univariate time series.
It may not be suitable for cases where advanced preprocessing (e.g., handling seasonality) is required.
It performs differencing only; other transformations (e.g., log transformation) are not considered.
Future Enhancements
Add support for other stationarity transformation techniques (e.g., log transformation).
Include automatic handling of seasonal components in the time series.
Allow for more flexible choices of differencing order and transformation.

Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or feature requests.
