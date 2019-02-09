from sqlalchemy import Integer, String, Enum
age_levels = ['0-2', '3-17', '18-34', '35-50', '51-69', '70+']
age_bins = Enum(*age_levels)
sex_levels = ["M","F"]
sex_bins = Enum(*sex_levels)
est_residential_density_levels = range(1, 3)
quartile_levels = range(1, 5)
quintile_levels = range(1, 6)
sextile_levels = range(1, 7)
boolean_levels = [0, 1]


envfeature_names = [
    stat + "Daily" + feature + "Exposure" + suffix + binning for binning in ["", "_qcut"] for feature in ["PM2.5", "Ozone"] for stat in ["Avg", "Max"] for suffix in ["", "_StudyAvg", "_StudyMax"]
]

features = {
    "patient": [
        ("AgeStudyStart", age_bins, age_levels),
        ("Sex", sex_bins, sex_levels),
        ("Race", String, None),
        ("Ethnicity", String, None),
        ("AsthmaDx", Integer, boolean_levels),
        ("CroupDx", Integer, boolean_levels),
        ("ReactiveAirwayDx", Integer, boolean_levels),
        ("CoughDx", Integer, boolean_levels),
        ("PneumoniaDx", Integer, boolean_levels),
        ("ObesityICD", Integer, boolean_levels),
        ("ObesityBMI", Integer, boolean_levels) ] + 
    [
        (feature_name, Integer, quintile_levels) for feature_name in envfeature_names ] + 
    [
        ("EstResidentialDensity", Integer, est_residential_density_levels),
        ("EstResidentialDesnity25Plus", Integer, quintile_levels),
        ("EstProbabilityNonHispWhite", Integer, quartile_levels),
        ("EstProbabilityHouseholdNonHispWhite", Integer, quartile_levels),
        ("EstProbabilityHighSchoolMaxEducation", Integer, quartile_levels),
        ("EstProbabilityNoAuto", Integer, quartile_levels),
        ("EstProbabilityNoHealthIns", Integer, quartile_levels),
        ("EstProbabilityESL", Integer, quartile_levels),
        ("EstHouseholdIncome", Integer, quintile_levels),
        ("MajorRoadwayHighwayExposure", Integer, sextile_levels),
        ("TotalEDInpatientVisits", Integer, None),
        ("Prednisone", Integer, boolean_levels),
        ("Fluticasone", Integer, boolean_levels),
        ("Mometasone", Integer, boolean_levels),
        ("Budesonide", Integer, boolean_levels),
        ("Beclomethasone", Integer, boolean_levels),
        ("Ciclesonide", Integer, boolean_levels),
        ("Flunisolide", Integer, boolean_levels),
        ("Albuterol", Integer, boolean_levels),
        ("Metaproterenol", Integer, boolean_levels),
        ("Diphenhydramine", Integer, boolean_levels),
        ("Fexofenadine", Integer, boolean_levels),
        ("Cetirizine", Integer, boolean_levels),
        ("Ipratropium", Integer, boolean_levels),
        ("Salmeterol", Integer, boolean_levels),
        ("Arformoterol", Integer, boolean_levels),
        ("Formoterol", Integer, boolean_levels),
        ("Indacaterol", Integer, boolean_levels),
        ("Theophylline", Integer, boolean_levels),
        ("Omalizumab", Integer, boolean_levels),
        ("Mepolizumab", Integer, boolean_levels),
    ],
    "visit": [
        ("VisitType", String, None),
        ("AgeVisit", age_bins, age_levels),
        ("Sex", sex_bins, sex_levels),
        ("Race", String, None),
        ("Ethnicity", String, None),
        ("AsthmaDxVisit", Integer, boolean_levels),
        ("CroupDxVisit", Integer, boolean_levels),
        ("ReactiveAirwayDxVisit", Integer, boolean_levels),
        ("CoughDxVisit", Integer, boolean_levels),
        ("PneumoniaDxVisit", Integer, boolean_levels),
        ("ObesityDxVisit", Integer, boolean_levels),
        ("ObesityBMIVisit", Integer, boolean_levels),
        ("Avg24hPM2.5Exposure", Integer, quintile_levels),
        ("Max24hPM2.5Exposure", Integer, quintile_levels),
        ("Avg24hOzoneExposure", Integer, quintile_levels),
        ("Max24hOzoneExposure", Integer, quintile_levels),
        ("Avg24hPM2.5Exposure_qcut", Integer, quintile_levels),
        ("Max24hPM2.5Exposure_qcut", Integer, quintile_levels),
        ("Avg24hOzoneExposure_qcut", Integer, quintile_levels),
        ("Max24hOzoneExposure_qcut", Integer, quintile_levels),
        ("EstResidentialDensity", Integer, quintile_levels),
        ("EstResidentialDesnity25Plus", Integer, quintile_levels),
        ("EstProbabilityNonHispWhite", Integer, quartile_levels),
        ("EstProbabilityHouseholdNonHispWhite", Integer, quartile_levels),
        ("EstProbabilityHighSchoolMaxEducation", Integer, quartile_levels),
        ("EstProbabilityNoAuto", Integer, quartile_levels),
        ("EstProbabilityNoHealthIns", Integer, quartile_levels),
        ("EstProbabilityESL", Integer, quartile_levels),
        ("EstHouseholdIncome", Integer, quintile_levels),
        ("MajorRoadwayHighwayExposure", Integer, sextile_levels),
        ("PrednisoneVisit", Integer, boolean_levels),
        ("FluticasoneVisit", Integer, boolean_levels),
        ("MometasoneVisit", Integer, boolean_levels),
        ("BudesonideVisit", Integer, boolean_levels),
        ("BeclomethasoneVisit", Integer, boolean_levels),
        ("CiclesonideVisit", Integer, boolean_levels),
        ("FlunisolideVisit", Integer, boolean_levels),
        ("AlbuterolVisit", Integer, boolean_levels),
        ("MetaproterenolVisit", Integer, boolean_levels),
        ("DiphenhydramineVisit", Integer, boolean_levels),
        ("FexofenadineVisit", Integer, boolean_levels),
        ("CetirizineVisit", Integer, boolean_levels),
        ("IpratropiumVisit", Integer, boolean_levels),
        ("SalmeterolVisit", Integer, boolean_levels),
        ("ArformoterolVisit", Integer, boolean_levels),
        ("FormoterolVisit", Integer, boolean_levels),
        ("IndacaterolVisit", Integer, boolean_levels),
        ("TheophyllineVisit", Integer, boolean_levels),
        ("OmalizumabVisit", Integer, boolean_levels),
        ("MepolizumabVisit", Integer, boolean_levels),
    ]
}
