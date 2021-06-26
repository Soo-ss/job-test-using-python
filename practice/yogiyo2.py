def solution(S):
    arr = S.split("\n")
    del arr[-1]
    del arr[0]
    # print(len(arr))

    for item in arr:
        item = item.strip()
        # print(item)

    answer = len(arr)
    print(arr)

    return str(answer)


solution(
    """
  root r-x delete-this.xls
  root r-- bug-report.pdf
  root r-- doc.xls
  root r-- podcast.flac
 alice r-- system.xls
  root --x invoices.pdf
 admin rwx SETUP.PY
"""
)