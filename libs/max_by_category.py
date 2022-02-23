# 6. 각 카테고리별 최대 소비액 데이터
def max_by_category(self):
    max_by_category = dict()

    for x in categories:
        max_by_category[x] = 0

    for _, data in self.df.iterrows():
        if (
            data["Price(\)"] < 0
            and max_by_category[data["Category"]] > data["Price(\)"]
        ):
            max_by_category[data["Category"]] = data["Price(\)"]

    colnames = ["Category", "Price(\)"]
    categorical_max_df = pd.DataFrame(list(max_by_category.items()), columns=colnames)
    categorical_max_df.set_index("Category", inplace=True)
    print("# Maximum consumption for each category.")
    return categorical_max_df
