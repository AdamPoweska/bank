from django.db import models

"""
1) model z podstawowymi informacjami o koncie: 
numer konta, 
dane użytkownika (imię i nazwisko, można dodać więcej żeby wyglądało bardziej profesjonalnie),
waluta,
saldo otwarcia (zawsze na zero),
aktywność + -,
saldo zamknięcia

- może przyjąć tylko jeden request w danej chwili (async)
- komunikat o błędzie jeśli np. są za małe środki na koncie (jakiś duży czerwony komunikat z htmx'a)

2) Subkonta oszczędnościowe:
dziedziczą po powyższym ale mają zamrożone środki (dla ułatwienia na razie na jeden i ten sam procent)

3) model zbiorczy banku:
- dziedziczy powyższy model, zawiera w sobie jego wszystkie dane
- pokazuje ilość środków zdeponowanych przez użytkowników w danych valutach,
- pokazuje ilość środków na danych lokatach (ile bank może używać),
    - może pokazywać w co są zainwestowane te pieniądze
        - i jak wyglądają zyski z tych investycji vs. to co trzeba zwrócić jako %.

"""