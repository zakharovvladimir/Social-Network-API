# API for Social Network

## Description

API for Social Network is a social network API project with opportunities of posting, commenting and following.

## Techs

* Python,
* Django,
* DRF,
* JWT (Djoser)

## How to use

- Git Clone
- Python 3.7+ is necessary
- installing requirements.txt list is necessary

```bash
pip install -r requirements.txt
```

- Project run:

```bash
python manage.py runserver
```

It is necessary to be authorized to make changes

```r
GET api/v1/posts/ - Get posts list
GET api/v1/posts/{id}/ - Get ID only post
GET api/v1/groups/ - Get list of communities
GET api/v1/groups/{id}/ - Get ID only communities
GET api/v1/{post_id}/comments/ - Get post comments
GET api/v1/{post_id}/comments/{id}/ - Get ID only comments
```

## Samples

- Create post:

```r
POST /api/v1/posts/
```


```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Update post:

```r
PUT /api/v1/posts/{id}/
```


```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Partial post update:

```r
PATCH /api/v1/posts/{id}/
```


```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Delete post:

```r
DEL /api/v1/posts/{id}/
```

- Follow:

```r
GET /api/v1/follow/
```

- Pagination:

```r
GET /api/v1/posts/?limit=10&offset=0
```

### Author

Vladimir Zakharov // vladimir.zakharov.s@yandex.ru
