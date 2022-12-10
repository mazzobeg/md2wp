# Wordpress interactioner cli
The project represent a functional POC for interacting with your wordpress webapp.

## Purpose
### Main
- From markdown article to publish wordpress article
### Secondary
- List your posts contents
- Upload media (image)


## Instalation
1. Create a 'venv.json' file in the directory.
2. Fill it with followed arguements: 
```json
{
    "WP_URL":"example.com",
    "USERNAME":"username",
    "PASSWORD":"password"
}
``` 
Your password must be generated on your wordrpess profil (see xxx).
3. (a) Installation
```
pip install .
```

## Usage
List your posts contents :
```
md2wp list
```
Create post based on your markdown file :
```
md2wp add <path_to_markdown_file>
```

## Improvement
Do not esitate to post a new feature request I will implement it.

