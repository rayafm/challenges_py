def decayed_followers(intl_followers, fraction_lost_daily, days):
    exp_decay = (1-fraction_lost_daily)**days
    remain_fllwrs = intl_followers * exp_decay
    return remain_fllwrs