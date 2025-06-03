from news import template

type = 'international'

#聯合新聞網
def udn():
    return template.udn(type)

#自由電子報
def itn():
    return template.itn(type)

#蘋果新聞網
def apple():
    return template.apple(type)

#三立新聞網
def setn():
    return template.setn(type)

#ETtoday
def ettoday():
    return template.ettoday(type)