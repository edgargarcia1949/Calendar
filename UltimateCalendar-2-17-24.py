import pygame, sys
from numbers import Number
import pygame_widgets
from pygame_widgets.textbox import TextBox
import datetime
from datetime import datetime, time
import calendar
import textwrap

pygame.font.init()
font12b = pygame.font.Font("OpenSans-Bold.ttf", 12)
font14 = pygame.font.Font("OpenSans-SemiBold.ttf", 14)
font14r = pygame.font.Font("OpenSans-Regular.ttf", 14)
font16b = pygame.font.Font("OpenSans-Bold.ttf", 16)
font18 = pygame.font.Font("OpenSans-SemiBold.ttf", 18)
font24 = pygame.font.Font("OpenSans-SemiBold.ttf", 24)
font25 = pygame.font.Font(None, 25)
font26b = pygame.font.Font("OpenSans-SemiBold.ttf", 26)
font24b = pygame.font.Font("OpenSans-Bold.ttf", 24)
font22b = pygame.font.Font("OpenSans-SemiBold.ttf", 22)
font40b = pygame.font.Font("OpenSans-SemiBold.ttf", 40)
font55b = pygame.font.Font("OpenSans-Bold.ttf", 55)
font65 = pygame.font.Font("OpenSans-SemiBold.ttf", 65)

BLACK, WHITE, BLUE, GREEN, MAROON = (0,0,0), (255,255,255), (0,0,255), (0,128,0), (128,0,0) 
PURPLE, TEAL, FUCHSIA, LIME, OLIVE = (128,0,128), (0,128,128), (255,0,255), (0,255,0), (128,128,0) 
NAVYBLUE, RED, ORANGE, AQUA, TAN = (0,0,128), (255,0,0), (255,165,0), (0,255,255), (255,255,200)

WIDTH = 924
HEIGHT = 714

Day = 0
Hour = 0
Year = datetime.now().year 
Month = datetime.now().month
BLPtr = 0

Colours = [BLUE, GREEN, MAROON, PURPLE, TEAL, FUCHSIA, LIME, OLIVE, NAVYBLUE, RED, ORANGE, AQUA]
MonthStrings=["DECEMBER", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
            "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", "JANUARY"]
WeekStringsShort=["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
WeekStringsLong=["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
DayNumbers=[" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15",
      "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
StartDayInMonth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]         # these need to be updated for year change
NumberOfDaysInMonth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]     # these need to be updated also
YOffset = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]                 # these too
CommentList2 = ['' for i in range(12) for j in range(31)]    # list of 372 empty strings for comment storage
BigList = []        # will hold 377 or 378 dates in 3 element list
HourList = ["7","8","9","10","11","12","1","2","3","4","5","6"]
hour_index = {"7":0, "8":1, "9":2, "10":3, "11":4, "12":5, "1":6, "2":7, "3":8, "4":9, "5":10, "6":11}
day_index = {"1":0, "2":1, "3":2, "4":3, "5":4, "6":5, "7":6}
CommentList = ['' for i in range(7) for j in range(12)]    # list of 84 empty strings for comment storage

x1, x2, x3 = 45, 283, 640
y1, y2, y3, y4, y5, y6 = 43, 68, 158, 183, 80, 12
sx1, sx2, sx3, sx4, sx5 = 34, 119, 238, 357, 833
sy1, sy2, sy3, sy4, sy5, sy6 = 90, 25, 115, 480, 13, 620
off1, yoff1, yoff2, yoff3 = 595, 80, 96, 120
X1, Y1, Y2, SX1, SY1 = 42, 86, 190, 210, 23

Rect1 = (x1, y2, sx1, sy1)      # x and y are position coordinates of rects
Rect2 = (x3, y2, sx1, sy1)      # sx and sy are widths and heights of rects
Rect3 = (x1, y3, sx2, sy2)
Rect4 = (x1, y1, sx3, sy2)
Rect5 = (x2, y1, sx4, sy3)
Rect6 = (x1, y4, sx5, sy4)
Rect7 = (42, 32, 840, 54)
Rect8 = (42, 32, 840, 625)

s1 = (["--> Advances 1 year", 240, 115, font14],
      ["<-- Goes back 1 year", 240, 140, font14],
      ["|  Outputs screen shot called", 251, 164, font14],
      ["V  YearlyCalendar...withdateandtime", 250, 178, font14],
      ["--> Advances 1 month", 240, 240, font14],
      ["<-- Goes back 1 month", 240, 265, font14],
      ["^ Toggles Text Boxes On/Off", 251, 287, font14],
      ["|", 251, 290, font14],
      ["|  Outputs screen shot called", 251, 314, font14],
      ["V  MonthlyCalendar...withdateandtime", 251, 328, font14],
      ["--> Advances 1 week", 240, 416, font14],
      ["<-- Goes back 1 week", 240, 440, font14],
      ["^ Toggles Text Boxes On/Off", 251, 462, font14],
      ["|", 251, 465, font14],
      ["|  Outputs screen shot called", 251, 489, font14],
      ["V  WeeklyCalendar...withdateandtime", 251, 502, font14],
      ["Month: 1-12 <ENTER> updates month", 549, 265, font14],
      ["Year: 1000-9999 <ENTER> updates year", 549, 287, font14],
      ["Day: 1-31 <ENTER> allows putting", 549, 314, font14],
      ["a comment in a certain date", 549, 329, font14],
      ["Comments: Type text <ENTER> allows up", 549, 354, font14],
      ["to 4 lines of comments in date", 549, 370, font14],
      ["Month: 1-12 <ENTER> goes to first week", 549, 435, font14],
      ["in month", 549, 447, font14],
      ["Day: 1-7 <ENTER> allows putting comments", 549, 464, font14],
      ["on a certain date", 548, 476, font14],
      ["Hour: 7-6 <ENTER> allows putting", 549, 491, font14],
      ["comments on a certain time", 549, 504, font14],
      ["Comments: Type text <ENTER> allows up to 3", 549, 524, font14],
      ["lines of comments in day at hour", 549, 538, font14],
      ["Delete key clears all comments", 549, 563, font14])
s2 = (["Instructions", 225, 15, font40b],
      ["Yearly Calendar:", 54, 108, font22b],
      ["Monthly Calendar:", 32, 233, font22b],
      ["Weekly Calendar:", 44, 409, font22b],
      ["Text Boxes", 615, 230, font22b],
      ["Text Boxes", 627, 398, font22b],  
      ["Select yearly - y", 126, 546, font22b],
      ["Select monthly - m", 102, 573, font22b],
      ["Select weekly - w", 115, 602, font22b],
      ["Return to Instructions - ESC", 23, 630, font22b])

def DoallRects():
    DoRects(*Rect1, Rect1[2], 7)    # left side small calendar rectangles
    DoRects(*Rect2, Rect2[2], 7)    # right side small calendar rectangles
    DoRects(*Rect3, Rect3[2], 7)    # day of week headings
    DoRects(*Rect4, off1, 2)         # small calendar headings
    DoRect(*Rect5)                  # month and year rectangle
    DoRect(*Rect6)                  # main body of calendar rectangle
    pygame.draw.rect(screen, BLACK, (x1, y1, sx5, sy6), 2)  # for looks
    
def DoallTexts(font):      
    if Month==1:
        DoText(MonthStrings[Month-1] + "  " + str(Year-1), x1, 39, sx3, sy2, BLACK, font)
    else:    
        DoText(MonthStrings[Month-1] + "  " + str(Year), x1, 39, sx3, sy2, BLACK, font)   # upper left calendar title
    if Month==12:
        DoText(MonthStrings[Month+1] + "  " + str(Year+1), x3, 39, sx3, sy2, BLACK, font)
    else:    
        DoText(MonthStrings[Month+1] + "  " + str(Year), x3, 39, sx3, sy2, BLACK, font)    # upper right calendar title
    [DoText(WeekStringsLong[i], x1 + i * sx2, y3-8, sx2, sy2, BLACK, font18)
    for i in range(7)]                       # display main body column titles
    [DoText(WeekStringsShort[j], x1 + i * off1 + j * sx1, 64, sx1, sy5, BLACK, font)    
    for i in range(2) for j in range(7)]     # display small cal headings
    
def DoRect(x, y, w, h):
    pygame.draw.rect(screen, BLACK, (x, y, w, h), 1)
  
def DoRects(x,y,w,h, offset, qty):    
    [DoRect(x+i*offset, y, w, h) for i in range(qty)]
    
def DoText(str, px, py, sx, sy, tuple, font):
    w, h = font.size(str)
    text = font.render(str, True, tuple)
    screen.blit(text, dest = (px+sx/2-w/2, py+sy/2-5))

def DoText2(str, x, y, font):
    text = font.render(str, True, BLACK)
    screen.blit(text, dest = (x, y))
    
def DoText3(str, x, y, font):
    text = font.render(str, True, BLUE)
    screen.blit(text, dest = (x, y))
    
def DoSmallCalYear(stday, dsinmo, x, y, font):
        counter=stday
        for i in range(dsinmo):
            DoText(DayNumbers[i], x+counter%7*30, y+counter//7*25, 30, 25, BLACK, font)
            counter+=1
            
def DoSmallCalMonth(stday, dsinmo, x, font):
        counter=stday
        for i in range(dsinmo):
            DoText(DayNumbers[i], x+counter%7*sx1, y5-3+counter//7*y6, sx1, sy5, BLACK, font)
            counter+=1    

def mthdata(y, m):
    data = calendar.monthrange(y, m)
    return (data[0]+1)%7, data[1]

def DayofWeek(y, m, d):
    data = calendar.weekday(y, m, d)
    return (data+1)%7

def UpdateYearArrays():         # puts data in 3 arrays when year changes
    for i in range(14):         # starting day of month, number of days in month
        if i==0 or i==13:       # and yoffset for y size of day boxes
            StartDayInMonth[0], NumberOfDaysInMonth[0] = mthdata(Year-1, 12)
            StartDayInMonth[13], NumberOfDaysInMonth[13] = mthdata(Year+1, 1)
        else:
            StartDayInMonth[i], NumberOfDaysInMonth[i] = mthdata(Year, i)
        YOffset[i]=yoff2    
        if StartDayInMonth[i]>=5 and NumberOfDaysInMonth[i]==31:    # happens about 3 times a year
            YOffset[i]=yoff1
        if StartDayInMonth[i]==6 and NumberOfDaysInMonth[i]>=30:
            YOffset[i]=yoff1
        if StartDayInMonth[2]==0 and NumberOfDaysInMonth[2]==28:    # happens about once in 10 years
            YOffset[2]=yoff3
            
def DoMonthArrays():
    for i in range(14):         # starting day of month, number of days in month
        if i==0 or i==13:       
            StartDayInMonth[0], NumberOfDaysInMonth[0] = mthdata(Year-1, 12)
            StartDayInMonth[13], NumberOfDaysInMonth[13] = mthdata(Year+1, 1)
        else:
            StartDayInMonth[i], NumberOfDaysInMonth[i] = mthdata(Year, i)
    [BigList.append([Year-1,12,i+26])        
    for i in range(6)]          # Create 377 or 378 member list with all dates                  
    [BigList.append([Year,i+1,j+1])    # from 6 days before the current year
    for i in range(12) for j in range(NumberOfDaysInMonth[i+1])]  # to 6 days after the current year
    [BigList.append([Year+1,1,i+1])                 
    for i in range(6)]
    
def DoGridBox(i, j):
    DoRect(42+j*120, 150+i*43, 120, 43)
    value = CommentList[i*7+j]       # if there is a comment in the CommentList list, then wordwrap it
    if value != '':
        wrapper = textwrap.TextWrapper(width = 18)    
        word_list=wrapper.wrap(text=value)
        counter2 = 0
        for line in word_list:
            DoText(line, 42+j*120, 134+i*43+(counter2*11), 120, 43, BLACK, font14r) # display it to screen
            counter2 += 1                                                          # one line at a time
            
def MonthTextBoxes(bool):  
    def outputMonth():
        global Month
        if(textbox.getText()).isdigit():
            if(int(textbox.getText())) >= 1 and (int(textbox.getText())) <= 12:
                Month = int(textbox.getText())
            
    def outputYear():
        global Year
        if(textbox2.getText()).isdigit():
            if(int(textbox2.getText())) >= 1000:
                Year = int(textbox2.getText())
                UpdateYearArrays()
            
    def outputDay():
        global Day
        if(textbox3.getText()).isdigit():
            if(int(textbox3.getText())) <= 31:
                Day = int(textbox3.getText())
            
    def outputComments():    
        CommentList2[(Month-1)*31+(Day-1)] = textbox4.getText()
        
    if bool:       
        global textbox
        textbox = TextBox(screen, 114, 673, 33, 25, colour=(TAN),
                          font = font25,
                          onSubmit=outputMonth, borderThickness=3)                            
 
        global textbox2
        textbox2 = TextBox(screen, 228, 673, 50, 25, colour=(TAN),
                           font = font25,                   
                           onSubmit=outputYear, borderThickness=3)

        global textbox3
        textbox3 = TextBox(screen, 347, 673, 33, 25, colour=(TAN),
                           font = font25, onSubmit=outputDay, borderThickness=3)

        global textbox4
        textbox4 = TextBox(screen, 515, 673, 360, 24, colour=(TAN),
                           font = font14r, onSubmit=outputComments, borderThickness=3)
    else:
        del textbox
        del textbox2
        del textbox3
        del textbox4
        
def WeekTextBoxes(bool):
    def outputMonth():
        global Month
        global BLPtr
        if(textbox.getText()).isdigit():
            if(int(textbox.getText())) >= 1 and (int(textbox.getText())) <= 12:
                Month = int(textbox.getText())
                BLPtr=BigList.index([Year, Month, 1])
                       
    def outputComments():    
        CommentList[Hour*7+Day] = textbox2.getText()
    
    def outputDay():
        global Day
        if(textbox3.getText()).isdigit():
            if(int(textbox3.getText())) >=1 and (int(textbox3.getText())) <= 7:
                Day = day_index[textbox3.getText()]
          
    def outputHour():
        global Hour
        if(textbox4.getText()).isdigit():
            if(int(textbox4.getText())) >=1 and (int(textbox4.getText())) <= 12:
                Hour = hour_index[textbox4.getText()]
                
    if bool:       
        global textbox
        textbox = TextBox(screen, 120, 673, 33, 25, colour=(TAN),
                          font = font25,
                          onSubmit=outputMonth, borderThickness=3)                            
 
        global textbox2
        textbox2 = TextBox(screen, 520, 673, 360, 24, colour=(TAN),
                           font = font14r,                   
                           onSubmit=outputComments, borderThickness=3)

        global textbox3
        textbox3 = TextBox(screen, 240, 673, 22, 25, colour=(TAN),
                           font = font25, onSubmit=outputDay, borderThickness=3)

        global textbox4
        textbox4 = TextBox(screen, 360, 673, 33, 25, colour=(TAN),
                           font = font25, onSubmit=outputHour, borderThickness=3)
    else:
        del textbox
        del textbox2
        del textbox3
        del textbox4
                
    
                       
def DoBigCal(stday, dsinmo, font):
    counter=stday
    if counter != 0:
        DoRect(x1, y4, counter%7*sx2, YOffset[Month])  # cleans up left side of top row
    for i in range(dsinmo):
        DoRect(x1+counter%7*sx2, y4+counter//7*YOffset[Month], sx2, YOffset[Month]) # big rectangle
        DoRect(x1+counter%7*sx2, y4+counter//7*YOffset[Month], 30, 30)    # small rectangle
        DoText(DayNumbers[i], x1+counter%7*sx2, y4-9+counter//7*YOffset[Month], 30, 22, BLACK, font)   # number in small rectangle
        value = CommentList2[(Month-1)*31+(i)]       # if there is a comment in the CommentList2 list, then wordwrap it
        if value != '':
            wrapper = textwrap.TextWrapper(width = 16)    
            word_list=wrapper.wrap(text=value)
            counter2 = 0
            for line in word_list:
                DoText(line, x1+counter%7*sx2, 198+counter//7*YOffset[Month]+(counter2*11), 119, 50, BLACK, font14r) # display it to screen
                counter2 += 1                                                                                       # one line at a time       
        counter+=1
    if 0<counter%7<=6:
        DoRect(x1+counter%7*sx2, y4+counter//7*YOffset[Month], (7-counter%7)*sx2, YOffset[Month]) # cleans up right side of bottom row
            
def DisplayYear():
        screen.fill(WHITE)
        pygame.display.set_caption("Yearly Calendar")
        DoRect(*Rect7)        # top rect around year number
        for i in range (4):
            for j in range (3):
                DoRect(X1+i*SX1, Y1+j*Y2, SX1, SY1)        # rectangle around month name
                DoRect(X1+i*SX1, Y1+j*Y2, SX1, Y2)        # rectangle to separate months
                DoText(MonthStrings[i+1+j*4], X1+i*SX1, 74+j*Y2, SX1, SY1, Colours[i+j*4], font24b)   # display month names
        DoRect(*Rect8)          # rect around body of calendar       
        DoText(str(Year), X1-30, 15, 900, 5, Colours[Month-1], font65)      # display year in big letters
        [DoText(WeekStringsShort[k], 43+k*30+i*SX1, 102+j*Y2, 30, SY1, BLACK, font12b)
        for i in range (4) for j in range (3) for k in range(7)]  # display SUN through SAT 12 times                   
        [DoSmallCalYear(StartDayInMonth[1+i+j*4], NumberOfDaysInMonth[1+i+j*4], 42+i*SX1, 114+j*Y2, font16b)
        for i in range (4) for j in range (3)]                    # displays all 12 small calendars                                   
        pygame.display.update()
        
def DisplayMonth():                        
    screen.fill(WHITE)  #clear background        
    pygame.display.set_caption("Monthly Calendar")      #draw scene
    DoallRects()               # draw 26 rectangles to make monthly calendar
    DoallTexts(font14)               # put all texts where they belong
    DoSmallCalMonth(StartDayInMonth[Month-1], NumberOfDaysInMonth[Month-1], x1, font14)
    DoSmallCalMonth(StartDayInMonth[Month+1], NumberOfDaysInMonth[Month+1], x3, font14)
    DoBigCal(StartDayInMonth[Month], NumberOfDaysInMonth[Month], font24)
    DoText(MonthStrings[Month], x2, 16, sx4, 40, Colours[Month-1], font55b)     # display current month
    DoText(str(Year), x2, 75, sx4, 35, Colours[Month-1], font55b)           # display current year
    if ShowTextBoxes:
        pygame_widgets.update(events)      # text boxes can be turned off with up arrow
        DoText("MONTH:", 34, 665, 80, 25, BLACK, font18)
        DoText("YEAR:", 150, 665, 100, 25, BLACK, font18)
        DoText("DAY:", 294, 665, 60, 25, BLACK, font18)
        DoText("COMMENTS:", 402, 665, 110, 25, BLACK, font18)
    pygame.display.update()
    
def DisplayWeek():
    screen.fill(WHITE)  #clear background        
    pygame.display.set_caption("Weekly Calendar")      #draw scene
    DoRect(42, 75, 841, 591)
    DoRects(42, 75, 120, 75, 120, 7)
    [DoGridBox(i, j) for i in range(12) for j in range(7)]  # draws grid rectangles and text if necessary                              
    DoText("Weekly Calendar  "+str(Year), 92, 5, 233, 25, BLUE, font26b)        # display text on left side  
    dayofweek=DayofWeek(*BigList[BLPtr])
    temp=BLPtr-dayofweek
    temp2=BLPtr+6-dayofweek
    DoText(str(BigList[temp][1])+"/"+str(BigList[temp][2])+"/"+str(BigList[temp][0])    # display text on right side
         +" - "+str(BigList[temp2][1])+"/"+str(BigList[temp2][2])+"/"+str(BigList[temp2][0]),
         525, 5, 366, 25, BLUE, font26b)
    for i in range(7):
        temp=BLPtr+i-dayofweek
        DoText(MonthStrings[BigList[temp][1]], 42+i*120, 66, 120, 20, Colours[BigList[temp][1]-1], font18)  # display Month
        DoText(WeekStringsLong[i], 42+i*120, 123, 120, 20, Colours[BigList[temp][1]-1], font18)             # display day of week
        DoText(DayNumbers[BigList[temp][2]-1], 70+i*120, 63, 50, 30, BLACK, font55b)                         # display large day number 
        [DoText(HourList[i], 42+j*120, 158+i*43, 15, 15, BLACK, font14r)                                     # display 7 - 6
        for i in range(12) for j in range(7)]
    if ShowTextBoxes:
        pygame_widgets.update(events)      # text boxes can be turned off with up arrow
        DoText("MONTH:", 39, 665, 80, 25, BLACK, font18)
        DoText("DAY:", 177, 665, 80, 25, BLACK, font18)
        DoText("HOUR:", 287, 665, 80, 25, BLACK, font18)
        DoText("COMMENTS:", 409, 665, 110, 25, BLACK, font18)           
    pygame.display.update() 
    

def DisplayInstructions():
        pygame.display.set_caption("Instructions")
        screen.fill(WHITE)
        [DoText2(*line) for line in s1]
        [DoText3(*line) for line in s2]
        pygame.display.update() 

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
UpdateYearArrays()
DoMonthArrays()
BLPtr=BigList.index([Year, Month, 1])       # BLPtr points to location in BigList of first day of Month
dayofweek=0                                 # this variable will hold the day of the week the first falls on
ShowYear = False
ShowMonth = False
ShowWeek = False
ShowInstructions = True
ShowTextBoxes = True
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if ShowInstructions:               
                if event.key == pygame.K_y:
                    ShowYear = True         # Display Yearly Calendar
                    ShowInstructions = False
                if event.key == pygame.K_m:
                    ShowMonth = True        # Display Monthly Calendar
                    ShowInstructions = False
                    MonthTextBoxes(True)    # set up Month text boxes
                if event.key == pygame.K_w:
                    ShowWeek = True
                    ShowInstructions = False
                    WeekTextBoxes(True)     # set up Week text boxes
            if ShowYear:
                if event.key == pygame.K_LEFT:
                    Year-=1
                    UpdateYearArrays()
                if event.key == pygame.K_RIGHT:
                    Year+=1
                    UpdateYearArrays()
                if event.key == pygame.K_DOWN:
                    pygame.image.save(screen, datetime.now().strftime("YearlyCalendar-%m-%d-%y-%H-%M-%S")+".png")
                if event.key == pygame.K_ESCAPE:
                    Year = datetime.now().year
                    UpdateYearArrays()
                    ShowYear = False
                    ShowInstructions = True
            if ShowMonth:
                if event.key == pygame.K_LEFT:    
                    Month=Month - 1
                    if Month==0:
                        Month=12
                        Year=Year-1
                        UpdateYearArrays()
                if event.key == pygame.K_RIGHT:
                    Month=Month+1
                    if Month==13:
                        Month=1
                        Year=Year+1
                        UpdateYearArrays()
                if event.key == pygame.K_UP:
                    ShowTextBoxes = not ShowTextBoxes 
                if event.key == pygame.K_DOWN:
                    pygame.image.save(screen, datetime.now().strftime("MonthlyCalendar-%m-%d-%y-%H-%M-%S")+".png")
                if event.key == pygame.K_ESCAPE:
                    Year = datetime.now().year
                    Month = datetime.now().month
                    UpdateYearArrays()
                    MonthTextBoxes(False)   # delete Month text boxes
                    ShowMonth = False
                    ShowInstructions = True
            if ShowWeek:
                if event.key == pygame.K_LEFT:      # left arrow goes back one week
                    if DayofWeek(Year, 1, 1)>=4:    # if January starts on Thursday, Friday or Saturday we use 7
                        if BLPtr-7>0:
                            BLPtr-=7
                    else:
                        if BLPtr-14>0:              # if January starts on Sunday through Wednesday we use 14 to prevent error
                            BLPtr-=7
                if event.key == pygame.K_RIGHT:     # right arrow advances one week
                    if DayofWeek(Year, 12, 1)>=5:   # if December starts on a Friday or Saturday we use 7
                        if BLPtr+7<=len(BigList)-1:
                            BLPtr+=7
                    else:
                        if BLPtr+14<=len(BigList)-1:    # if December starts on a Sunday through Thursday we use 14 to prevent error
                            BLPtr+=7 
                if event.key == pygame.K_UP:            # up arrow toggles showing of text boxes
                    ShowTextBoxes = not ShowTextBoxes
                if event.key == pygame.K_DOWN:
                    pygame.image.save(screen, datetime.now().strftime("WeeklyCalendar-%m-%d-%y-%H-%M-%S")+".png")    
                if event.key == pygame.K_DELETE:        # delete key re-initializes comment list
                    CommentList = ['' for i in range(7) for j in range(12)]
                if event.key == pygame.K_ESCAPE:
                    Month = datetime.now().month
                    BLPtr = BigList.index([Year, Month, 1])
                    WeekTextBoxes(False)   # delete Week text boxes
                    ShowWeek = False
                    ShowInstructions = True    
                    
    if ShowYear:
        DisplayYear()
    if ShowMonth:
        DisplayMonth()
    if ShowWeek:
        DisplayWeek()
    if ShowInstructions:
        DisplayInstructions()
       
         

    
