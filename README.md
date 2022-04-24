# moteur-ma-api
This is an unofficial Python API for Moteur.ma


# install
```bash
pip install moteurmapy
```

# Quick Start
### Example 1: collect search results
```python

from moteurmapy import MoteurList

moteur_list = MoteurList()

url = "https://www.moteur.ma/fr/voiture/achat-voiture-occasion/recherche/?ville=rabat&per_page=30"

list_of_cars, page_count = moteur_list.run( url )

df_list = pd.DataFrame( list_of_cars )
```

### Example 2: collect details about a car

```python

from moteurmapy import MoteurDetails

moteur_details = MoteurDetails()

url = "https://www.moteur.ma/fr/voiture/achat-voiture-occasion/detail-annonce/387055/renault-scenic-.html"

details_of_one_car = moteur_details.run( url )
```


### Example 3: build queries for MoteurList

```python

from moteurmapy import QueryBuilder

query_builder = QueryBuilder()

url = query_builder.build(marque="dacia", 
                        carburant="diesel", 
                        km=20000, 
                        region="rabat-sale-kenitra", 
                        first_use=True, 
                        page=0)

```