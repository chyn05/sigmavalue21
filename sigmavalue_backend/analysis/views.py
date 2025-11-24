from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import AnalyzeRequestSerializer, AnalyzeResponseSerializer
from .services.query_parser import extract_areas, detect_metric, detect_year_range
from .services.analytics import compute_trends, build_mock_summary
from .services.excel_loader import DatasetNotFoundError

@api_view(["POST"])
def analyze_view(request):
    serializer = AnalyzeRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    query = serializer.validated_data["query"]

    try:
        areas = extract_areas(query)
        metric = detect_metric(query)
        year_range = detect_year_range(query)

        chart_data, table_data = compute_trends(areas, metric, year_range)
        summary = build_mock_summary(query, areas, metric, chart_data)

        response_payload = {
            "summary": summary,
            "chartData": chart_data,
            "tableData": table_data,
        }

        response_serializer = AnalyzeResponseSerializer(response_payload)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    except DatasetNotFoundError as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({"error": "Internal server error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
