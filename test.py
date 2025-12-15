hrs=input("Enter hours:")
rte=input("Enter Rate:")
h=float(hrs)
r=float(rte)
def computepay(h, r):
    if h > 40:
        regular=40*r
        overtime= (h-40)*r*1.5
        Pay= overtime+regular
    else: 
        Pay= h*r
    return Pay

x= computepay(h,r)
print("Pay", x)