App.ActiveDocument.Sketch.addGeometry(
    Part.Circle(
        App.Vector(14.417536,36.808411,0),
        App.Vector(0,0,1),
        10),
    True
)
App.ActiveDocument.Sketch.addGeometry(
    Part.Circle(
        App.Vector(-70.777008,19.769506,0),
        App.Vector(0,0,1),
        10),
    True
)
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
App.ActiveDocument.Sketch.addGeometry(
    Part.Circle(
        App.Vector(-54.830334,-52.099743,0),
        App.Vector(0,0,1),
        10),
    True
)
# App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
App.ActiveDocument.Sketch.addGeometry(
    Part.BSplineCurve(
        [
            App.Vector(14.4175,36.8084),
            App.Vector(-70.777,19.7695),
            App.Vector(-54.8303,-52.0997)
        ],
        None,
        None,
        False,
        3,
        None,
        False),
    False)
conList = []
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',0,3,3,0))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',1,3,3,1))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,3,3,2))
App.ActiveDocument.Sketch.addConstraint(conList)

# App.ActiveDocument.Sketch.exposeInternalGeometry(3)
