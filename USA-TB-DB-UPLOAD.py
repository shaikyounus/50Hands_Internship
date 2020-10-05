import pymysql.cursors
f=open(r"USA-TB-States.csv","r")
fString=f.read()
fList=[]



for line in fString.split('\n'):
    fList.append(line.split(','))

# Connect to the database
#connection = pymysql.connect(host="",
                             #user="",
                             #password="",
                             #db="")

connection = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             db="sampletestdb")


rows=""
try:

    
    with connection.cursor() as cursor:
        cursor.execute("""DROP TABLE IF EXISTS USA_Comorbidity_TB_Province_level""")
        cursor.execute("""CREATE TABLE USA_Comorbidity_TB_Province_level
(

ReportingArea text(255),
cases_2018 text(200),
cases_2017 text(200),
caserates_2018 text(200),
caserates_2017 text(200),
rank_2018 text(200),
rank_2017 text(200)
)
""")
        

    
        
        for i in range(3,len(fList)-16):
            #fList[i][1]=db.escape_string(fList[i][1])
            
            rows+="('{}','{}','{}','{}','{}','{}','{}')".format(str(fList[i][1]),str(fList[i][2]),str(fList[i][3]),str(fList[i][4]),str(fList[i][5]),str(fList[i][6]),str(fList[i][7]))
                                       
            if i!=len(fList)-17:
                
                rows+=','
                
                                       
                                       
                            
                                           
                
                                    




        
        queryInsert="""


INSERT INTO USA_Comorbidity_TB_Province_level VALUES """+rows
        cursor.execute(queryInsert)
        

        connection.commit()
    
    
 
        
finally:
    connection.close()






