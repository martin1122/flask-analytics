from .csv_loader import load_dataset
from .dataset_operations import merge_datasets_by_fields, get_entries_after
from .datetime_operations import get_beginning_of_the_week_date


def get_summary(site_name):
    voc_dataset = load_dataset(site_name, 'voc')
    cc_dataset = load_dataset(site_name, 'cc')

    merged_dataset = merge_datasets_by_fields(voc_dataset, cc_dataset, ['EndDate'])
    merged_dataset = get_entries_after(merged_dataset, get_beginning_of_the_week_date())

    return {
        'week': {
            'reviews': len(merged_dataset),
            'promoters': 99,
            'passives': 99,
            'detractors': 99
        },
        'month': {
            'reviews': 99,
            'promoters': 99,
            'passives': 99,
            'detractors': 99
        },
    }


def addition(a, b):
    return a + b