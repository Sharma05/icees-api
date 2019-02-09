create type age_bins as enum ('0-2', '3-17', '18-34', '35-50', '51-69', '70+');

create table patient(
    "PatientId" varchar,
    "AgeStudyStart" age_bins,
    "Sex" varchar,
    "Race" varchar,
    "Ethnicity" varchar,
    "AsthmaDx" integer,
    "CroupDx" integer,
    "ReactiveAirwayDx" integer,
    "CoughDx" integer,
    "PneumoniaDx" integer,
    "ObesityICD" integer,
    "ObesityBMI" integer,
    "AvgDailyPM2.5Exposure" integer,
    "MaxDailyPM2.5Exposure" integer,
    "AvgDailyOzoneExposure" integer,
    "MaxDailyOzoneExposure" integer,
    "EstResidentialDensity" integer,
    "EstResidentialDesnity25Plus" integer,
    "EstProbabilityNonHispWhite" integer,
    "EstProbabilityHouseholdNonHispWhite" integer,
    "EstProbabilityHighSchoolMaxEducation" integer,
    "EstProbabilityNoAuto" integer,
    "EstProbabilityNoHealthIns" integer,
    "EstProbabilityESL" integer,
    "EstHouseholdIncome" integer,
    "MajorRoadwayHighwayExposure" integer,
    "TotalEDInpatientVisits" integer,
    "Prednisone" integer,
    "Fluticasone" integer,
    "Mometasone" integer,
    "Budesonide" integer,
    "Beclomethasone" integer,
    "Ciclesonide" integer,
    "Flunisolide" integer,
    "Albuterol" integer,
    "Metaproterenol" integer,
    "Diphenhydramine" integer,
    "Fexofenadine" integer,
    "Cetirizine" integer,
    "Ipratropium" integer,
    "Salmeterol" integer,
    "Arformoterol" integer,
    "Formoterol" integer,
    "Indacaterol" integer,
    "Theophylline" integer,
    "Omalizumab" integer,
    "Mepolizumab" integer,
    "AvgDailyPM2.5Exposure_qcut" integer,
    "AvgDailyPM2.5Exposure_StudyAvg_qcut" integer,
    "AvgDailyPM2.5Exposure_StudyMax_qcut" integer,
    "MaxDailyPM2.5Exposure_qcut" integer,
    "MaxDailyPM2.5Exposure_StudyAvg_qcut" integer,
    "MaxDailyPM2.5Exposure_StudyMax_qcut" integer,
    "AvgDailyOzoneExposure_qcut" integer,
    "AvgDailyOzoneExposure_StudyAvg_qcut" integer,
    "AvgDailyOzoneExposure_StudyMax_qcut" integer,
    "MaxDailyOzoneExposure_qcut" integer,
    "MaxDailyOzoneExposure_StudyAvg_qcut" integer,
    "MaxDailyOzoneExposure_StudyMax_qcut" integer,
    "AvgDailyPM2.5Exposure_StudyAvg" integer,
    "AvgDailyPM2.5Exposure_StudyMax" integer,
    "MaxDailyPM2.5Exposure_StudyAvg" integer,
    "MaxDailyPM2.5Exposure_StudyMax" integer,
    "AvgDailyOzoneExposure_StudyAvg" integer,
    "AvgDailyOzoneExposure_StudyMax" integer,
    "MaxDailyOzoneExposure_StudyAvg" integer,
    "MaxDailyOzoneExposure_StudyMax" integer,
    "year" integer
);

create table visit(
    "Patient_ID" varchar,
    "VisitId" varchar,
    "VisitType" varchar,
    "AgeVisit" age_bins,
    "Sex" varchar,
    "Race" varchar,
    "Ethnicity" varchar,
    "AsthmaDxVisit" integer,
    "CroupDxVisit" integer,
    "ReactiveAirwayDxVisit" integer,
    "CoughDxVisit" integer,
    "PneumoniaDxVisit" integer,
    "ObesityDxVisit" integer,
    "ObesityBMIVisit" integer,
    "Avg24hPM2.5Exposure" integer,
    "Max24hPM2.5Exposure" integer,
    "Avg24hOzoneExposure" integer,
    "Max24hOzoneExposure" integer,
    "EstResidentialDensity" integer,
    "EstResidentialDesnity25Plus" integer,
    "EstProbabilityNonHispWhite" integer,
    "EstProbabilityHouseholdNonHispWhite" integer,
    "EstProbabilityHighSchoolMaxEducation" integer,
    "EstProbabilityNoAuto" integer,
    "EstProbabilityNoHealthIns" integer,
    "EstProbabilityESL" integer,
    "EstHouseholdIncome" integer,
    "MajorRoadwayHighwayExposure" integer,
    "PrednisoneVisit" integer,
    "FluticasoneVisit" integer,
    "MometasoneVisit" integer,
    "BudesonideVisit" integer,
    "BeclomethasoneVisit" integer,
    "CiclesonideVisit" integer,
    "FlunisolideVisit" integer,
    "AlbuterolVisit" integer,
    "MetaproterenolVisit" integer,
    "DiphenhydramineVisit" integer,
    "FexofenadineVisit" integer,
    "CetirizineVisit" integer,
    "IpratropiumVisit" integer,
    "SalmeterolVisit" integer,
    "ArformoterolVisit" integer,
    "FormoterolVisit" integer,
    "IndacaterolVisit" integer,
    "TheophyllineVisit" integer,
    "OmalizumabVisit" integer,
    "MepolizumabVisit" integer,
    "Avg24hPM2.5Exposure_qcut" integer,
    "Max24hPM2.5Exposure_qcut" integer,
    "Avg24hOzoneExposure_qcut" integer,
    "Max24hOzoneExposure_qcut" integer,
    "year" integer
);

create table cohort (cohort_id varchar primary key, size integer, features varchar, "table" varchar, year integer);

create sequence cohort_id;

create table name(
    name varchar primary key,
    "table" varchar,
    cohort_id varchar references cohort(cohort_id)
);
