from collections import defaultdict

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    @staticmethod
    def has_digit_in_name(title):
        return any(char.isdigit() for char in title)

    def count_entries_with_digits(self, column_name):
        return sum(self.df[column_name].apply(self.has_digit_in_name))

    def count_entries_per_category(self, category_column):
        category_counts = defaultdict(int)
        for category in self.df[category_column]:
            category_counts[category] += 1
        return category_counts

    def sort_results(self, data, reverse=True):
        return sorted(data.items(), key=lambda x: x[1], reverse=reverse)