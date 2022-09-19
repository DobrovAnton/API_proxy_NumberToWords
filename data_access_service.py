# Веб-служба, предоставляющая функцию преобразования числа в слово.
# Возвращает слово, соответствующее положительному числу, переданному в качестве параметра. Ограничено квадриллионами.
DATA_ACCESS_API_URL = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?op=NumberToWords'


# Словарь с префиксами для парсинга ответов запроса.
# https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
namespaces = {
    "soap": "http://www.w3.org/2003/05/soap-envelope",
    "m": "http://www.dataaccess.com/webservicesserver/"
}

