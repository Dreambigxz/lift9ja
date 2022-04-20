import datetime
from variables import *
from emails_list import emails



def send_mail():

    COMPANY = 'Loan Company'

    html_message = loader.render_to_string('mail/mail.html', {
        'name': 'name',
        'sitename': COMPANY,

    })

    data = {
        'Messages': [
            {
                "From": {
                    "Email": settings.EMAIL_DELIVERY,
                    "Name": COMPANY
                },
                "To": [
                    {
                        "Email": 'donyemordi@gmail.com',
                        "Name": ""
                    }
                ],
                "Subject": COMPANY,
                "HTMLPart": html_message,
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }

    mail = mailjet.send.create(data=data)
    print(mail)




def mail():

    Subject = 'Business Partnership Proposal'
    COMPANY = 'Royal Credit Union'
    email = 'noreply@peektop.com'

    company_name = 'Airbus'

    emails = [
        # 'donyemordi@gmail.com',
        # 'derrickanderson780@yahoo.com',

        # 'navantia@navantia.es'
        # 'press@ryanfournier.com'
        # 'investorrelations@gestamp.com'
        # 'redessociales@repsol.com'

        # 'info.na@byd.com'
        # 'gwmomd@gwm.cn'

        # 'ShengNan.Yang.VW@faw-vw.com'
        # 'ShengNan.Yang.VW@faw-vw.com'

        'dataprotection@airbus.com'
    ]


    for i in emails:
        print(i)
        html_message = loader.render_to_string('mail/mail.html', {
            'img': 'https://royalcu.herokuapp.com/static/Content/Assets/images/rcu-logo-512-trans.png',
            'company_name': company_name

        })

        data = {
            'Messages': [
                {
                    "Headers": {
                        "Reply-to": "royalcumarketing@peektop.com"
                    },

                    "From": {
                        "Email": email,
                        "Name": COMPANY
                    },

                    "To": [
                        {
                            "Email": i,
                            "Name": ''
                        }
                    ],
                    "Subject": Subject,
                    "HTMLPart": html_message,
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }


        s = mailjet.send.create(data=data)
        print(s.json())
        print(s.status_code)
        print('Mail Sent')
