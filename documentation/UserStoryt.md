## Käyttäjä

Käyttäjä voi ilman kirjautumista tarkastella mitä keskusteluita sivut sisältää. Keskustelun kommentteja ei kuitenkaan näe ilman kirjautumista.

Kirjautumisen jälkeen käyttäjä voi tarkastella sovelluksessa olevia keskusteluita, lisätä niihin vastauksia, poistamaan niitä sekä aloittaa uusia keskusteluja.

Käyttäjä pystyy poistamaan omia aloittamiaan keskusteluita ja lisäksi muokkaamaan aloittamiaan keskusteluita.

Käyttäjä pystyy tilaamaan keskustelun, jolloinka se näkyy erillisellä tilaukset-sivulla. Tilauksen pystyy myös poistamaan.

Käyttäjä pystyy myös tarkastelemaan kommenttien ja keskusteluiden määriä.

## SQL-kyselyt

### Kysely tilausten hakemiselle. Parametrina account id.
"SELECT Conversation.id, Conversation.name, Subs.conversation_id, (select COUNT(Subs.conversation_id) FROM Subs WHERE Subs.account_id=:accid) FROM Conversation LEFT JOIN Subs ON Subs.conversation_id=Conversation.id WHERE Subs.account_id=:accid"

### Kysely keskustelun kommenttien hakuun. Parametrina keskustelun id.
"SELECT Comment.id, Comment.name, Comment.conversation_id, Account.username, Comment.account_id, Comment.date_created,  (select COUNT(Comment.id) FROM Comment WHERE Comment.conversation_id=:convid) FROM Comment, Account WHERE Account.id = Comment.account_id AND Comment.conversation_id = :convid"

### Kysely keskustelun kommenttien poistamiseen. Parametrina keskustelun id. (keskustelun poistamisen yhteydessä)
"DELETE FROM Comment WHERE Comment.conversation_id = :convid"