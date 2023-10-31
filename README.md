# geo_graphene
This source implements geo spatial queries based on GRAPHQL API

1. Installation:

  - Download and install python3.6:
    [( https://www.python.org/downloads/ ])


  - Install MongoDB database:
    [(https://docs.mongodb.com/manual/installation/)]


  - Install pip and virtual env
    - On macOS and Linux:
      - >python3 -m pip install --user --upgrade pip
      - >python3 -m pip install --user virtualenv

    - On Windows:
      - >py -m pip install --user virtualenv


  - Clone the git repository
    - >git clone https://github.com/fabwat/geo_graphene.git
    
    
  - Inside the geo_graphene folder,create a virtual env and install the packages needed to run the program:
      - On macOS and Linux:
        - >python3 -m venv geo_graphene
        - >source geo_graphene/bin/activate
        - >pip install -r requirements.txt

      - On Windows:
        - >py -m venv geo_graphene
        - >.\geo_graphene\Scripts\activate
        - >pip install -r requirements.txt


2. How to start:
  - >source geo_graphene/bin/activate
  - >python/py app.py
   
            

3. How to
  - insert new partner:
    * address is the restaurant coordinates,
    * coverageArea is an area represented by polygon, where restaurant has delivery service.

```yaml
    mutation{
      createPartner(  input:{
      id: "121w1", 	
        tradingName: "Restaurante1",  	  	
        ownerName: "Owner",
        document: "1432132123891/0001",  	
        coverageArea:
        [
            [[[30, 20], [45, 40], [10, 40], [30, 20]]], 
          [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]] 
        ] ,    	
        address: [-46.57421, -21.785741]  	
      })   
      {
          partner {      
          id      
        }    
        res    
      }  
    } 
```

  - How to find restaurant by id
```yaml
    query{
      loadPartnerById(id:"1"){  
        id,    
        document,    
        ownerName,    
        tradingName,    
        address{    
          coordinates
        },
        coverageArea{    
          coordinates      
        }
      }
    }
```

  - How to search nearest restaurant, where point is your coordinates location. 

```yaml
    query{
      searchPartner(point:[11,11]){  
        tradingName,    
        address {    
          coordinates      
        },    
        coverageArea{    
          coordinates      
        }    
        id,    
        document    
      }    
    } 
```

