import peevee.ext4

def test_validate_good():
    path = u'/a/path/which/should/work'
    assert peevee.ext4.validate(path)

def test_validate_bad_filename():
    path = u'/a/path/which/shouldn\'t/work/..'
    assert not peevee.ext4.validate(path)

def test_validate_bad_length():
    path = (
        u'/a/verylongpathwithaverylongfilenamewhichiswrittendownhereandshouldn'
        u'everworkandnowthisisduplicatedafewtimesverylongpathwithaverylongfile'
        u'namewhichiswrittendownhereandshouldneverworkandnowthisisduplicatedaf'
        u'ewtimesverylongpathwithaverylongfilenamewhichiswrittendownhereandsho'
        u'uldneverworkandnowthisisduplicatedafewtimes/which/shouldn\'t/work'
    )
    assert not peevee.ext4.validate(path)

def test_validate_NUL():
    path = (
        u'/a/path/which/has/\u0000'
    )
    assert not peevee.ext4.validate(path)
