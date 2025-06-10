import pandas as pd


class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        # Get total number of rows
        total_rows = len(self)
        # Print in chunks of 10 rows
        for start in range(0, total_rows, 10):
            # Calculate end of current chunk
            end = min(start + 10, total_rows)
            # Print headers and current chunk
            print("\nColumns:", list(self.columns))
            print("-" * 100)  # Separator line
            print(super().iloc[start:end])


# Create instance and test
if __name__ == "__main__":
    # Create DFPlus instance from CSV
    dfp = DFPlus.from_csv("../csv/products.csv")

    # Print with headers every 10 lines
    dfp.print_with_headers()
