'''
This Python script is offered with no formal support from Stack Overflow. 
If you run into difficulties, reach out to the person who provided you with this script.
'''

# Standard Python libraries
import argparse

# Third-party libraries
from wordcloud import WordCloud
import pandas as pd


def main():

    args = get_args()
    wordcloud_data = process_data(args.csv)
    create_wordcloud(wordcloud_data, int(args.max_tags))


def get_args():

    parser = argparse.ArgumentParser(
        prog='so4t_tag_cloud.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Uses the CSV output from so4t_tag_report.py to '
        'create a word cloud of tag names based on page views.',
        epilog = 'Example for Stack Overflow Business: \n'
                'python3 so4t_tag_cloud.py --csv tag_report.csv --max-tags 100')
    parser.add_argument('--csv', help='Name of CSV file to create', default='tag_report.csv')
    parser.add_argument('--max-tags', help='Maximum number of tags to include in word cloud', default=100)

    return parser.parse_args()


def process_data(csv_file):

    # Read the CSV file into a Pandas DataFrame
    csv_columns = ['Tag Name', 'Total Page Views']
    data = pd.read_csv(csv_file, usecols=csv_columns, encoding='utf-8')

    # Convert the DataFrame to a list of dictionaries
    dict_data = data.to_dict('records')

    # Convert the list of dictionaries to a dictionary
    # The wordcloud library is expecting a dictionary of dictionaries
    wordcloud_data = {item['Tag Name']: item['Total Page Views'] for item in dict_data}

    return wordcloud_data


def create_wordcloud(wordcloud_data, max_tags):

    wordcloud = WordCloud(
        width=1600, 
        height=900, 
        max_words=max_tags,
        background_color='white')
    
    wordcloud.generate_from_frequencies(wordcloud_data)

    export_name = f'so4t_tag_cloud_{max_tags}_tags.html'
    wordcloud.to_file(export_name)
    print(f'Tag cloud image saved to {export_name}')


if __name__ == '__main__':

    main()

