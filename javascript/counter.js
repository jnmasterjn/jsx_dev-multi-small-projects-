if (!localStorage.getItem('counter')){
    localStorage.setItem('counter',0);
}

function count(){
    let counter= localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML=counter;
    localStorage.setItem('counter', counter);
    }

    // if (counter%10===0){
    //     alert(`The count is now ${counter}`)}
    //         }

document.addEventListener("DOMContentLoaded",function(){
    document.querySelector('button').onclick=count;
    }); 

// setInterval(count,1000)    
//addEventListener("the type of event you want to listen for", the function to run when the event is detected)
                    //ex: click, scroll                            
        