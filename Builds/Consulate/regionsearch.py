from pytrends.request import TrendReq

pytrends = TrendReq()
region = input("Enter the region you want to search for: ")
trending = pytrends.trending_searches(pn=region)
print(trending)