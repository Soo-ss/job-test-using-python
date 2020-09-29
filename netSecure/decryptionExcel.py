import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

# 반드시 절대경로
filename = "C:\\Users\\dj532\\VSCODE\\netSecure\\test.xlsx"

f = open("passwordList.txt")
for x in f.readlines():
    try:
        wb = excel.Workbooks.Open(filename, 0, True, None, x.strip())
        print(x)
    except:
        continue

