Немного кода на Django:
1) Переопределение модели пользователя.
2) API на DRF
3) Аутентификация по oauth2.

Для проверки аутентификации через VK необходимо создать файл .env, в котором следует указать ключи:
```
SOCIAL_AUTH_VK_OAUTH2_KEY=xxxxxx
SOCIAL_AUTH_VK_OAUTH2_SECRET=xxxxx
```
Пример .env(example)):