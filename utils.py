from constants import SIMPLE_DAY_FORMAT, VERBOSE_DATE_FORMAT

from datetime import datetime

def formated_date(verbose):
    format =  VERBOSE_DATE_FORMAT if verbose else SIMPLE_DAY_FORMAT
    date = datetime.now()
    return date.strftime(format)
