import pandas as pd

data = pd.read_csv("./assets/original-2007-2014.csv", low_memory=False)
data.drop(["informad", "dadress"], axis=1, inplace=True)
data.to_csv("./assets/2007-2014.csv", index=False)

data = pd.read_csv("./assets/original-2015-2020.csv", low_memory=False)
data.drop(
    [
        "ResidencePlaceAddress1",
        "ResidencePlaceAddress2",
        "InformantAddress1",
        "InformantAddress2",
        "DeathPlaceAddress1",
        "DeathPlaceAddress2",
        "CertifierAddress1",
        "CertifierAddress2",
        "InjuryOccurrenceAddress1",
        "InjuryOccurrenceAddress2",
    ],
    axis=1,
    inplace=True,
)
data.to_csv("./assets/2015-2020.csv", index=False)
