# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.3.0 with dump python functionality
###

import os
import sys #
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
pwd = os.getcwd()
print("Current path is {}".format(pwd))
notebook = salome_notebook.NoteBook(theStudy) #
sys.path.insert(0, pwd)
meshname = 'study_griffin2011HF_mesh'

### geometry parameters###
w_air = 0.1
h_air = 0.05
r_el = 0.04
h_el = 0.01
gap = 0.002
r_dish = 0.0175
h_dish = 0.01
t_dish = 0.001
####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("w_air", w_air)
notebook.set("h_air", h_air)
notebook.set("r_el", r_el)
notebook.set("h_el", h_el)
notebook.set("gap", gap)
notebook.set("r_dish", r_dish)
notebook.set("h_dish", h_dish)
notebook.set("t_dish", t_dish)
notebook.set("r_medium", "r_dish-t_dish")
notebook.set("h_medium", "h_dish-gap-t_dish")
notebook.set("x_center", "w_air/2.")
notebook.set("z_electrode2", "h_dish+h_el")
notebook.set("z_medium", "h_el+t_dish")
notebook.set("z_air", "h_el+h_dish-gap")
####################################################
##        End of NoteBook variables section       ##
####################################################
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ("w_air", "w_air", "h_air")
[geomObj_1,geomObj_2,geomObj_3,geomObj_4,geomObj_5,geomObj_6] = geompy.SubShapeAll(Box_1, geompy.ShapeType["FACE"])
geomObj_7 = geompy.MakeCylinderRH(0.04, 0.01)
geomObj_8 = geompy.MakeCylinderRH(0.0175, 0.01)
geomObj_9 = geompy.MakeCylinderRH(0.0165, 0.007)
centerBoxBase = geompy.MakeVertex("x_center", "x_center", 0)
Cylinder_4 = geompy.MakeCylinder(centerBoxBase, OZ, "r_el", "h_el")
[geomObj_10,geomObj_11,geomObj_12] = geompy.SubShapeAll(Cylinder_4, geompy.ShapeType["FACE"])
Cylinder_5 = geompy.MakeCylinder(centerBoxBase, OZ, "r_dish", "h_dish")
Cylinder_6 = geompy.MakeCylinder(centerBoxBase, OZ, "r_medium", "h_medium")
[geomObj_13,geomObj_14,geomObj_15] = geompy.SubShapeAll(Cylinder_6, geompy.ShapeType["FACE"])
Translation_1 = geompy.MakeTranslation(Cylinder_4, 0, 0, "z_electrode2")
[geomObj_16,geomObj_17,geomObj_18] = geompy.SubShapeAll(Translation_1, geompy.ShapeType["FACE"])
[geomObj_19,geomObj_20,geomObj_21] = geompy.SubShapeAll(Translation_1, geompy.ShapeType["FACE"])
Translation_2 = geompy.MakeTranslation(Cylinder_5, 0, 0, "h_el")
Translation_3 = geompy.MakeTranslation(Cylinder_6, 0, 0, "z_medium")
Cylinder_1 = geompy.MakeCylinder(centerBoxBase, OZ, "r_medium", "gap")
geompy.TranslateDXDYDZ(Cylinder_1, 0, 0, "z_air")
Cut_1 = geompy.MakeCutList(Box_1, [Cylinder_4, Translation_1], True)
Partition_1 = geompy.MakePartition([Translation_2, Translation_3, Cylinder_1, Cut_1], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["SOLID"])
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_10)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_16)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_17)
LowerElectrode = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(LowerElectrode, [75, 80, 11])
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_1)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_2)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_3)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_4)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_6)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_19)
listSameIDs = geompy.GetSameIDs(Partition_1, geomObj_20)
UpperElectrode = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(UpperElectrode, [88, 93, 13, 32, 83])
dish = geompy.CreateGroup(Partition_1, geompy.ShapeType["SOLID"])
geompy.UnionIDs(dish, [2])
medium = geompy.CreateGroup(Partition_1, geompy.ShapeType["SOLID"])
geompy.UnionIDs(medium, [36])
airgap = geompy.CreateGroup(Partition_1, geompy.ShapeType["SOLID"])
geompy.UnionIDs(airgap, [30, 38])
geompy.DifferenceIDs(airgap, [30, 38])
geompy.UnionIDs(airgap, [38])
geompy.DifferenceIDs(airgap, [38])
geompy.UnionIDs(airgap, [30])
air = geompy.CreateGroup(Partition_1, geompy.ShapeType["SOLID"])
geompy.UnionIDs(air, [38])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( centerBoxBase, 'centerBoxBase' )
geompy.addToStudy( Cylinder_4, 'Cylinder_4' )
geompy.addToStudy( Cylinder_5, 'Cylinder_5' )
geompy.addToStudy( Cylinder_6, 'Cylinder_6' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Translation_2, 'Translation_2' )
geompy.addToStudy( Translation_3, 'Translation_3' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, LowerElectrode, 'LowerElectrode' )
geompy.addToStudyInFather( Partition_1, UpperElectrode, 'UpperElectrode' )
geompy.addToStudyInFather( Partition_1, dish, 'dish' )
geompy.addToStudyInFather( Partition_1, medium, 'medium' )
geompy.addToStudyInFather( Partition_1, airgap, 'airgap' )
geompy.addToStudyInFather( Partition_1, air, 'air' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Partition_1)
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
LowerElectrode_1 = Mesh_1.GroupOnGeom(LowerElectrode,'LowerElectrode',SMESH.FACE)
UpperElectrode_1 = Mesh_1.GroupOnGeom(UpperElectrode,'UpperElectrode',SMESH.FACE)
dish_1 = Mesh_1.GroupOnGeom(dish,'dish',SMESH.VOLUME)
medium_1 = Mesh_1.GroupOnGeom(medium,'medium',SMESH.VOLUME)
LowerElectrode_2 = Mesh_1.GroupOnGeom(LowerElectrode,'LowerElectrode',SMESH.NODE)
UpperElectrode_2 = Mesh_1.GroupOnGeom(UpperElectrode,'UpperElectrode',SMESH.NODE)
dish_2 = Mesh_1.GroupOnGeom(dish,'dish',SMESH.NODE)
medium_2 = Mesh_1.GroupOnGeom(medium,'medium',SMESH.NODE)
smesh.SetName(Mesh_1, 'Mesh_1')
airgap_1 = Mesh_1.GroupOnGeom(airgap,'airgap',SMESH.VOLUME)
airgap_2 = Mesh_1.GroupOnGeom(airgap,'airgap',SMESH.NODE)
air_1 = Mesh_1.GroupOnGeom(air,'air',SMESH.VOLUME)
air_2 = Mesh_1.GroupOnGeom(air,'air',SMESH.NODE)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(medium, 0.001)
[ LowerElectrode_1, UpperElectrode_1, dish_1, medium_1, LowerElectrode_2, UpperElectrode_2, dish_2, medium_2, airgap_1, airgap_2, air_1, air_2 ] = Mesh_1.GetGroups()
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(airgap, 0.0005)
[ LowerElectrode_2, UpperElectrode_2, dish_2, medium_2, airgap_2, air_2, LowerElectrode_1, UpperElectrode_1, airgap_1, air_1, dish_1, medium_1 ] = Mesh_1.GetGroups()
smesh.SetName(Mesh_1, 'Mesh_1')
NETGEN_3D_Parameters_1.SetMaxSize( 0.005 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 4 )
NETGEN_3D_Parameters_1.SetMinSize( 0 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(medium, 0.001)
isDone = Mesh_1.Compute()
[ LowerElectrode_2, UpperElectrode_2, dish_2, medium_2, airgap_2, air_2, LowerElectrode_1, UpperElectrode_1, airgap_1, air_1, dish_1, medium_1 ] = Mesh_1.GetGroups()
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED(pwd + '/' + str(meshname) + '.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(dish_2, 'dish')
smesh.SetName(UpperElectrode_2, 'UpperElectrode')
smesh.SetName(LowerElectrode_2, 'LowerElectrode')
smesh.SetName(air_2, 'air')
smesh.SetName(airgap_2, 'airgap')
smesh.SetName(medium_2, 'medium')
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(airgap_1, 'airgap')
smesh.SetName(air_1, 'air')
smesh.SetName(medium_1, 'medium')
smesh.SetName(LowerElectrode_1, 'LowerElectrode')
smesh.SetName(dish_1, 'dish')
smesh.SetName(UpperElectrode_1, 'UpperElectrode')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)