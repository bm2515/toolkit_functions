def read_data(filename, keys=[]):
    #Keys is given list for JSON Data
    #Returns Pandas DataFrame
    pass


def identify_missing_dates(df):
    #Returns the total number of missing dates
    pass


def fill_missing_dates(df):
    #Using prev & next
    pass


def drop_missing_dates(df):
    pass
    
    
def identify_missing_features(df, baseline_features=None):
    #baseline_features is a list of given features which helps idenitify missing data in other columns
    pass


def drop_missing_data(df):
    pass


def fill_data_by_next(df):
    pass
    
    
def fill_data_by_previous(df):
    pass


def fill_data_by_average(df):
    pass
    
    
def fill_data_by_groupby_average(df, groupby='weekend', weekend=['Friday', 'Saturday']):
    #groupby: day (e.g Monday), weekdays, weekend
    pass
    
    
def resample_data(df, interval='weekly', weekend=['Friday', 'Saturday']):
    #Interval: monthly, weekly, weekdays, weekend, day (successive Mondays)
    pass

    
def compute_statistic(df, feature, statistic = 'mean'):
    #Statistics = mean, median, standard deviation, variance
    pass


def reformat_date(df, format='%Y/%M/%D'):
    #Reformats date from String to DateTime
    pass


def reformat_feature(df, feature,scaling_factor=1000):
    pass


def visualize_data(df, y_label, x_label, title):
    pass


def rename_columns(df, old=[], new=[]):
    #old and new are list of column names
    pass


def add_weekday(df):
    pass
