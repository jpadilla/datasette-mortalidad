import pandas as pd


def remove_sensitive_columns():
    data = pd.read_csv("./assets/original-2007-2014.csv", low_memory=False)
    data.drop(
        [
            "dadress",
            "dname",
            "fname",
            "fsurnam",
            "fsurname",
            "informad",
            "informname",
            "mname",
            "msurnam",
            "msurname",
            "sponame",
        ],
        axis=1,
        inplace=True,
    )
    data.to_csv("./assets/2007-2014.csv", index=False)

    data = pd.read_csv("./assets/original-2015-2020.csv", low_memory=False)
    data.drop(
        [
            "AKALastName",
            "AKAMiddleName",
            "AKAName",
            "AKASecondLastName",
            "CertifierAddress1",
            "CertifierAddress2",
            "CertifierName",
            "DeathPlaceAddress1",
            "DeathPlaceAddress2",
            "EmbalmerName",
            "FatherLastName",
            "FatherMiddleName",
            "FatherName",
            "FatherSecondLastName",
            "FuneralFacilityDirectorName",
            "InformantAddress1",
            "InformantAddress2",
            "InformantName",
            "InjuryOccurrenceAddress1",
            "InjuryOccurrenceAddress2",
            "LastName",
            "MiddleName",
            "MotherLastName",
            "MotherMiddleName",
            "MotherName",
            "MotherSecondLastName",
            "Name",
            "ResidencePlaceAddress1",
            "ResidencePlaceAddress2",
            "SecondLastName",
            "SpouseName",
        ],
        axis=1,
        inplace=True,
    )
    data.to_csv("./assets/2015-2020.csv", index=False)


if __name__ == "__main__":
    remove_sensitive_columns()
