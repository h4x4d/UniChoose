from django.db.models import Q


def departments_checker(queryset, user_subjects, user_marks, user_id,
                        department):
    mark = 0
    for subject in department.ege_subjects:
        if type(subject) == list:
            current_mark = 0
            for user_subject in user_subjects:
                if user_subject in subject:
                    current_mark = max(
                        user_marks[user_subjects.index(user_subject)],
                        current_mark)

            if not current_mark:
                return False
            mark += current_mark
        else:
            if subject not in user_subjects:
                return False
            else:
                mark += user_marks[user_subjects.index(subject)]

    if mark >= department.entry_score:
        try:
            queryset.get(
                Q(relations__department__id=department.id)
                & Q(relations__account__id=user_id))
            return False
        except Exception:
            return True

    return False
