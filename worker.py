from init import *

def CreateBeam():
    try:
        print('clicked')
        print(1234123+12341234)
        myModel = Model()
        p1=T3D.Point(0,0,0)
        p2=T3D.Point(6000.0,6000.0,1000.0)
        print(p1)
        print(p2)
        myBeam =  Beam(p1,p2)

        myBeam.Material.MaterialString = "C245"
        myBeam.Profile.ProfileString = "I30B1_20_93"
        myBeam.Name = "Привет Форуму"

        myBeam.Insert()
        myModel.CommitChanges()

    except Exception as ex:
        print(ex)

    
def ReadBeams():
    try:
        # myModel = Model()
        GetSelectedObjects = TUI.ModelObjectSelector()
        SelectedObjects = GetSelectedObjects.GetSelectedObjects()

        print("вывод типов")
        for Object in SelectedObjects:
            print(type(Object))

        print("вывод только балочных типов + их длины")
        SelectedObjects.Reset()
        for Object in SelectedObjects:
            Object = SelectedObjects.Current 
            if type(Object) is Beam:
                print(type(Object) , " | длина: " , str(T3D.Distance.PointToPoint(Object.StartPoint,Object.EndPoint)))       
    except Exception as ex:
        print(ex)