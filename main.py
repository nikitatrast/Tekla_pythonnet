from .init import *
from .worker import *


class MyWindow(Window):
    def __init__(self):
        try:
            
            stream = StreamReader(os.getcwd()+r'.\gui.xaml')
            self.window = XamlReader.Load(stream.BaseStream)
            self.button1inXAML = LogicalTreeHelper.FindLogicalNode(self.window, "button1")
            self.button2inXAML = LogicalTreeHelper.FindLogicalNode(self.window, "button2")
            self.button1inXAML.Click +=  RoutedEventHandler(self.button1_Click)
            self.button2inXAML.Click +=  RoutedEventHandler(self.button2_Click)
            Application().Run(self.window)
        except Exception as ex:
            print(ex)

    def button1_Click(self, sender, e):
        CreateBeam()
    def button2_Click(self, sender, e):
        ReadBeams()

if __name__ == '__main__':
    thread = Thread(ThreadStart(MyWindow))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()
    thread.Join()