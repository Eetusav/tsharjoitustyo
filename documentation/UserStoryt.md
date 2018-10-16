## K�ytt�j�

K�ytt�j� voi ilman kirjautumista tarkastella mit� keskusteluita sivut sis�lt��. Keskustelun kommentteja ei kuitenkaan n�e ilman kirjautumista.

Kirjautumisen j�lkeen k�ytt�j� voi tarkastella sovelluksessa olevia keskusteluita, lis�t� niihin vastauksia, poistamaan niit� sek� aloittaa uusia keskusteluja.

K�ytt�j� pystyy poistamaan omia aloittamiaan keskusteluita ja lis�ksi muokkaamaan aloittamiaan keskusteluita.

K�ytt�j� pystyy tilaamaan keskustelun, jolloinka se n�kyy erillisell� tilaukset-sivulla. Tilauksen pystyy my�s poistamaan.

K�ytt�j� pystyy my�s tarkastelemaan kommenttien ja keskusteluiden m��ri�.

## SQL-kyselyt

### Kysely tilausten hakemiselle. Parametrina account id.
"SELECT Conversation.id, Conversation.name, Subs.conversation_id, (select COUNT(Subs.conversation_id) FROM Subs WHERE Subs.account_id=:accid) FROM Conversation LEFT JOIN Subs ON Subs.conversation_id=Conversation.id WHERE Subs.account_id=:accid"

### Kysely keskustelun kommenttien hakuun. Parametrina keskustelun id.
"SELECT Comment.id, Comment.name, Comment.conversation_id, Account.username, Comment.account_id, Comment.date_created,  (select COUNT(Comment.id) FROM Comment WHERE Comment.conversation_id=:convid) FROM Comment, Account WHERE Account.id = Comment.account_id AND Comment.conversation_id = :convid"

### Kysely keskustelun kommenttien poistamiseen. Parametrina keskustelun id. (keskustelun poistamisen yhteydess�)
"DELETE FROM Comment WHERE Comment.conversation_id = :convid"