from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
table = [
            ['F','F','F','F','F','F',],
            ['F','F','F','F','F','F',],
            ['F','F','F','F','F','F',],
            ['F','F','F','F','F','F',],
            ['F','F','F','F','F','F',],
            ['F','F','F','F','F','F',],
        ]


def revealed_cell(position_x, position_y):
    if not table[position_x][position_y] == 'B':
        table[position_x][position_y] == 'R'


@api_view(['POST'])
def revealed(request, position_x, position_y):
    if  table[position_x][position_y] == 'B':
        return Response({'status': 'GAME OVER'})
    else:
        revealed_cell([position_x + 1][position_y + 1])
        revealed_cell(table[position_x - 1][position_y - 1])
        revealed_cell(table[position_x + 1][position_y - 1])
        revealed_cell(table[position_x - 1][position_y - 1])
        revealed_cell(table[position_x + 1][position_y])
        revealed_cell(table[position_x - 1][position_y])
        revealed_cell(table[position_x][position_y + 1])
        revealed_cell(table[position_x][position_y - 1])

        return Response({'table', table})
