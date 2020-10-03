Attribute VB_Name = "Module1"
Sub stock():


  lastrow = ActiveSheet.Cells(Rows.Count, 1).End(xlUp).Row

  'create variables for headers
  Dim ticker As String
  Dim yrchange As Double
  Dim ptchange As Double
  Dim volume As Double
  Dim yo As Double
  Dim yc As Double

  ' define output table row
  Dim tablerow As Integer
  tablerow = 2



  ' titles for columns
  Cells(1, 9).Value = "Ticker"
  Cells(1, 10).Value = "Yearly Change"
  Cells(1, 11).Value = "Percent Change"
  Cells(1, 12).Value = "Total stock Volume"



  ' create loop
  For r = 2 To lastrow



    If Cells(r - 1, 1).Value <> Cells(r, 1).Value Then

      yo = Cells(r, 3).Value

      volume = Cells(r, 7).Value



    ElseIf Cells(r + 1, 1).Value <> Cells(r, 1).Value Then

      ticker = Cells(r, 1).Value

      yc = Cells(r, 6).Value

      yrchange = (yc - yo)
      ptchange = (yrchange / yo) * 100

      volume = Cells(r, 7).Value + volume



      Cells(tablerow, 9).Value = ticker
      Cells(tablerow, 10).Value = yrchange
      Cells(tablerow, 11).Value = ptchange
      Cells(tablerow, 12).Value = volume

      tablerow = tablerow + 1

      volume = 0


    Else

      volume = Cells(r, 7).Value + volume

      ticker = Cells(r, 1).Value

      Cells(tablerow, 9).Value = ticker
      Cells(tablerow, 10).Value = yrchange
      Cells(tablerow, 11).Value = ptchange
      Cells(tablerow, 12).Value = volume
    
    'volume = 0

      



    End If

    

  Next r


End Sub
