import pandas as pd


class PandasDataAnalyzer:

    REQUIRED_COLUMNS = [
        "Customer", "Age", "Income", "Experience", "Purchased"
    ]

    NUMERICAL_COLUMNS = [
        "Age", "Income", "Experience", "Purchased"
    ]

    def __init__(self, data):
        self.data = data
        self.df = None
        self.cleaned_df = None

    def validate_input(self):
        if not isinstance(self.data, list) or len(self.data) == 0:
            raise ValueError("Input must be a non-empty list.")

        for index, record in enumerate(self.data):
            if not isinstance(record, dict):
                raise ValueError(
                    f"Record {index + 1} must be a dictionary."
                )

            missing_columns = [
                column for column in self.REQUIRED_COLUMNS
                if column not in record
            ]

            if missing_columns:
                raise ValueError(
                    f"Missing required columns: {missing_columns}"
                )

            customer = record["Customer"]

            if not isinstance(customer, str) or not customer.strip():
                raise ValueError(
                    f"Record {index + 1}: Customer must be a non-empty string."
                )

            for column in self.NUMERICAL_COLUMNS:
                value = record[column]

                if value is None or pd.isna(value):
                    continue

                if isinstance(value, bool) or not isinstance(
                    value, (int, float)
                ):
                    raise ValueError(
                        f"Record {index + 1}: {column} must be numeric."
                    )

            purchased = record["Purchased"]

            if not pd.isna(purchased) and purchased not in (0, 1):
                raise ValueError("Purchased must be 0 or 1.")

        print("Input validation successful.")
        return True

    def create_dataframe(self):
        self.df = pd.DataFrame(
            self.data,
            columns=self.REQUIRED_COLUMNS
        )

        for column in self.NUMERICAL_COLUMNS:
            self.df[column] = pd.to_numeric(
                self.df[column], errors="raise"
            )

        print("\nORIGINAL DATAFRAME")
        print(self.df.to_string(index=False))

        return self.df

    def get_dataset_info(self):
        if self.df is None:
            raise ValueError("Create DataFrame first.")

        print("\nDATASET INFORMATION")
        print("Rows:", self.df.shape[0])
        print("Columns:", self.df.shape[1])
        print("Column names:", list(self.df.columns))
        print("Shape:", self.df.shape)

        print("\nData types:")
        print(self.df.dtypes)

        return self.df.dtypes

    def find_missing_values(self):
        if self.df is None:
            raise ValueError("Create DataFrame first.")

        missing = self.df.isnull().sum()

        print("\nMISSING VALUES BY COLUMN")
        print(missing)

        return missing

    def count_missing_values(self):
        if self.df is None:
            raise ValueError("Create DataFrame first.")

        total = int(self.df.isnull().sum().sum())

        print("\nTotal missing values:", total)

        return total

    def find_duplicates(self):
        if self.df is None:
            raise ValueError("Create DataFrame first.")

        duplicates = self.df[self.df.duplicated()].copy()

        print("\nDUPLICATE RECORDS")
        print("Duplicate count:", len(duplicates))

        if not duplicates.empty:
            print(duplicates.to_string(index=False))

        return duplicates

    def remove_duplicates(self):
        if self.df is None:
            raise ValueError("Create DataFrame first.")

        self.cleaned_df = (
            self.df.drop_duplicates()
            .reset_index(drop=True)
            .copy()
        )

        print("\nRows after removing duplicates:", len(self.cleaned_df))

        return self.cleaned_df

    def fill_missing_values(self):
        if self.cleaned_df is None:
            raise ValueError("Remove duplicates before filling missing values.")

        missing_count = int(
            self.cleaned_df["Income"].isnull().sum()
        )

        if missing_count > 0:
            income_mean = self.cleaned_df["Income"].mean()

            if pd.isna(income_mean):
                raise ValueError(
                    "Cannot fill Income because all Income values are missing."
                )

            self.cleaned_df["Income"] = (
                self.cleaned_df["Income"].fillna(income_mean)
            )

            print("\nIncome mean used:", round(float(income_mean), 2))
            print("Income values filled:", missing_count)

        else:
            print("\nNo missing Income values found.")

        print(
            "Remaining missing Income values:",
            int(self.cleaned_df["Income"].isnull().sum())
        )

        return self.cleaned_df

    def filter_customers(self, min_income):
        if self.cleaned_df is None:
            raise ValueError("Clean the dataset before filtering.")

        if (
            isinstance(min_income, bool)
            or not isinstance(min_income, (int, float))
        ):
            raise ValueError("Minimum income must be numeric.")

        result = self.cleaned_df[
            self.cleaned_df["Income"] >= min_income
        ].copy()

        print(f"\nCUSTOMERS WITH INCOME >= {min_income}")
        print(result.to_string(index=False))

        return result

    def sort_by_income(self, ascending=True):
        if self.cleaned_df is None:
            raise ValueError("Clean the dataset before sorting.")

        if not isinstance(ascending, bool):
            raise ValueError("Ascending must be True or False.")

        result = self.cleaned_df.sort_values(
            by="Income",
            ascending=ascending
        ).reset_index(drop=True)

        order = "Ascending" if ascending else "Descending"

        print(f"\nINCOME SORTED: {order}")
        print(result.to_string(index=False))

        return result

    def calculate_statistics(self):
        if self.cleaned_df is None:
            raise ValueError("Clean the dataset before calculating statistics.")

        statistics = self.cleaned_df[
            self.NUMERICAL_COLUMNS
        ].agg(["mean", "min", "max", "std"]).T

        statistics.columns = [
            "Mean", "Minimum", "Maximum", "Std Dev"
        ]

        print("\nNUMERICAL STATISTICS")
        print(statistics.round(2).to_string())

        return statistics

    def analyze_features(self):
        if self.cleaned_df is None:
            raise ValueError("Clean the dataset before feature analysis.")

        print("\nFEATURE ANALYSIS")

        for column in self.NUMERICAL_COLUMNS:
            values = self.cleaned_df[column]

            print(f"\n{column}")
            print("Mean:", round(float(values.mean()), 2))
            print("Minimum:", values.min())
            print("Maximum:", values.max())
            print(
                "Standard deviation:",
                round(float(values.std()), 2)
            )

    def analyze_target(self):
        if self.cleaned_df is None:
            raise ValueError("Clean the dataset before target analysis.")

        counts = self.cleaned_df["Purchased"].value_counts()

        result = {
            "Purchased": int(counts.get(1, 0)),
            "Not Purchased": int(counts.get(0, 0))
        }

        print("\nPURCHASE ANALYSIS")
        print("Purchased (1):", result["Purchased"])
        print("Not Purchased (0):", result["Not Purchased"])

        return result

    def perform_eda(self):
        if self.cleaned_df is None:
            raise ValueError("Clean the dataset before performing EDA.")

        df = self.cleaned_df

        result = {
            "Customer Count": len(df),
            "Average Age": df["Age"].mean(),
            "Average Income": df["Income"].mean(),
            "Highest Income": df["Income"].max(),
            "Average Experience": df["Experience"].mean(),
            "Number of Purchasers": int(
                (df["Purchased"] == 1).sum()
            )
        }

        print("\nEXPLORATORY DATA ANALYSIS")

        for name, value in result.items():
            if isinstance(value, float):
                value = round(value, 2)

            print(f"{name}: {value}")

        return result

    def group_by_purchase_status(self):
        if self.cleaned_df is None:
            raise ValueError("Clean the dataset before grouping.")

        result = self.cleaned_df.groupby("Purchased").agg(
            Customer_Count=("Customer", "count"),
            Average_Age=("Age", "mean"),
            Average_Income=("Income", "mean"),
            Average_Experience=("Experience", "mean")
        )

        result.index = result.index.map({
            0: "Not Purchased",
            1: "Purchased"
        })

        print("\nGROUP ANALYSIS BY PURCHASE STATUS")
        print(result.round(2).to_string())

        return result

    def display_report(self):
        if self.df is None or self.cleaned_df is None:
            raise ValueError("Complete the cleaning workflow first.")

        print("\n" + "=" * 55)
        print("CUSTOMER DATA ANALYSIS")
        print("=" * 55)

        print("Original Dataset Shape:", self.df.shape)

        print(
            "Missing Income Values:",
            int(self.df["Income"].isnull().sum())
        )

        print(
            "Duplicate Records:",
            int(self.df.duplicated().sum())
        )

        print("Rows After Cleaning:", len(self.cleaned_df))

        print("\nFEATURE STATISTICS")
        statistics = self.calculate_statistics()
        print(statistics.round(2).to_string())

        self.analyze_target()
        self.perform_eda()
        self.group_by_purchase_status()

        print("\nFINAL CLEANED DATASET")
        print(self.cleaned_df.to_string(index=False))

        print("=" * 55)


def run_test_cases():

    data = [
        {
            "Customer": "C001", "Age": 25, "Income": 30000,
            "Experience": 2, "Purchased": 0
        },
        {
            "Customer": "C002", "Age": 30, "Income": 45000,
            "Experience": 5, "Purchased": 1
        },
        {
            "Customer": "C003", "Age": 35, "Income": None,
            "Experience": 8, "Purchased": 1
        },
        {
            "Customer": "C004", "Age": 40, "Income": 80000,
            "Experience": 12, "Purchased": 1
        },
        {
            "Customer": "C005", "Age": 45, "Income": 100000,
            "Experience": 15, "Purchased": 0
        },
        {
            "Customer": "C002", "Age": 30, "Income": 45000,
            "Experience": 5, "Purchased": 1
        }
    ]

    # Test 1: Normal dataset
    test1 = PandasDataAnalyzer(data)
    test1.validate_input()
    test1.create_dataframe()

    assert test1.count_missing_values() == 1
    assert len(test1.find_duplicates()) == 1

    test1.remove_duplicates()
    test1.fill_missing_values()

    assert len(test1.cleaned_df) == 5
    assert test1.cleaned_df["Income"].isnull().sum() == 0

    print("\nTest 1 PASSED: Normal dataset")

    # Test 2: No missing values
    no_missing = [
        {
            **row,
            "Income": 50000 if row["Income"] is None else row["Income"]
        }
        for row in data
    ]

    test2 = PandasDataAnalyzer(no_missing)
    test2.validate_input()
    test2.create_dataframe()

    assert test2.count_missing_values() == 0

    print("Test 2 PASSED: No missing values")

    # Test 3: Multiple missing Income values
    multiple_missing = [row.copy() for row in data]

    multiple_missing[0]["Income"] = None
    multiple_missing[1]["Income"] = None
    multiple_missing[2]["Income"] = None

    test3 = PandasDataAnalyzer(multiple_missing)
    test3.validate_input()
    test3.create_dataframe()
    test3.remove_duplicates()
    test3.fill_missing_values()

    assert test3.cleaned_df["Income"].isnull().sum() == 0

    print("Test 3 PASSED: Multiple missing values")

    # Test 4: Duplicate records
    test4 = PandasDataAnalyzer(data + [data[0].copy()])
    test4.validate_input()
    test4.create_dataframe()

    assert len(test4.find_duplicates()) == 2

    test4.remove_duplicates()

    assert len(test4.cleaned_df) == 5

    print("Test 4 PASSED: Duplicate detection and removal")

    # Test 5: Missing required column
    invalid_data = [
        {
            "Customer": "C001",
            "Age": 25,
            "Experience": 2,
            "Purchased": 0
        }
    ]

    try:
        PandasDataAnalyzer(invalid_data).validate_input()
        raise AssertionError("Missing column was not detected.")

    except ValueError as error:
        assert "Income" in str(error)
        print("Test 5 PASSED: Missing required column")

    # Test 6: Empty dataset
    try:
        PandasDataAnalyzer([]).validate_input()
        raise AssertionError("Empty dataset was not detected.")

    except ValueError:
        print("Test 6 PASSED: Empty dataset")

    # Test 7: Filtering
    test7 = PandasDataAnalyzer(data)
    test7.validate_input()
    test7.create_dataframe()
    test7.remove_duplicates()
    test7.fill_missing_values()

    filtered = test7.filter_customers(50000)

    assert (filtered["Income"] >= 50000).all()

    print("Test 7 PASSED: Income filtering")

    print("\nAll seven test cases passed successfully.")


def main():

    data = [
        {
            "Customer": "C001", "Age": 25, "Income": 30000,
            "Experience": 2, "Purchased": 0
        },
        {
            "Customer": "C002", "Age": 30, "Income": 45000,
            "Experience": 5, "Purchased": 1
        },
        {
            "Customer": "C003", "Age": 35, "Income": None,
            "Experience": 8, "Purchased": 1
        },
        {
            "Customer": "C004", "Age": 40, "Income": 80000,
            "Experience": 12, "Purchased": 1
        },
        {
            "Customer": "C005", "Age": 45, "Income": 100000,
            "Experience": 15, "Purchased": 0
        },
        {
            "Customer": "C002", "Age": 30, "Income": 45000,
            "Experience": 5, "Purchased": 1
        }
    ]

    try:
        analyzer = PandasDataAnalyzer(data)

        analyzer.validate_input()
        analyzer.create_dataframe()
        analyzer.get_dataset_info()
        analyzer.find_missing_values()
        analyzer.count_missing_values()
        analyzer.find_duplicates()
        analyzer.remove_duplicates()
        analyzer.fill_missing_values()
        analyzer.filter_customers(50000)
        analyzer.sort_by_income(ascending=True)
        analyzer.sort_by_income(ascending=False)
        analyzer.calculate_statistics()
        analyzer.analyze_features()
        analyzer.perform_eda()
        analyzer.analyze_target()
        analyzer.group_by_purchase_status()
        analyzer.display_report()

        run_test_cases()

    except (ValueError, TypeError, KeyError) as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()