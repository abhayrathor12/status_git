const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".menu-links"),
      modeSwitch = body.querySelector(".toggle-switch")
      modeText = body.querySelector(".mode-text");


toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})

searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click" , () =>{
    body.classList.toggle("dark");
    
    if(body.classList.contains("dark")){
        modeText.innerText = "Light mode";
    }else{
        modeText.innerText = "Dark mode";
        
    }
});



function disableFieldsFirst(disable) {
    var select = document.getElementById("myList");
    var start = document.getElementsByName("start")[0];
    var end = document.getElementsByName("end")[0];
    
    select.disabled = disable;
    start.disabled = !disable;
    end.disabled = !disable;
}

