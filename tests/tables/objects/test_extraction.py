# coding: utf-8
import json
from io import BytesIO

from img2table.tables.objects.cell import Cell
from img2table.tables.objects.extraction import create_all_rectangles, CellPosition, TableCell, BBox
from img2table.tables.objects.row import Row
from img2table.tables.objects.table import Table


def test_create_all_rectangles():
    c = TableCell(bbox=BBox(x1=0, y1=0, x2=0, y2=0), value="Test")
    cell_positions = [CellPosition(cell=c, row=0, col=0), CellPosition(cell=c, row=1, col=0),
                      CellPosition(cell=c, row=2, col=0), CellPosition(cell=c, row=3, col=0),
                      CellPosition(cell=c, row=0, col=1), CellPosition(cell=c, row=1, col=1),
                      CellPosition(cell=c, row=2, col=1), CellPosition(cell=c, row=3, col=1),
                      CellPosition(cell=c, row=2, col=2), CellPosition(cell=c, row=3, col=2),
                      CellPosition(cell=c, row=2, col=3), CellPosition(cell=c, row=3, col=3),
                      ]

    result = create_all_rectangles(cell_positions=cell_positions)

    assert result == [(0, 0, 1, 3), (2, 2, 3, 3)]
