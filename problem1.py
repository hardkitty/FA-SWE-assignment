import vtk
import sys
import argparse
sys.path.append('D:\\vtk tests')

class class1():
    def __init__(self):
        super(class1,self).__init__()

        self.function1()
    def function1(self):
        reader1=vtk.vtkSTLReader()

        #Reading STL file
        reader1.SetFileName('assignment.stl')
    
        mapper=vtk.vtkDataSetMapper()
        mapper.SetInputConnection(reader1.GetOutputPort())
        actor=vtk.vtkActor()
        actor.SetMapper(mapper)
        self.window=vtk.vtkRenderWindow()
        self.inter=vtk.vtkRenderWindowInteractor()
        self.renderer=vtk.vtkRenderer()

        colors=vtk.vtkNamedColors()
       
        #Declaring cutter,mapper,actor and plane for z-height=10.0
        #1st
                
        cutter1=vtk.vtkCutter()
        mapper1=vtk.vtkPolyDataMapper()
        actor1=vtk.vtkActor()
        plane1=vtk.vtkPlane()
        plane1.SetOrigin(0.0,10.0,0.0)
        plane1.SetNormal(0.0,1.0,0.0)

        #Inputting implicit plane function as z-height mentioned for sectioning
        cutter1.SetCutFunction(plane1)
        cutter1.SetInputConnection(reader1.GetOutputPort())
        mapper1.SetInputConnection(cutter1.GetOutputPort())

        actor1.SetMapper(mapper1)
        actor1.GetProperty().SetColor(colors.GetColor3d('Yellow'))
        actor1.GetProperty().SetAmbient(1.0)
        actor1.GetProperty().SetLineWidth(2)

        self.renderer.AddActor(actor1)

        #2nd
                
        cutter2=vtk.vtkCutter()
        mapper2=vtk.vtkPolyDataMapper()
        actor2=vtk.vtkActor()
        plane2=vtk.vtkPlane()
        plane2.SetOrigin(0.0,30.0,0.0)
        plane2.SetNormal(0.0,1.0,0.0)

        #Inputting implicit plane function as z-height mentioned for sectioning
        cutter2.SetCutFunction(plane2)
        cutter2.SetInputConnection(reader1.GetOutputPort())
        mapper2.SetInputConnection(cutter2.GetOutputPort())

        actor2.SetMapper(mapper2)
        actor2.GetProperty().SetColor(colors.GetColor3d('Red'))
        actor2.GetProperty().SetAmbient(1.0)
        actor2.GetProperty().SetLineWidth(2)

        self.renderer.AddActor(actor2)

        #3rd
                
        cutter3=vtk.vtkCutter()
        mapper3=vtk.vtkPolyDataMapper()
        actor3=vtk.vtkActor()
        plane3=vtk.vtkPlane()
        plane3.SetOrigin(0.0,50.0,0.0)
        plane3.SetNormal(0.0,1.0,0.0)

        #Inputting implicit plane function as z-height mentioned for sectioning
        cutter3.SetCutFunction(plane3)
        cutter3.SetInputConnection(reader1.GetOutputPort())
        mapper3.SetInputConnection(cutter3.GetOutputPort())

        actor3.SetMapper(mapper3)
        actor3.GetProperty().SetColor(colors.GetColor3d('Yellow'))
        actor3.GetProperty().SetAmbient(1.0)
        actor3.GetProperty().SetLineWidth(2)

        self.renderer.AddActor(actor3)
        self.window.AddRenderer(self.renderer)
        self.window.SetSize(1000,1000)
        self.window.SetWindowName('Problem 1')

        
        self.inter.SetRenderWindow(self.window)

        self.inter.Initialize()
        self.window.Render()
       
        self.inter.Start()


c=class1()

