const MAX_ROW_SIZE = 3;
var databaseIndex;
var INPUT_FILE = $.getJSON(filename, function(data){databaseIndex = data});
var warehouseObj = JSON.parse(INPUT_FILE);

<p id="Warehouse 1"></p>

<script>
document.getElementById("Warehouse 1").innerHTML =
obj.employees[1].firstName + " " + obj.employees[1].lastName;
</script>

function initWarehouses(){
    let count = 0;
    let row = 0;
    for(let i = 0; i < INPUT_FILE.length; i++){
        if(count === MAX_ROW_SIZE - 1){
            //create new row
            row++;
        }

        //create new card from INPUT_FILE[i]
        //add into row[row]
        count++;
    }
    //initialize warehouses
    //create rows of 3 cards
    //continue to create warehouse cards until JSON file complete
    
    //everytime MAX_ROW_SIZE is reached, create new row and reset
    //continue to create cards with details read from JSON file
}

function init(){
    initWarehouses();
}

/*  when it comes in i have a list in the form of a json file
    for each item in the list 
    */

    //id = "navbarHeader"
    //id = "Warehouse 1"
    //id = "Warehouse 2"
    //etc......

    //var file = $.getJSON(filename) -> parses into an object; 
    //declare dictionary var in for loop -> set equal to [i] element
    //