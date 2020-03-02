"""
:description:
            python file that can create objects related to the data we are mining.
            not currently used in the project.
"""


class CrimeReport:
    def __init__(self, date_of_arrest: str, case_no: str, loc_of_arrest: str, offense: str, arrestee: str,
                 dob_of_arrestee: str, city_of_arrest: str, state_of_arrest: str, zip_of_arrest: str, status: str, officer: str):
        self.arrest_date = date_of_arrest
        self.case_number = case_no
        self.arrest_location = loc_of_arrest
        self.arrest_offense = offense
        self.arrestee_identification = arrestee
        self.arrestee_birth = dob_of_arrestee
        self.arrest_city = city_of_arrest
        self.arrest_state = state_of_arrest
        self.arrest_zipcode = zip_of_arrest
        self.arrest_status = status
        self.arresting_officer = officer

    def return_report(self):
        return (self.arrest_date, self.case_number, self.arrest_location,
                self.arrest_offense, self.arrestee_identification, self.arrestee_birth,
                self.arrest_city, self.arrest_state, self.arrest_zipcode,
                self.arrest_status, self.arresting_officer)

    def __str__(self):
        return "Crime Report Object"

    def __eq__(self, other):
        return self.case_number == other.case_number

    def __copy__(self):
        return CrimeReport(self.arrest_date, self.case_number, self.arrest_location,
                           self.arrest_offense, self.arrestee_identification, self.arrestee_birth,
                           self.arrest_city, self.arrest_zipcode, self.arrest_status, self.arresting_officer)

    def return_criminal(self):
        return (self.case_number, self.arrest_date, self.arrestee_identification, self.arrestee_birth, self.arrest_offense)
    def return_officer(self):
        return (self.case_number, self.arrest_date, self.arresting_officer, self.arrest_location, self.arrest_offense)
    def return_scene(self):
        return (self.case_number, self.arrest_date, self.arrest_location, self.arrest_zipcode, self.arrest_city)


class Criminal:
    def __init__(self, criminal_tuple: tuple):
        assert len(criminal_tuple) == 5

        self.case_no = criminal_tuple[0]
        self.date = criminal_tuple[1]
        self.id = criminal_tuple[2]
        self.birth = criminal_tuple[3]
        self.offense = criminal_tuple[4]



class Officer:
    def __init__(self, officer_tuple: tuple):

        assert len(officer_tuple) == 5
        self.case_no = officer_tuple[0]
        self.date = officer_tuple[1]
        self.id = officer_tuple[2]
        self.birth = officer_tuple[3]
        self.offense = officer_tuple[4]

class Scene:
    def __init__(self, scene_tuple: tuple):
        assert len(scene_tuple) == 5
        self.case_no = scene_tuple[0]
        self.date = scene_tuple[1]
        self.id = scene_tuple[2]
        self.location = scene_tuple[3]
        self.offense = scene_tuple[4]

if __name__ == "__main__":
    """c_test = CrimeReport("", "", "", "", "", "", "", "", "", "")
    print(c_test)

    test_ret_criminal = c_test.return_criminal()
    print(test_ret_criminal)
    test_criminal = Criminal(test_ret_criminal)
    print(test_criminal)

    test_officer = Officer(test_ret_criminal)
    assert type(test_officer) == Officer

    test_scene = Scene(test_ret_criminal)

    assert type(test_scene) == Scene
    print(test_officer)


    print(test_scene)
    """
    pass
