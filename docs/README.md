## Прокси API для преобразования числа в текст
___
### Описание работы прокси API
Работа программы основана на требованиях тестового задания:

- прокси API принимает данные в JSON формате;<br/>
- преобразует полученные данные в XML;<br/>
- делает запрос на API Number Conversion Service
- получает ответ в XML формате;
- преобразует в JSON и возвращает ответ на запрос.

Более детально требования описаны в документе *TWIN_task_2_API_proxy.pdf*
___

### Запуск программы
Программа запускается из файла ***main.py***

Блок кода запуска программы из ***main.py***:

```python
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
```

___

###Ключевые источники информации
 - [FastAPI documentation][1]
 - [Number Conversion Service][2]
 - [XML Tutorial][3]
 - [The ElementTree XML API][4]
 - [Знакомство с XML][5]
 - [Что такое SOAP API][6]
 - [XML & ElementTree video lesson][7]

___

[1]:(https://fastapi.tiangolo.com/)
[2]:(https://www.dataaccess.com/webservicesserver/NumberConversion.wso?op=NumberToWords)
[3]:(https://www.w3schools.com/xml/)
[4]:(https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)
[5]:(https://blog.skillfactory.ru/glossary/xml/)
[6]:(https://blog.skillfactory.ru/glossary/soap-api/)
[7]:(https://www.youtube.com/watch?v=j0xr0-IAqyk&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=26)