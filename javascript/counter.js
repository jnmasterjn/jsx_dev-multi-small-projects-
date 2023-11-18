let counter=0;
    function count(){
    counter++;
    document.querySelector('h1').innerHTML=(counter);
                
    if (counter%10===0){
        alert(`The count is now ${counter}`)}
            }
    document.addEventListener("DOMContentLoaded",function(){
    document.querySelector('button').onclick=count;
    }); 
        
//addEventListener("the type of event you want to listen for", the function to run when the event is detected)
                    //ex: click, scroll                            
        