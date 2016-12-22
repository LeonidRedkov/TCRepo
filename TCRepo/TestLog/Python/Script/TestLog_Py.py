#
#  This example demonstrates how to post messages and images to
#  TestComplete's test log.
#

def rgb(r, g, b):
  def tobyte(c):
    return 0 if c < 0 else (255 if c > 255 else c)
  return (tobyte(b) << 16) | (tobyte(g) << 8) | tobyte(r)

def testLog():
  Log.Message("A message")
  Log.Checkpoint("A checkpoint")
  Log.Warning("A warning")
  Log.Error("An error")
  Log.Event("An event")

  Log.Message("A message", "An expanded message")
  Log.Checkpoint("A checkpoint", "An expanded checkpoint")
  Log.Warning("A warning", "An expanded warning")
  Log.Error("An error", "An expanded error")
  Log.Event("An event", "An expanded event")
  
  oLogAttr = Log.CreateNewAttributes()
  oLogAttr.Bold = True
  
  nFirstFolderID = Log.CreateFolder("First folder", "Use folders to group similar fragments of log messages")
  nSecondFolderID = Log.CreateFolder("Second folder", "", pmLowest, oLogAttr)
  oLogAttr.Bold = False
  oLogAttr.Italic = True
  nChildFolderID = Log.CreateFolder("Another level folder", "", pmNormal, oLogAttr, nFirstFolderID)
  
  Log.PushLogFolder(nFirstFolderID)  

  Log.Picture(Sys.Desktop.Picture(0, 0, 100, 100), "Sys.Desktop.Picture(0, 0, 100, 100)")
  Log.Picture(Sys.Desktop.PictureUnderMouse[40, 40], "Sys.Desktop.PictureUnderMouse", "A rectangle with the mouse cursor in the center")

  Log.PushLogFolder(nChildFolderID)

  Log.Message("A message", "A message with priority = pmLowest", pmLowest)
  Log.Warning("A warning", "A warning with priority = pmLower", pmLower)
  Log.Message("A message", "A message with priority = pmNormal", pmNormal)
  Log.Checkpoint("A checkpoint", "A checkpoint with priority = pmLower", pmLower)
  Log.Error("An error", "An error with priority = pmHigher", pmHigher)
  Log.Event("An event", "An event with priority = pmHighest", pmHighest)
  
  Log.PopLogFolder()
  Log.PopLogFolder()
  
  Log.Message("A message", "Priority = 9 (Can be used as a tag)", 9)

  oLogAttr.Italic = False
  oLogAttr.FontColor = rgb(192, 0, 0)
  oLogAttr.BackColor = rgb(255, 255, 0) 
  oImage = Sys.Desktop.Picture()
  
  Log.Message("Error Count = {0}".format(Log.ErrCount), "", pmNormal, oLogAttr, oImage, nSecondFolderID)
  Log.Message("Warning Count = {0}".format(Log.WrnCount), "", pmNormal, oLogAttr, oImage, nSecondFolderID)
  Log.Message("Event Count = {0}".format(Log.EvnCount), "", pmNormal, oLogAttr, oImage, nSecondFolderID)
  Log.Message("Image Count = {0}".format(Log.ImgCount), "", pmNormal, oLogAttr, 0, nSecondFolderID) 
  Log.Message("Message Count = {0}".format(Log.MsgCount), "", pmNormal, oLogAttr, 0, nSecondFolderID)