#import project0.modules.Crime.crime as Crime

def test_tuple_length():
    from project0.modules.Crime import crime as Crime
    c_test = Crime.CrimeReport("", "", "", "", "", "", "", "", "", "")

    assert len(c_test.return_scene()) == 5
    assert len(c_test.return_officer()) == 5
    assert len(c_test.return_criminal()) == 5

def test_object_type():
    from project0.modules.Crime import crime as Crime
    c_test = Crime.CrimeReport("", "", "", "", "", "", "", "", "", "")
    assert type(c_test) == Crime.CrimeReport

    officer_test = Crime.Officer(c_test.return_officer())
    assert type(officer_test) == Crime.Officer

    scene_test = Crime.Scene(c_test.return_scene())
    assert type(scene_test) == Crime.Scene

    criminal_test = Crime.Criminal(c_test.return_criminal())
    assert type(criminal_test) == Crime.Criminal

def test_object_eq():
    from project0.modules.Crime import crime as Crime
    c_test = Crime.CrimeReport("", "", "", "", "", "", "", "", "", "")
    copy_test = c_test.__copy__()
    assert c_test == copy_test


