from django.db.models import Avg
from rest_framework import serializers

from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(source="name")
    main_skill_score = serializers.FloatField(source="score")
    related_skills = serializers.SerializerMethodField()

    def get_related_skills(self, obj: Candidate):
        candidates = Candidate.objects.filter(name=obj.name).exclude(skill=obj.skill)
        average_scores = Candidate.objects.values("skill").annotate(
            avg_score=Avg("score")
        )
        average_scores_dict = {
            average_score["skill"].lower(): round(average_score["avg_score"])
            for average_score in average_scores
        }
        related_skills = [
            {
                "name": candidate.skill,
                "average": average_scores_dict[candidate.skill],
                "score": candidate.score,
            }
            for candidate in candidates
        ]
        return related_skills

    class Meta:
        model = Candidate
        fields = ["candidate_name", "main_skill_score", "related_skills"]


class SearchResultSerializer(serializers.Serializer):
    candidates = CandidateSerializer(many=True)
    count = serializers.IntegerField()
