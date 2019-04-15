##Docker Image should only have _ ( underscore / low dash) no slash as well .. 
##gCloud Cluster name should only have - ( hyphen / dash ) 

   function rmimage {
      # Removing the Image .. So, need to be careful !!.
      docker rmi omdb_py3_alpine
   } 

   function stop {
   		docker stop gc_omdb_py3_alpine
   		docker rm gc_omdb_py3_alpine
   }   

   function build {
      docker build -f=../image/Dockerfile -t=omdb_py3_alpine ../image       
   }    

   function run {
   		docker run -d -P --name gc_omdb_py3_alpine -w /home/omdb -e APIKEY=ca5e163c -e PORT=8010 -p 8010:8010 omdb_py3_alpine
   		docker logs gc_omdb_py3_alpine
   } 

   function getMovieRating {
    echo ${2}    
    case "${2}" in
        '')  echo "MovieTitle 2nd argument is not set. Please enter it";;      
        *)   echo "$2: MovieTitle is set. MovieTitle: ${2}"
             curl  -G -v 'http://localhost:8010/movie' --data-urlencode "movieTitle=${2}"
             echo ""
        ;;
    esac    
   }    

   function tag {
		docker tag omdb_py3_alpine omdb_py3_alpine
   } 

   function push {
    echo "push"
   }    

if [ "$#" -lt 1 ]; then
  echo "Usage: stop-build-run-tag-push / stop-build-run-tag / stop-build-run * /  stop / getMovieRating / tag / run / push / rmimage combination is acceptable." >&2
  exit 1
fi

# idiomatic parameter and option handling in sh
while test $# -gt 0
do
    case "$1" in
        stop-build-run-tag-push) echo "Option stop-build-run-push is executing!! ";
   				stop "$*";
   				build "$*";  				
   				run "$*";
   				tag "$*";    				
   				push "$*";
            ;;
        stop-build-run-tag) echo "Option stop-build-run is executing!! ";
   				stop "$*";
   				build "$*";
   				run "$*";
   				tag "$*";    				
            ;;
        stop-build-run) echo "Option stop-build-run is executing!! ";
   				stop "$*";
   				build "$*";
   				run "$*";   				
            ;;                
        stop) echo "Option stop is executing!! ";
          stop "$*";
            ;;
        getMovieRating) echo "Option getMovieRating is executing!! ";
          getMovieRating "$@";
            ;;                    
        tag) echo "Option tag is executing!! ";
   				tag "$*";
            ;;
        run) echo "Option run is executing!! ";
   				run "$*";
            ;;
        push) echo "Option push is executing!! ";
   				push "$*";
            ;;   
        rmimage) echo "Option rmimage is executing!! ";
          rmimage "$*";
            ;;                      
        *) echo "Usage: stop-build-run-tag-push / stop-build-run-tag / copy * / stop-build-run * /  stop / getMovieRating / tag / run / push / rmimage combination is acceptable. Not $1"
            ;;
    esac
    shift
    break 1
done
