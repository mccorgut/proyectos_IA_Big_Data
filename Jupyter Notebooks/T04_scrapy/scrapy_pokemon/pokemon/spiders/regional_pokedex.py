import scrapy
from urllib.parse import urlencode
import requests

API_KEY = '65d6c1a7-1432-4494-8d2e-8ed1d4552e53'

class RegionalPokedexSpider(scrapy.Spider):
    response = requests.get( 
    url='https://proxy.scrapeops.io/v1/',
    params={
            'api_key': API_KEY,
            'url': 'https://www.serebii.net/pokemon/nationalpokedex.shtml', 
        },
    )
    
    name = "regional-pokedex"
    allowed_domains = ["www.serebii.net"]
    start_urls = ["https://www.serebii.net/pokemon/nationalpokedex.shtml"]
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36'
    }
    
    def parse(self, response):
        # Find the table containing the Pokémon data
        table = response.css('table.dextable')
        # table = response.css('tr>td.fooinfo::text').getall()

        # Iterate over all the rows of the table (skipping header rows)
        rows = table.css('tr')
        
        with open("response.html", "wb") as f:
            f.write(response.body)
            
        print(response.headers)    
        
        rows = table.css('tr')
        
        print("Tabla: ", len(table))
        
        print("Filas: ", len(rows))
        
        # Loop through the rows (excluding the header rows)
        for i, row in enumerate(rows[2:]):  
            cells = row.css('td')

            # skipp rows without data
            if len(cells) < 12:
                continue

            # extracts data for each pokemon
            pokedex_number = cells[0].css('::text').get().strip()  
            image_url = cells[1].css('img::attr(src)').get(default="N/A")
            name = cells[3].css('a::text').get().strip()   
            types = [
               img.css('img::attr(src)').get().split('/')[-1].replace('.gif', '')
               for img in cells[4].css('a img')
            ]
            # abilities = cells[5].css('::text').getall()  
            
            abilities = [ability.strip() for ability in cells[5].css('::text').getall() if ability.strip()]
            abilities = ", ".join(abilities) 
            
            base_stats = [cell.css('::text').get().strip() for cell in cells[6:12]]  
            
            yield {
                #'row_index': i + 2,  # adjust index to match the row's position
                'pokedex_number': pokedex_number,
                'image_url': image_url,
                'name': name,
                'types': types,
                'abilities': abilities,
                'base_stats': base_stats,
            }
        
        """
        for i, row in enumerate(rows):
            cells = row.css('td')
            
            # Extract row data and clean it
            row_data = [cell.css('::text').getall() for cell in cells]
            row_data = [' '.join(cell).strip() for cell in row_data]
            
            # Extract image URLs
            image_urls = [
                cell.css('img::attr(src)').get(default="N/A") for cell in cells
            ]
             
            yield {
                'row_index': i,
                'row_data': row_data,
                'image_urls': image_urls,     
            }
         """
         
