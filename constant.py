YEAR = "111"
SEM = "1"

def URL(id):
    return "https://newdoc.nccu.edu.tw/teaschm/" + YEAR + SEM + "/statistic.jsp-tnum=" + id + ".htm"

def COURSE_RATE_URL(param):
    return "https://newdoc.nccu.edu.tw/teaschm/" + YEAR + SEM + "/" + param