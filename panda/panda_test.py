import sys

from direct.showbase.ShowBase import ShowBase
 
class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)

print(sys.version)
app = MyApp()
app.run()
