import requests
import xml.etree.ElementTree as ET
from data_access_service import namespaces, DATA_ACCESS_API_URL
from schemas import ParserException
from fastapi import HTTPException


def create_soap_envelope(body: str):
    """

    :param body:
    :return:
    """
    return f"""<?xml version="1.0" encoding="utf-8"?>
                <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                  <soap12:Body>
                    {body}
                  </soap12:Body>
                </soap12:Envelope>"""


def create_number_to_words_soap_message(number: int):
    """

    :param number:
    :return:
    """
    return create_soap_envelope(f"""<NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
                                      <ubiNum>{number}</ubiNum>
                                    </NumberToWords>""")


def number_to_words_parser(response_xml: str):
    """
    Находит в ответе число в виде текста.
    :param response_xml:
    :return:
    """
    root = ET.fromstring(response_xml)
    body = root.find("soap:Body", namespaces)
    if body is not None:
        response = body.find('m:NumberToWordsResponse', namespaces)
        if response is not None:
            result = response.find('m:NumberToWordsResult', namespaces)
            if result is not None:
                return result.text

    raise ParserException(response_xml)


def send_soap_request(message: str, response_parser=None):
    """

    :param message:
    :param response_parser:
    :return:
    """
    headers = {"Content-Type": "application/soap+xml; charset=utf-8"}
    response = requests.request("POST", DATA_ACCESS_API_URL, headers=headers, data=message)
    if not response.ok:
        raise HTTPException(response.status_code)

    return response_parser(response.text) if response_parser is not None else response
