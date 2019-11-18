from faker import Faker

fake = Faker()

fake.random.seed(5467)

medical_equipments_list = [
    "Feeding Pump", "Fetal Doppler",
    "Fetal Monitor", "Infant Incubator",
    "Infant Warmer", "Infusion Pump",
    "IV Pole",
    "incubator",
    "Lab Microscope",
    "Lab Refrigerator",
    "Laryngoscope",
    "Nebulizer"
]
non_medical_equipments_list = ["Bed", "Chair", "Table", "Table lamp", "Sofa", "Wardrobe"]
diagnosis_list = [
    "Hypertension", "Pain in joint",
    "Hyperlipidemia", "Acute laryngopharyngitis",
    "Diabetes", "Acute maxillary sinusitis",
    "Back pain", "Major depressive disorder",
    "Anxiety", "Acute bronchitis",
    "Obesity", "Asthma",
    "Allergic rhinitis", "Depressive disorder",
    "Reflux esophagitis", "Nail fungus",
    "Respiratory problems", "Coronary atherosclerosis",
    "Hypothyroidism", "Urinary tract infection",
    "Visual refractive errors",
    "General medical exam",
    "Osteoarthritis",
    "Fibromyalgia / myositis",
    "Malaise and fatigue",
]
prescription_list = [
    'home sense'
    , 'Power Aqua Balancing Toner'
    , 'Cotton Seed'
    , 'Antibacterial Foam'
    , 'Aplicare Povidone-iodine Triples'
    , 'Multi Sympton Cold Day Night'
    , 'Gazyva'
    , 'OVACE'
    , 'risperidone'
    , 'Gambil Oak'
    , 'Metformin Hydrochloride'
    , 'Quetiapine Fumarate'
    , 'Doxycycline Monohydrate'
    , 'Cardizem CD'
    , 'Clindamycin'
    , 'Lithium Carbonate'
    , 'CALCAREA FLUORICA'
    , 'Cold Sore Complex'
    , 'LBEL NATURAL FINISH MOISTURIZING FOUNDATION SPF 25'
    , 'Clonidine Hydrochloride'
]
non_medical_position_list = [
    "IT department",
    "Security",
    "Sanitation",
    "Adminstration",
]
medical_position_list = [
    "Allergy",
    "Colorectal Surgery",
    "General Surgery",
    "Neurosurgery",
    "Anesthesia",
    "Dermatology",
    "Geriatrics",
    "Internal Medicine",
    "Nuclear Medicine",
    "Bariatric Medicine/Surgery",
    "Electrophysiology",
    "Gynecologic Oncology",
    "Interventional Radiology",
    "Obstetrics & Gynecology",
    "Burn/Trauma",
    "Emergency Medicine",
    "Hematology/Oncology",
    "Medical Genetics",
    "Occupational Medicine",
    "Cardiac Catheterization",
    "Endocrinology",
    "Hepatobiliary",
    "Neonatology",
    "Ophthalmology",
    "Cardiology",
    "Family Practice",
    "Hospitalist",
    "Nephrology",
    "Oral Surgery",
    "Cardiovascular Surgery",
    "Gastroenterology",
    "Infectious Disease",
    "Neuroradiology",
    "Nurse", "Nurse", "Nurse", "Nurse",
    "Nurse", "Nurse", "Nurse", "Nurse",
    "Nurse", "Nurse", "Nurse", "Nurse",
    "Nurse", "Nurse", "Nurse", "Nurse",
    "Nurse", "Nurse", "Nurse", "Nurse",
    "Nurse", "Nurse", "Nurse", "Nurse",
]


def chance(x):
    return (fake.random_int(min=1, max=100) <= x)



def full_name():
    return fake.name()

def non_medical_equipment():
    return fake.word(ext_word_list=non_medical_equipments_list)


def medical_equipment():
    return fake.word(ext_word_list=medical_equipments_list)


def passport_number():
    return fake.ean(13)


def login():
    return fake.user_name()


def password():
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)


def last_time_online():
    return fake.date_time_between(start_date="-7d", end_date="now", tzinfo=None)


def account_created():
    return fake.date_time_between(start_date="-10y", end_date="now", tzinfo=None)
