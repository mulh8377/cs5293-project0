#import project0.modules.Crime.crime as Crime

def test_tuple_length():
    import project0.modules.Crime.crime as Cr
    c_test = Cr.CrimeReport("", "", "", "", "", "", "", "", "", "", "")

    assert len(c_test.return_scene()) == 5
    assert len(c_test.return_officer()) == 5
    assert len(c_test.return_criminal()) == 5

def test_object_type():
    import project0.modules.Crime.crime as Cr
    c_test = Cr.CrimeReport("", "", "", "", "", "", "", "", "", "", "")
    assert type(c_test) == Cr.CrimeReport

    officer_test = Cr.Officer(c_test.return_officer())
    assert type(officer_test) == Cr.Officer

    scene_test = Cr.Scene(c_test.return_scene())
    assert type(scene_test) == Cr.Scene

    criminal_test = Cr.Criminal(c_test.return_criminal())
    assert type(criminal_test) == Cr.Criminal

def test_object_eq():
    import project0.modules.Crime.crime as Cr
    c_test = Cr.CrimeReport("", "", "", "", "", "", "", "", "", "", "")
    copy_test = c_test.__copy__()
    assert c_test == copy_test


