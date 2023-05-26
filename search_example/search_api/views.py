from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Candidate
from .paginators import CustomPagination
from .serializers import CandidateSerializer, SearchResultSerializer


class CandidateView(APIView):
    pagination_class = CustomPagination
    queryset = Candidate.objects.all().order_by("-score")

    @property
    def paginator(self):
        """The paginator instance associated with the view, or `None`."""
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """Return a single page of results, or `None` if pagination is disabled."""
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    @swagger_auto_schema(
        operation_summary="search candidate by skill",
        responses={200: SearchResultSerializer, 422: "field missing"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["skill_name"],
            properties={
                "skill_name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="skill name, for example backend",
                ),
                "page": openapi.Schema(type=openapi.TYPE_INTEGER, default=1),
                "page_size": openapi.Schema(
                    type=openapi.TYPE_INTEGER, default=20, min=1, max=20
                ),
            },
        ),
    )
    def post(self, request):
        skill = request.data.get("skill_name")
        if not skill:
            return Response(status=422)
        queryset = self.queryset.filter(skill=request.data["skill_name"])
        page = self.paginate_queryset(queryset)
        serializer = CandidateSerializer(page, many=True)
        return Response(
            {
                "candidates": serializer.data,
                "count": self.paginator.page.paginator.count,  # total
            }
        )
