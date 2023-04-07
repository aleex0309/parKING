# ParKING
<p align="center">
  <p align="center">
    <BR>
  Web Project assignment 2022/2023 <BR>
Universtat de Lleida
</p>


Developers
-------------
- Alexandru Cristian Stoia - [@aleex0309](https://github.com/aleex0309)
- Pere Muñoz Figuerol - [@peremunoz](https://github.com/peremunoz)
- Rafel Salgueiro Santacreu [@rafelsalgueiro](https://github.com/rafelsalgueiro)
- Marc Gaspà Joval - [@marcgj](https://github.com/marcgj) 
- Andreu Pérez Torra

Usage
---------

**To Build the web:**
1. Build:
```
docker-compose up -d --build  
```
2. Run:
```
docker-compose up
```
3. Do makemigrations  & migrate in the container:

&ensp; Use ```Docker ps``` in another Terminal to see running containers and ```docker exec -t -i container_id bash``` to open container's terminal.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
4. Create superuser in the container:
```
python manage.py createsuperuser
```
5. Go to [LocalHost](http://0.0.0.0/)
