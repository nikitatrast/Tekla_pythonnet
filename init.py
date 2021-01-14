import clr, sys,os


clr.AddReference(r"wpf\PresentationFramework")

from System import *
from System.IO import *
from System.Windows.Markup import XamlReader
from System.Windows import *
from System.Threading import Thread, ThreadStart, ApartmentState
from System.Windows.Controls import *
from System.Collections import *
from System.Collections.Generic import *
from System.Linq import *
from System.Text import *
from System.Threading.Tasks import *
from System.Data import *
from System.Windows.Data import *
from System.Windows.Documents import *
from System.Windows.Input import *
from System.Windows.Media import *
from System.Windows.Media.Imaging import *
from System.Windows.Navigation import *
from System.Windows.Resources import *
from System.Windows.Shapes import *
from System.Windows.Data import *
from System.Windows.Data import *
from System.Linq import *
from System.Linq import *
from System.Linq import *
from System.Linq import *
from System.Linq import *
from System.Linq import *
from System.Linq import *

sys.path.append(r"C:\TeklaStructures\2020.0\nt\bin\plugins")
from Tekla.Structures import *
from Tekla.Structures.Model import *

from Tekla.Structures import Geometry3d as T3D
from Tekla.Structures.Model import UI as TUI
from Tekla.Structures.Model import Operations as TMO

