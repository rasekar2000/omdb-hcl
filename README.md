# OMDB API
OMDB API Data Analysis


To get 'Rotten Tomatoes' rating please use this  *OMDB HCL API Here*, check out the [OMDB API Data Analysis](https://github.com/rasekar2000/omdb-hcl) 

### Table of Contents
**[Installation Instructions](#installation-instructions)**<br>
**[Usage Instructions](#usage-instructions)**<br>
**[Test Results](#test-results)**<br>

## Installation Instructions

1. In MAC/linux, *make sure* have git installed. If not please install them. 
2. In the MAC/linux command prompt go to the terminal and execte the following instruction
   <pre>

   ```unix
   git clone https://github.com/rasekar2000/omdb-hcl.git
   ```
   </pre>

## Usage Instructions

1. In MAC, *make sure* have docker & curl installed. If not please install them. 
2. In the command prompt go to the *scripts* folder
   <pre>

   ```unix
   chmod +x docker.omdb_py3_alpine.sh
   ```
   </pre>
3. In the command prompt go to the *scripts* folder to 
   <pre>

   **build & run** `docker`.
   ```unix
   ./docker.omdb_py3_alpine.sh stop-build-run
   ```
   </pre>
4. In the command prompt go to the *scripts* folder to 

   <pre>
   **Test** `getMovieRating`.

   ```unix
   ./docker.omdb_py3_alpine.sh getMovieRating 'Guardians of the Galaxy Vol. 2'
   ```
   Input : You can give any other Movie Title
   Output : 
       Negative : {"rating": "-1%"} means No value retrieved from OMDB API
   	   Postive  : Any other rating value is retrieved from OMDB API
   </pre>

## Test Results

![screenshot of conversion](https://github.com/rasekar2000/omdb-hcl/blob/master/Install.Run.png?raw=true)

