import sys
sys.path.append(r'C:\Users\asea2\Desktop\PycharmProjects\Prikolno')
from funcs import bezier_curve_freecad as bezier_freecad

from main import points_for_spinka, points_for_korytse, points_for_radius1, points_for_radius2, points_for_srednaya
import numpy as np

sys.path.append(r'C:\Program Files\FreeCAD 0.18\bin')
sys.path.append(r'C:\Program Files\FreeCAD 0.18\lib')

import FreeCAD as App
# import
import Part
import Sketcher

# Создание нового документа
# exec(open('C:/Program Files/FreeCAD 0.18/data/Mod/Start/StartPage/LoadNew.py').read())
doc = App.newDocument()
App.setActiveDocument("Unnamed")
# App.ActiveDocument = App.getDocument("Unnamed")

# secheniya = range(12)

# Добавление эскиза
Sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
Sketch.Placement = App.Placement(
    App.Vector(0.000000, 0.000000, 0.0),
    App.Rotation(0.000000, 0.000000, 0.000000, 1.000000)
)
Sketch.MapMode = "Deactivated"

# list_test = [1]
# list_test_2 = [2]
# list_test_3 = list_test + list_test_2

point_1 = points_for_spinka
point_2 = points_for_radius2
point_3 = points_for_korytse
point_4 = points_for_radius1
point_5 = [
    (np.array(points_for_srednaya[0])+15).tolist(),
    points_for_srednaya[1]
]
point_6 = [
    (np.array(points_for_srednaya[0])-15).tolist(),
    points_for_srednaya[1]
]
point_7 = [
    points_for_srednaya[0],
    points_for_srednaya[1]
]

# print(point_1)
# print(point_2)

b = 1
n = 0

for point in point_1:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(point[0], point[1], point[2]),
            App.Vector(0, 0, 1),
            10),
        True
    )


# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-70.777008, 19.769506, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-54.830334, -52.099743, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
list_of_points = []
for point in point_1:
    list_of_points.append(
        App.Vector(point[0], point[1])
    )


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        list_of_points,
        None,
        None,
        False,
        3,
        None,
        False),
    False)
# conList = []
# for i in range(len(point_1)):
#     conList.append(
#         Sketcher.Constraint(
#             'InternalAlignment:Sketcher::BSplineControlPoint', n, 3, 3, i
#         )
#     )
#     n += 1
#
#
# n += 1

# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 1, 3, 3, 1))
# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 2, 3, 3, 2))

# App.ActiveDocument.Sketch.addConstraint(conList)

# ДО ЭТОГО МЕСТА

for point in point_2:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(point[0], point[1], point[2]),
            App.Vector(0, 0, 1),
            10),
        True
    )


# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-70.777008, 19.769506, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-54.830334, -52.099743, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
list_of_points = []
for point in point_2:
    list_of_points.append(
        App.Vector(point[0], point[1])
    )


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        list_of_points,
        None,
        None,
        False,
        3,
        None,
        False),
    False)
# conList = []
# for i in range(len(point_2)):
#     conList.append(
#         Sketcher.Constraint(
#             'InternalAlignment:Sketcher::BSplineControlPoint', n, 3, 3, i
#         )
#     )
#     n += 1


# n += 1


# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 1, 3, 3, 1))
# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 2, 3, 3, 2))

# App.ActiveDocument.Sketch.addConstraint(conList)

# blade_points = point_1+point_2+point_3.tolist()+point_4.tolist()
# n_0 = 0
# n_1 = bezier_freecad(point_1, App, Part, Sketcher, n_0)
# n_2 = bezier_freecad(point_2, App, Part, Sketcher, n_1)
# bezier_freecad(point_3, App, Part, Sketcher)
# bezier_freecad(point_4, App, Part, Sketcher)

for point in point_4:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(point[0], point[1], point[2]),
            App.Vector(0, 0, 1),
            10),
        True
    )


# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-70.777008, 19.769506, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-54.830334, -52.099743, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
list_of_points = []
for point in point_4:
    list_of_points.append(
        App.Vector(point[0], point[1])
    )


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        list_of_points,
        None,
        None,
        False,
        3,
        None,
        False),
    False)
# conList = []
# for i in range(len(point_2)):
#     conList.append(
#         Sketcher.Constraint(
#             'InternalAlignment:Sketcher::BSplineControlPoint', n, 3, 3, i
#         )
#     )
#     n += 1


# n += 1


# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 1, 3, 3, 1))
# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 2, 3, 3, 2))

# App.ActiveDocument.Sketch.addConstraint(conList)

# blade_points = point_1+point_2+point_3.tolist()+point_4.tolist()
# n_0 = 0
# n_1 = bezier_freecad(point_1, App, Part, Sketcher, n_0)
# n_2 = bezier_freecad(point_2, App, Part, Sketcher, n_1)
# bezier_freecad(point_3, App, Part, Sketcher)
# bezier_freecad(point_4, App, Part, Sketcher)


App.getDocument('Unnamed').recompute()


for point in point_3:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(point[0], point[1], point[2]),
            App.Vector(0, 0, 1),
            10),
        True
    )


# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-70.777008, 19.769506, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-54.830334, -52.099743, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
list_of_points = []
for point in point_3:
    list_of_points.append(
        App.Vector(point[0], point[1])
    )


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        list_of_points,
        None,
        None,
        False,
        3,
        None,
        False),
    False)
# conList = []
# for i in range(len(point_2)):
#     conList.append(
#         Sketcher.Constraint(
#             'InternalAlignment:Sketcher::BSplineControlPoint', n, 3, 3, i
#         )
#     )
#     n += 1


# n += 1


# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 1, 3, 3, 1))
# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 2, 3, 3, 2))

# App.ActiveDocument.Sketch.addConstraint(conList)

# blade_points = point_1+point_2+point_3.tolist()+point_4.tolist()
# n_0 = 0
# n_1 = bezier_freecad(point_1, App, Part, Sketcher, n_0)
# n_2 = bezier_freecad(point_2, App, Part, Sketcher, n_1)
# bezier_freecad(point_3, App, Part, Sketcher)
# bezier_freecad(point_4, App, Part, Sketcher)


App.getDocument('Unnamed').recompute()

"""
for point in point_5:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(point[0], point[1], point[2]),
            App.Vector(0, 0, 1),
            10),
        True
    )


# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-70.777008, 19.769506, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-54.830334, -52.099743, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
list_of_points = []
for point in point_5:
    list_of_points.append(
        App.Vector(point[0], point[1])
    )


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        list_of_points,
        None,
        None,
        False,
        3,
        None,
        False),
    False)
# conList = []
# for i in range(len(point_2)):
#     conList.append(
#         Sketcher.Constraint(
#             'InternalAlignment:Sketcher::BSplineControlPoint', n, 3, 3, i
#         )
#     )
#     n += 1


# n += 1


# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 1, 3, 3, 1))
# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 2, 3, 3, 2))

# App.ActiveDocument.Sketch.addConstraint(conList)

# blade_points = point_1+point_2+point_3.tolist()+point_4.tolist()
# n_0 = 0
# n_1 = bezier_freecad(point_1, App, Part, Sketcher, n_0)
# n_2 = bezier_freecad(point_2, App, Part, Sketcher, n_1)
# bezier_freecad(point_3, App, Part, Sketcher)
# bezier_freecad(point_4, App, Part, Sketcher)


App.getDocument('Unnamed').recompute()


for point in point_6:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(point[0], point[1], point[2]),
            App.Vector(0, 0, 1),
            10),
        True
    )


# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-70.777008, 19.769506, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
# App.ActiveDocument.Sketch.addGeometry(
#     Part.Circle(
#         App.Vector(-54.830334, -52.099743, 0),
#         App.Vector(0, 0, 1),
#         10),
#     True
# )
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
list_of_points = []
for point in point_6:
    list_of_points.append(
        App.Vector(point[0], point[1])
    )


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        list_of_points,
        None,
        None,
        False,
        3,
        None,
        False),
    False)
# conList = []
# for i in range(len(point_2)):
#     conList.append(
#         Sketcher.Constraint(
#             'InternalAlignment:Sketcher::BSplineControlPoint', n, 3, 3, i
#         )
#     )
#     n += 1


# n += 1


# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 1, 3, 3, 1))
# conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint', 2, 3, 3, 2))

# App.ActiveDocument.Sketch.addConstraint(conList)

# blade_points = point_1+point_2+point_3.tolist()+point_4.tolist()
# n_0 = 0
# n_1 = bezier_freecad(point_1, App, Part, Sketcher, n_0)
# n_2 = bezier_freecad(point_2, App, Part, Sketcher, n_1)
# bezier_freecad(point_3, App, Part, Sketcher)
# bezier_freecad(point_4, App, Part, Sketcher)


App.getDocument('Unnamed').recompute()
"""
# App.getDocument("Unnamed").saveAs(u"C:/Users/asea2/Desktop/PycharmProjects/Prikolno/freecadfiles/111.FCStd")

print(points_for_srednaya)


for p in points_for_srednaya:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(p[0]+15,p[1],0),  # TODO
            App.Vector(0,0,1),
            10),
        True)


lllist = []
for p in points_for_srednaya:
    lllist.append(App.Vector(p[0]+15,p[1]))


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        lllist,
        None,None,False,3,None,False),
    False
)


for p in points_for_srednaya:
    App.ActiveDocument.Sketch.addGeometry(
        Part.Circle(
            App.Vector(p[0]-15,p[1],0),  # TODO
            App.Vector(0,0,1),
            10),
        True)


lllist = []
for p in points_for_srednaya:
    lllist.append(App.Vector(p[0]-15,p[1]))


App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        lllist,
        None,None,False,3,None,False),
    False
)

App.ActiveDocument.Sketch.addGeometry(
    Part.LineSegment(
        App.Vector(points_for_srednaya[0][0]-15, points_for_srednaya[0][1], 0),
        App.Vector(points_for_srednaya[0][0]-15, points_for_srednaya[0][1]+10, 0)
    ),
    False
)

App.ActiveDocument.Sketch.addGeometry(
    Part.LineSegment(
        App.Vector(points_for_srednaya[-1][0]-15, points_for_srednaya[-1][1], 0),
        App.Vector(points_for_srednaya[-1][0]-15, points_for_srednaya[-1][1]-10, 0)
    ),
    False
)

App.ActiveDocument.Sketch.addGeometry(
    Part.LineSegment(
        App.Vector(points_for_srednaya[0][0]-15, points_for_srednaya[0][1]+10, 0),
        App.Vector(points_for_srednaya[0][0]+15, points_for_srednaya[0][1]+10, 0)
    ),
    False
)

App.ActiveDocument.Sketch.addGeometry(
    Part.LineSegment(
        App.Vector(points_for_srednaya[-1][0]+15, points_for_srednaya[-1][1], 0),
        App.Vector(points_for_srednaya[-1][0]+15, points_for_srednaya[-1][1]-10, 0)
    ),
    False
)

App.ActiveDocument.Sketch.addGeometry(
    Part.LineSegment(
        App.Vector(points_for_srednaya[0][0]+15, points_for_srednaya[0][1], 0),
        App.Vector(points_for_srednaya[0][0]+15, points_for_srednaya[0][1]+10, 0)
    ),
    False
)

App.ActiveDocument.Sketch.addGeometry(
    Part.LineSegment(
        App.Vector(points_for_srednaya[-1][0]-15, points_for_srednaya[-1][1]-10, 0),
        App.Vector(points_for_srednaya[-1][0]+15, points_for_srednaya[-1][1]-10, 0)
    ),
    False
)

App.getDocument('Unnamed').recompute()

f = FreeCAD.getDocument('Unnamed').addObject('Part::Extrusion', 'Extrude')
f = App.getDocument('Unnamed').getObject('Extrude')
f.Base = App.getDocument('Unnamed').getObject('Sketch')
f.DirMode = "Custom"
f.Dir = App.Vector(0.000000000000000, 0.000000000000000, 1.000000000000000)
f.DirLink = None
f.LengthFwd = 1.000000000000000  # длина выдавливания
f.LengthRev = 0.000000000000000
f.Solid = True
f.Reversed = False
f.Symmetric = False
f.TaperAngle = 0.000000000000000
f.TaperAngleRev = 0.000000000000000
# Gui.ActiveDocument.Extrude.ShapeColor=Gui.ActiveDocument.Sketch.ShapeColor
# Gui.ActiveDocument.Extrude.LineColor=Gui.ActiveDocument.Sketch.LineColor
# Gui.ActiveDocument.Extrude.PointColor=Gui.ActiveDocument.Sketch.PointColor
# f.Base.ViewObject.hide()
App.ActiveDocument.recompute()

__objs__=[]
__objs__.append(FreeCAD.getDocument("Unnamed").getObject("Extrude"))
import Import
Import.export(__objs__, u"C:/Users/asea2/Desktop/PycharmProjects/Prikolno/freecadfiles/model.step")

del __objs__
