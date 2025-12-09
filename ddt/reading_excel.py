import xlrd

def read_testdata(filepath,sheetname,val=1):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    d={}
    for ele in rows:
        d[ele[0].value] = ele[val].value
    return d

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    for ele in rows:
        #d[key] = value ---> to add data to dictionary
        d[ele[0].value]= ele[1].value
        # print(d)
        # print(d['firstname'])
    return d

# path = r'C:\Users\User\PycharmProjects\Selenium_Training\trianing\Files\demo_data.xlsx'
# print(read_testdata(path,'registration'))

