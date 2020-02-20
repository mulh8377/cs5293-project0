def test_insert():
    import project0.modules.Storage.tosstorage as St
    import project0.modules.Crime.crime as Cr
    import subprocess
    c_test = Cr.CrimeReport("test", "test", "test", "test", "test", "test", "test", "test", "test", "test", "test")
    summary = c_test.return_report()
    assert len(summary) == 11
    print(summary)
    St.insert_into_crime_report(c_test.return_report())
    #subprocess.call(["bash", "./scripts/toss-csv.sh"])
    assert True == True

def test_fetch_table():
    import project0.modules.Storage.tosstorage as St
    storage = St.fetch_CrimeReport_table()
    assert len(storage) > 0
    print(storage)

def test_fetch_value():
    import project0.modules.Storage.tosstorage as St
    storage1 = St.fetch_CrimeReport_value(field="arresttime", val="test")
    print(storage1)
    storage2 = St.fetch_CrimeReport_value(field="casenumber", val="test")
    storage3 = St.fetch_CrimeReport_value(field="arrest_location", val="test")
    storage4 = St.fetch_CrimeReport_value(field="offense", val="test")
    storage5 = St.fetch_CrimeReport_value(field="arresteename", val="test")
    storage6 = St.fetch_CrimeReport_value(field="arresteebirthday", val="test")

    storage7 = St.fetch_CrimeReport_value(field="city", val="test")

    storage8 = St.fetch_CrimeReport_value(field="state", val="test")
    storage9 = St.fetch_CrimeReport_value(field="zip", val="test")
    storage10 = St.fetch_CrimeReport_value(field="status", val="test")
    storage11 = St.fetch_CrimeReport_value(field="officer", val="test")


