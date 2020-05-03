
Gui.activateWorkbench("SketcherWorkbench")
App.activeDocument().addObject('Sketcher::SketchObject','Sketch')
App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000,0.000000,0.000000),App.Rotation(0.000000,0.000000,0.000000,1.000000))
App.activeDocument().Sketch.MapMode = "Deactivated"
Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii \n OrthographicCamera {\n viewportMapping ADJUST_CAMERA \n position 0 0 87 \n orientation 0 0 1  0 \n nearDistance -112.88701 \n farDistance 287.28702 \n aspectRatio 1 \n focalDistance 87 \n height 143.52005 }')
Gui.activeDocument().setEdit('Sketch')
import Show.TempoVis
ActiveSketch = App.ActiveDocument.getObject('Sketch')
tv = Show.TempoVis(App.ActiveDocument)
if ActiveSketch.ViewObject.HideDependent:
  objs = tv.get_all_dependent(ActiveSketch)
  objs = filter(lambda x: not x.TypeId.startswith("TechDraw::"), objs)
  objs = filter(lambda x: not x.TypeId.startswith("Drawing::"), objs)
  tv.hide(objs)
if ActiveSketch.ViewObject.ShowSupport:
  tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
if ActiveSketch.ViewObject.ShowLinks:
  tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
tv.hide(ActiveSketch)
ActiveSketch.ViewObject.TempoVis = tv
del(tv)

ActiveSketch = App.ActiveDocument.getObject('Sketch')
if ActiveSketch.ViewObject.RestoreCamera:
  ActiveSketch.ViewObject.TempoVis.saveCamera()

App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(14.417536,36.808411,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(-70.777008,19.769506,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',0,10.000000))
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,1))
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(-54.830334,-52.099743,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
App.ActiveDocument.Sketch.addGeometry(Part.BSplineCurve([App.Vector(14.4175,36.8084),App.Vector(-70.777,19.7695),App.Vector(-54.8303,-52.0997)],None,None,False,3,None,False),False)
conList = []
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',0,3,3,0))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',1,3,3,1))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,3,3,2))
App.ActiveDocument.Sketch.addConstraint(conList)

App.ActiveDocument.Sketch.exposeInternalGeometry(3)