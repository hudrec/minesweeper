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


def revealed_cell(r_x, r_y):
    if r_y in range(0, len(table)) and r_x in range(0, len(table[0])):
        table[r_x][r_y] = 'R'


@api_view(['POST'])
def revealed(request, position_x, position_y):
    position_x = int(position_x)
    position_y = int(position_y)
    if table[position_x][position_y] == 'B':
        return Response({'status': 'GAME OVER'})
    else:
        revealed_cell(position_x + 1, position_y + 1)
        revealed_cell(position_x - 1, position_y - 1)
        revealed_cell(position_x + 1, position_y - 1)
        revealed_cell(position_x - 1, position_y + 1)
        revealed_cell(position_x + 1, position_y)
        revealed_cell(position_x - 1, position_y)
        revealed_cell(position_x, position_y + 1)
        revealed_cell(position_x, position_y - 1)
        revealed_cell(position_x, position_y)

        return Response({'table': table})
