import ml

def test_month_length():
    assert ml.month_length("January") == 31, "failed on January"
    assert ml.month_length("February") == 28, "failed on February"
    assert ml.month_length("February", leap_year=True) == 29, "failed on February, leap_year"
    assert ml.month_length("March") == 31, "failed on March"
    assert ml.month_length("April") == 30, "failed on April"
    assert ml.month_length("May") == 31, "failed on May"
    assert ml.month_length("June") == 30, "failed on June"
    assert ml.month_length("July") == 31, "failed on July"
    assert ml.month_length("August") == 31, "failed on August"
    assert ml.month_length("September") == 30, "failed on September"
    assert ml.month_length("October") == 31, "failed on October"
    assert ml.month_length("November") == 30, "failed on November"
    assert ml.month_length("December") == 31, "failed on December"
    assert ml.month_length("Month") == None, "failed on invalid input"