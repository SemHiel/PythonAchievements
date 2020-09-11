Microsoft Windows [Version 10.0.19041.508]
(c) 2020 Microsoft Corporation. All rights reserved.

C:\Users\Sequos>py
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Sem Hiel')
Mijn naam is Sem Hiel
>>> naam = 'Sem Hiel'
>>> print(naam)
Sem Hiel
>>> print(naam.upper())
SEM HIEL
>>> print(naam[0:2])
Se
>>> print(naam[::-1])
leiH meS
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Sem Hiel ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
...
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
340
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
371
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 371
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-11 14:08:56.992270
>>> dataum.strftime('%A %d %B %Y')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dataum' is not defined
>>> datum.strftime('%A %d %B %Y')
'Friday 11 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 11 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 11 settembre 2020'
>>>
