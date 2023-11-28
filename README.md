# Alembic Test
*26 November 2023*

## Summary
Implimentation of the tutorial at https://medium.com/@peytonrunyan/alembic-101-897f322c9334

This works! And it worked the first time! was able to add Alembic and create a migration, generate and upgrade the database, and then add a new column to the database and upgrade again. All without any issues.

## Commands Used:
```powershell
PS alembic init alembic
# This creates the alembic folder and the alembic.ini file

PS alembic revision --autogenerate -m 'Create dog model'
# This creates the first migration file

PS alembic upgrade head
# This creates the database and applies the first migration

# Add a new column to the dog model

PS alembic revision --autogenerate -m 'Add Breed to dog model'
PS alembic upgrade head
# This applies the second migration and the DB is updated
```

</>