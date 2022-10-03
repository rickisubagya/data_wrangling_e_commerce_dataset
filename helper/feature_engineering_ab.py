import numpy as np
import pandas as pd
from statsmodels.stats.proportion import power_proportions_2indep, test_proportions_2indep
from statsmodels.stats.weightstats import ttest_ind
from statsmodels.stats.power import tt_ind_solve_power

def feature_engineering_ab(df8):
    
    ab_test = df8
    
    # Convert timestamp into datetime format and sort by ascending value
    ab_test['timestamp'] = pd.to_datetime(ab_test['timestamp'])
    ab_test = ab_test.sort_values('timestamp')
    ab_test['date'] = ab_test['timestamp'].dt.date
    
    # Remove value with group control in new_page and vice versa
    ab_test = ab_test[(~(ab_test['group'] == 'control') & (ab_test['landing_page'] == 'new_page')) | (~(ab_test['group'] == 'treatment') & (ab_test['landing_page'] == 'old_page'))]
    
    # Drop duplicate user id
    ab_test = ab_test.drop_duplicates(subset=['user_id'], keep='first')
    
    # Groupby date the datasets and separate the control and treatment
    ab_test_temp = ab_test.groupby(['date', 'group']).agg(['count', 'sum']).unstack().reset_index()[['date', 'converted']].values
    ab_test_daily = pd.DataFrame(ab_test_temp, columns=['date', 'control_visit', 'treatment_visit', 'control_converted', 'treatment_converted'])
    
    # Calculate the conversion rate in group control and treatment
    ab_test_daily = ab_test_daily.set_index('date').cumsum().reset_index()
    ab_test_daily['control_conversion_rate'] = ab_test_daily['control_converted'] / ab_test_daily['control_visit']
    ab_test_daily['treatment_conversion_rate'] = ab_test_daily['treatment_converted'] / ab_test_daily['treatment_visit']
    
    # Calculate power
    n_obs = len(ab_test[ab_test['group'] == 'control']) + len(ab_test[ab_test['group'] == 'treatment'])
    test_split = len(ab_test[ab_test['group'] == 'treatment']) / (len(ab_test[ab_test['group'] == 'control']) + len(ab_test[ab_test['group'] == 'treatment']))
    ab_test_daily['power'] = ab_test_daily.apply(lambda x: power_proportions_2indep(diff=x['control_conversion_rate']*0.03,
                                                                                    prop2=x['control_conversion_rate'],
                                                                                    nobs1=(x['control_visit']+x['treatment_visit'])*test_split,
                                                                                    ratio=(1-test_split)/test_split,
                                                                                    alpha=0.05,
                                                                                    alternative='two-sided',
                                                                                    return_results=False),axis=1)
    
    # Calculate the p-value
    ab_test_daily['p_value'] = ab_test_daily.apply(lambda x: test_proportions_2indep(count1=x['treatment_converted'],
                                                                                     nobs1=x['treatment_visit'],
                                                                                     count2=x['control_converted'],
                                                                                     nobs2=x['control_visit'],
                                                                                     alternative='two-sided')[1], axis=1)
    
    return ab_test_daily