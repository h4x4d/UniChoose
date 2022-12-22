subjects_attr_names = [
    'mark_informatics',
    'mark_math',
    'mark_russian',
    'mark_social',
    'mark_foreign',
    'mark_biology',
    'mark_geography',
    'mark_chemistry',
    'mark_physics',
    'mark_literature',
    'mark_history',
    'mark_additional',
]
subjects_attr_placeholders = [
    'ИКТ',
    'Математика',
    'Русский язык',
    'Обществознание',
    'Иностранный язык',
    'Биология',
    'География',
    'Химия',
    'Физика',
    'Литература',
    'История',
    'Доп. баллы',
]
subjects_convert = {
    subjects_attr_placeholders[i]: subjects_attr_names[i]
    for i in range(len(subjects_attr_names))
}
reversed_subjects_convert = {subjects_convert[i]: i for i in subjects_convert}
