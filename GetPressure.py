#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests_html import HTMLSession


# In[106]:


import time


# In[2]:


session = HTMLSession()


# In[3]:


url = 'https://weather.gc.ca/city/pages/bc-96_metric_e.html'


# In[4]:


r = session.get(url)


# In[102]:


sel = 'body > main > div > div#mainContent > section:nth-child(1) > details.panel.panel-default.hidden-xs > div.row.no-gutters.wb-eqht.hidden-print > div.col-sm-10.text-center > div > div:nth-child(1) > dl > dd.mrgn-bttm-0.wxo-metric-hide'


# In[103]:


result0 = r.html.find(sel)

sel1 = 'body > main > div > div#mainContent > section:nth-child(1) > details.panel.panel-default.visible-xs.wxo-obs.mrgn-bttm-md.mrgn-tp-sm > details > dl > dd:nth-child(2)'

result1 = r.html.find(sel1)
# In[112]:



record = open('/home/debian/nas_home/git/daily_riun/record.csv','a')
record.write(','.join(result1[0].text.split())+','+result0[0].text+'\n')
record.close()




