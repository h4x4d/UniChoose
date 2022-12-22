from rest_framework import serializers

from departments.models import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    university_name = serializers.CharField(source='university.name')
    university_rating = serializers.CharField(source='university.avg_rating')
    university_rating_count = serializers.CharField(
        source='university.rating_count')

    class Meta:
        model = Department
        fields = ('id', 'name', 'profile', 'profile_class', 'entry_score',
                  'edu_level', 'ege_subjects', 'university_name',
                  'university_rating', 'university_rating_count')
