import json
import pandas as pd

class FewShotPosts:
    def __init__(self, file_path= 'data/processed_posts.json'):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)


    def load_posts(self, file_path):
        with open(file_path,encoding='utf-8') as f:
            post = json.load(f)
            df = pd.json_normalize(post)
            df['Length'] = df['Line_count'].apply(self.categorize_length)
            self.df = df
            all_tags = df['tags'].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))
        return self.unique_tags 

    def get_tags(self):
        return self.unique_tags


    def categorize_length(self, Line_count):
        if Line_count <= 3:
            return 'short'
        elif 3 <  Line_count <= 8:
            return 'medium'
        else:
            return 'Long'

    def get_filtered_post(self, length, language,tag):
        mask = pd.Series(True, index=self.df.index)  # Start with all rows as True

        if length:
            mask &= self.df['Length'] == length  # Filter by length

        if language:
            mask &= self.df['Language'] == language  # Filter by language

        if tag:
            mask &= self.df['tags'].apply(lambda tags:tag in tags)  # Filter by tags

            df_filtered = self.df[mask]

        return  df_filtered.to_dict(orient = 'records')  # Return the filtered DataFrame


    
if __name__ == '__main__':
    fs = FewShotPosts()
    post = fs.get_filtered_post('short', 'English','Finance')
    print(post)
    pass 

