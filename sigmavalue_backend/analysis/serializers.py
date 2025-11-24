from rest_framework import serializers

class AnalyzeRequestSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=500)

class ChartDataPointSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=False)
    area = serializers.CharField(required=False)
    price = serializers.FloatField(required=False)
    demand = serializers.FloatField(required=False)

class TableRowSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=False)
    area = serializers.CharField(required=False)
    price = serializers.FloatField(required=False)
    demand = serializers.FloatField(required=False)
    size = serializers.FloatField(required=False, allow_null=True)

class AnalyzeResponseSerializer(serializers.Serializer):
    summary = serializers.CharField()
    chartData = ChartDataPointSerializer(many=True)
    tableData = TableRowSerializer(many=True)
