# Automatically tracking new circulars and reports shared by regulators

Project started : 0:50 , 29/10/2017 | PwC challenge #11, Hack2Innovate Hackathon (2 Day), IIT-G

Our approach/solution 

Dependencies :
          
      amqp==2.2.2
      billiard==3.5.0.3
      celery==4.1.0
      certifi==2017.7.27.1
      cffi==1.11.2
      chardet==3.0.4
      Django==1.11.6
      django-debug-toolbar==1.8
      django-environ==0.4.4
      idna==2.6
      kombu==4.1.0
      oauthlib==2.0.6
      pyasn1==0.3.7
      pycparser==2.18
      pytz==2017.2
      requests==2.18.4
      requests-oauthlib==0.8.0
      six==1.11.0
      sqlparse==0.2.4
      tweepy==3.5.0
      urllib3==1.22
      vine==1.1.4
      
 To run:
 
      >>> ./manage.py runserver --settings=config.settings.local
      localhost:8080 - WebUI


------------------------------------------------------------------------------------------------



------------------------------------------------------------------------------------------------
 Twitter Bot
--------------------------------
The twitter bot (tweetbot) is programmed to follow the tweets of Government officials & Goverment/Political bodies or organisation.It will scrape the bio of all the channels found and will save it in a json file.

The json file is forwarded to the DNN.

------------------------------------------------------------------------------------------------
Training the Deep Neural network 
--------------------------------
Tensorflow DNN is trained with gradient decent, with bio data fed from dataBO.json scrapped by the twitter bot.
This is used to decide if the bot will follow a user from government or regulatory body or not.

Correctness ~ 80 %

![test_result](https://github.com/geekodour/p4pwc/blob/master/test_res.PNG)

------------------------------------------------------------------------------------------------
Feature Exraction using NLP 
--------------------------------
The twitter runs periodically searching for circulars & reports in the following users timelines.It extracts the information like date , time , bio from the user.

------------------------------------------------------------------------------------------------
FINAL WEBAPP UI
---------------------------------------------
The latest 

![ui](https://github.com/geekodour/p4pwc/blob/master/ui.PNG)

------------------------------------------------------------------------------------------------
Future Scope : Crawl Bot 

   Due to lack of time, we couldn't complete the crawlbot.But the Idea is to crawl websites for government officials and regulators.Basically to search for circulars and reports.





