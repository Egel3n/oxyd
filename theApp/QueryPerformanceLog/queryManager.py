class queryManager:
    query = "Select * from QueryPerformanceLog_queryperformancelog WHERE"
    modified = False

    def addHostnameFilter(self,hostname):
        if len(hostname) > 0:
            self.query = self.query + " " + f"Hostname LIKE '%%{hostname}%%' AND"
            self.modified = True

    def addUsernameFilter(self,username):
        if len(username) > 0:
            self.query = self.query + " " + f"UserName LIKE '%%{username}%%' AND"
            self.modified = True

    def addAppnameFilter(self,appname):
        if len(appname)>0:
            self.query = self.query + " "+ f"AppName LIKE '%%{appname}%%' AND"
            self.modified = True

    def  addQueryFilter(self,sqlQuery):
        if len(sqlQuery)>0:
            self.query = self.query + " "+ f"SqlText LIKE '%%{sqlQuery}%%' AND"
            self.modified = True
    
    def addDurationFilter(self,durationFrom,durationTo):

        if len(durationFrom) > 0 and len(durationTo) > 0:
            self.query = self.query + " " + f"Duration BETWEEN {durationFrom} AND {durationTo} AND"
            self.modified = True

        elif len(durationFrom) > 0:
            self.query = self.query + " " + f"Duration > {durationFrom} AND"
            self.modified = True

        elif len(durationTo) > 0:
            self.query = self.query + " " + f"Duration < {durationTo} AND"
            self.modified = True


    def addDateFilter(self,dateFrom,dateTo):
     
        if len(dateFrom) > 0 and len(dateTo) > 0:
            self.query = self.query  + " " + f"EVENTDATE BETWEEN '{dateFrom}' AND '{dateTo}' AND"
            self.modified = True
        
        elif len(dateFrom) > 0:
            self.query = self.query + " " + f"EVENTDATE > '{dateFrom}' AND"
            self.modified = True
        
        elif len(dateTo) > 0:
            self.query = self.query + " " + f"EVENTDATE < '{dateTo}' AND"
            self.modified = True


    def addDatabaseIDFilter(self,databaseID):
        if len(databaseID) > 0:
            self.query = self.query + " " + f"DATABASEID = {databaseID} AND"
            self.modified = True
    
    def addSessionIDFilter(self,sessionID):
        if len(sessionID) > 0:
            self.query = self.query + " " + f"SESSIONID = {sessionID} AND"
            self.modified = True



    
    def __str__(self) -> str:
        if self.modified == False:
            return self.query.replace("WHERE","")

        if self.modified == True:
            return self.query[:-3]