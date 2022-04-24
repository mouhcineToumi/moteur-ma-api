

class QueryBuilder:

    def __init__(self):
        pass

    def build(self, 
                      marque: str = None,
                      modele: str = None,
                      carburant: str = None,
                      boite: str = None,
                      prix_min: int = None,
                      prix_max: int = None,
                      annee_min: int = None,
                      annee_max: int = None,
                      km: int = None,
                      couleur: str = None,
                      carrosserie: str = None,
                      first_use: bool = False,
                      ville: str = None,
                      region: str = None,
                      page=1):
        base_url = "https://www.moteur.ma/fr/voiture/achat-voiture-occasion/"

        filters_prefix = "recherche/?"

        filters = []
        if marque:
            filters.append("marque="+marque)

        if modele:
            filters.append("modele="+modele)

        if carburant:
            filters.append("carburant="+carburant)

        if boite:
            filters.append("boite="+boite)

        if prix_min:
            filters.append("prix_min="+str(prix_min))

        if prix_max:
            filters.append("prix_max="+str(prix_max))

        if annee_min:
            filters.append("annee_min="+str(annee_min))

        if annee_max:
            filters.append("annee_max="+str(annee_max))

        if km:
            filters.append("km="+str(km))

        if couleur:
            filters.append("couleur="+couleur)

        if couleur:
            filters.append("couleur="+couleur)

        if carrosserie:
            filters.append("carrosserie="+carrosserie)

        if first_use:
            filters.append("first_use=1")

        # add the location
        if region:
            filters.append("region=" + '+-+'.join(region.split('-')))
        else:
            if ville:
                filters.append("ville="+ville)

        # add the page number
        if page < 1:
            page = 1

        if len(filters) == 0:
            return base_url + str((page-1)*15)

        else:
            filters.append("per_page="+str((page-1)*15))

        return base_url + filters_prefix + "&".join(filters)

