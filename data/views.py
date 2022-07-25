from asyncio.format_helpers import extract_stack
from rest_framework.views import APIView
from rest_framework.response import Response
from .fpl_requests import get_bulk_data, get_fixtures
from .data_extraction import DataExtractor

class Fixtures(APIView):
    def get(self, request, format=None):
        fixtures = get_fixtures()
        return Response(fixtures)

class BulkData(APIView):
    def get(self, request, format=None):
        extractor = DataExtractor()
        extractor.show_teams()
        extractor.show_players()
        return Response(extractor.data)
    
class TeamFixtures(APIView):
    def get(self, request, tid, format=None):
        extractor = DataExtractor()
        fixtures = extractor.show_fixtures_for_team(tid)
        return Response(fixtures)

class Teams(APIView):
    def get(self, request, format=None):
        extractor = DataExtractor()
        return Response(extractor.data["teams"])
