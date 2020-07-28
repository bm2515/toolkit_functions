def identify_missing_dates(df):
    #Returns the total number of missing dates
    #Returns all records with missing dates
    pass


#strategy : [fill, drop]
#how: [default, zeros]
#rows: [all, int]
def handle_missing_dates(df, strategy='fill', how='default', rows='all'):
    pass

  
def identify_missing_features(df, baseline_features=None):
    #baseline_features is a list of given features which helps idenitify missing data in other columns
    #returns all records with missing features in one or more columns
    pass


#Strategy: [drop, fill]
#how: [next, prev, avg, groupby_avg: day, weekend, weekdays]
#rows: [all, int]
def handle_missing_features(df, strategy = 'fill', how='avg', rows='all'):
    pass

#Statistic: [mean, variance, standard deviation]
#Interval: monthly (M), weekly (W), weekdays (WD), weekend (WK), day (monday)
def resample_data(df, interval='W', statistic ='mean', weekend=['Fri', 'Sat']):
    #Interval: monthly, weekly, weekdays, weekend, day (successive Mondays)
    pass

    
def compute_statistic(df, feature, statistic = 'mean'):
    #Statistics = mean, median, standard deviation, variance
    pass


def reformat_date(df, format='%Y/%M/%D'):
    #Reformats date from String to DateTime
    pass

#strategy: replace, scale
#lambda x: x.replace()
#function: lambda x: x * 1000
def reformat_feature(df, feature,strategy='scale', function= lambda x : x * 1000):
    pass

#graphs: ['histogram', 'bubble_chart', 'line_chart', 'donut_histogram', 'scatter_chart']
def visualize_data(df, y_label, x_label, title, graph = 'histogram'):
    pass


def rename_columns(df, old=[], new=[]):
    #old and new are list of column names
    pass


def add_weekday(df):
    pass


def describe_dataset(df, features='all', identify_missing_data='yes'):
    #computer statistics for the given features: mean, median, standard deviation, interquartatile range, max, min, etc.
    #Display data types for each feature and its labels
    #Display statistic for each feature : % of missing data in each column
    
    #Pseudocode Implementation
    import pandas as pd
    print(df.describe().to_string())
    if identify_missing_data:
        identify_missing_dates()
        identify_nontimestamp_missing_data()

    pass


def merge_dataframes(df_1, df_2, merge_on='feature'):
    pass


def normalize(df, strategy='default'):
    pass
